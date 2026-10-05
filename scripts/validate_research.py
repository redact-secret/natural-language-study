"""Validate research structure; linguistic claims still require human review."""

import json
import re
from pathlib import Path
from urllib.parse import unquote

import jsonschema
import yaml


ROOT = Path(__file__).resolve().parents[1]
ERRORS = []
SECTIONS = (
    "Question and scope", "Observation", "Illustrative examples and contrasts",
    "NER hypothesis", "Evidence handoff", "Evaluation handoff",
    "Implementation options", "Limitations and review",
    "Downstream outcomes and revisions",
)


class MetadataLoader(yaml.SafeLoader):
    pass


# Keep dates as ISO strings so the JSON Schema format checker sees them.
MetadataLoader.yaml_implicit_resolvers = {
    key: [(tag, regex) for tag, regex in values
          if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f"duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


MetadataLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping
)


def error(path, message):
    ERRORS.append(f"{path.relative_to(ROOT)}: {message}")


def frontmatter(path, schema_name):
    text = path.read_text()
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not match:
        error(path, "missing YAML front matter")
        return None
    try:
        data = yaml.load(match[1], Loader=MetadataLoader)
        schema = json.loads((ROOT / "schemas" / schema_name).read_text())
        validator = jsonschema.Draft202012Validator(
            schema, format_checker=jsonschema.FormatChecker()
        )
        problems = list(validator.iter_errors(data))
        for problem in problems:
            error(path, f"{list(problem.path)}: {problem.message}")
        return None if problems else data
    except (ValueError, yaml.YAMLError) as exc:
        error(path, str(exc))
        return None


def anchors(text):
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    result, counts = set(), {}
    for heading in re.findall(r"^#{1,6} (.+)$", text, re.M):
        slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        count = counts.get(slug, 0)
        result.add(f"{slug}-{count}" if count else slug)
        counts[slug] = count + 1
    return result


def main():
    findings, prefixes = {}, set()
    for overview in sorted((ROOT / "studies").glob("*/overview.md")):
        meta = frontmatter(overview, "overview.schema.json")
        if meta is None:
            continue
        dossier = overview.parent
        prefix = meta["id_prefix"]
        if prefix in prefixes:
            error(overview, f"duplicate prefix {prefix}")
        prefixes.add(prefix)
        if meta["language_key"] != dossier.name:
            error(overview, "language_key does not match directory")
        source_path = dossier / "sources.md"
        if not source_path.exists():
            error(overview, "missing sources.md")
            continue
        sources = set()
        for block in re.findall(r"```yaml\n(.*?)\n```", source_path.read_text(), re.S):
            try:
                record = yaml.load(block, Loader=MetadataLoader)
                required = {"id", "title", "authors_or_institution", "publication_date",
                            "url_or_identifier", "accessed", "source_type", "language_scope",
                            "relevant_locators", "reuse_terms", "limitations"}
                if not isinstance(record, dict) or not required <= record.keys():
                    raise ValueError("incomplete source record")
                sid = record["id"]
                if not isinstance(sid, str) or not re.fullmatch(prefix + r"-S\d{3,}", sid):
                    raise ValueError(f"invalid source ID: {sid}")
                if sid in sources:
                    error(source_path, f"duplicate source ID {sid}")
                sources.add(sid)
                jsonschema.FormatChecker().check(record["accessed"], "date")
                if record["publication_date"] is not None:
                    jsonschema.FormatChecker().check(record["publication_date"], "date")
                if not record["relevant_locators"] or not record["limitations"]:
                    error(source_path, f"{sid}: missing locator or limitation")
            except (ValueError, yaml.YAMLError, jsonschema.exceptions.FormatError) as exc:
                error(source_path, str(exc))
        if not sources:
            error(source_path, "no structured source records")
        for path in sorted((dossier / "findings").glob("*.md")):
            data = frontmatter(path, "finding.schema.json")
            if data is None:
                continue
            fid = data["id"]
            if fid in findings:
                error(path, f"duplicate finding {fid}")
            findings[fid] = (path, data)
            if path.stem != fid or not fid.startswith(prefix + "-"):
                error(path, "finding ID, filename or dossier prefix disagree")
            if not data["language_tags"] or not set(data["language_tags"]) <= set(meta["language_tags"]):
                error(path, "finding language tags are outside dossier scope")
            if data["updated"] < data["created"]:
                error(path, "updated precedes created")
            text = path.read_text()
            for sid in data["source_ids"]:
                if sid not in sources:
                    error(path, f"unresolved source {sid}")
                if f"../sources.md#{sid.lower()}" not in text:
                    error(path, f"source {sid} has no body citation")
            body_ids = set(re.findall(r"\b[A-Z]{3}-S\d{3,}\b", text.split("---\n", 2)[-1]))
            if body_ids - set(data["source_ids"]):
                error(path, "body source citations absent from source_ids")
            for section in SECTIONS:
                if f"## {section}\n" not in text:
                    error(path, f"missing section: {section}")
            if not re.search(r"\b(synthetic|adapted|attested)\b", text):
                error(path, "missing example provenance")
            if data["hypothesis_outcome"] != "untested" and not data["downstream"]["ner_eval"]:
                error(path, "tested outcome requires a downstream evaluation link")
            if data["status"] == "superseded" and not data["superseded_by"]:
                error(path, "superseded finding requires a replacement")
            if f"findings/{fid}.md" not in overview.read_text():
                error(overview, f"finding {fid} not indexed")
    for path, data in findings.values():
        for fid in data["supersedes"] + data["superseded_by"]:
            if fid not in findings or fid == data["id"]:
                error(path, f"invalid supersession reference {fid}")
    if not findings:
        error(ROOT / "studies", "no findings discovered")
    # Check all authored Markdown, including source anchors and local epic links.
    docs = [p for p in ROOT.rglob("*.md")
            if not any(part in {".git", ".venv", "graft", "__pycache__"}
                       for part in p.relative_to(ROOT).parts)]
    for path in docs:
        text = path.read_text()
        if not text.endswith("\n"):
            error(path, "missing final newline")
        prose = re.sub(r"```.*?```", "", text, flags=re.S)
        for destination in re.findall(r"\[[^\]]+\]\(([^)]+)\)", prose):
            if re.match(r"[a-z]+:", destination):
                continue
            target, _, anchor = unquote(destination).partition("#")
            resolved = (path.parent / target).resolve() if target else path
            if not resolved.is_relative_to(ROOT) or not resolved.exists():
                error(path, f"broken local link {destination}")
            elif anchor and resolved.suffix == ".md" and anchor not in anchors(resolved.read_text()):
                error(path, f"broken anchor {destination}")
    if ERRORS:
        print("\n".join(ERRORS))
        raise SystemExit(1)
    print(f"Validated {len(prefixes)} dossiers, {len(findings)} findings and {len(docs)} Markdown files.")


if __name__ == "__main__":
    main()
