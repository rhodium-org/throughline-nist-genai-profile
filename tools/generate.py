#!/usr/bin/env python3
"""Generate the NIST AI RMF Generative AI Profile (NIST AI 600-1) throughline source.

Vendored NIST inputs live under ``tools/airmf-genai-1.0/`` (public domain — a work of the
US Federal Government, 17 U.S.C. Sec. 105):

* ``functions.json`` — the four AI RMF Function statements (GOVERN / MAP / MEASURE /
  MANAGE), reused from the base AI RMF Core; each is a root intent's ``text``.
* ``subcategories.json`` — the 49 AI RMF Subcategory outcome statements that the Profile
  gives suggested Actions for (keyed ``"GOVERN 4.3"``); each is a user_requirement's
  ``text``.
* ``actions.json`` — the 212 suggested Actions extracted from NIST AI 600-1 Tables (see
  ``extract_actions.py`` + ``nist-ai-600-1.layout.txt``); each is a system_requirement,
  with the Action text as ``text``, the GenAI risks it addresses in ``attrs.genai_risks``,
  and its parent Subcategory id in ``attrs.subcategory``.

**UIDs are permanent.** The mapping from a Function / Subcategory / Action to a throughline
UID is derived from the items already on disk, keyed by ``attrs.source_ref`` (the NIST
handle: ``"GOVERN"``, ``"GOVERN 4.3"``, ``"GV-4.3-001"``). Anything without an item yet gets
a freshly allocated UID in document order; a UID, once allocated, never moves. Bodies
regenerate from the vendored data each run.

**Multi-root by design.** GOVERN / MAP / MEASURE / MANAGE are four genuinely different
reasons the framework exists, so there are four co-equal root intents (INT-0001..INT-0004),
never a single "manage GenAI risk" umbrella. Each Subcategory the Profile addresses is a
user_requirement that ``derives_from`` its own Function; each suggested Action is a
system_requirement that ``implements`` its Subcategory. A Subcategory belongs to exactly one
Function, so an Action grounds to its Function up implements->derives_from with no extra
edge. The 12 GenAI risks are a many-to-many cross-cut carried in ``attrs.genai_risks``, not
roots. Editions are git tags of this one repo.

Usage:  python tools/generate.py
"""
from __future__ import annotations

import json
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
DATA_DIR = REPO / "tools" / "airmf-genai-1.0"
INTENTS_DIR = REPO / "intents"          # intent (Function roots), prefix INT
SUBCATS_DIR = REPO / "subcategories"    # user_requirement (Subcategories), prefix UR
ACTIONS_DIR = REPO / "actions"          # system_requirement (Actions), prefix SR
SPEC = REPO / "docs" / "spec.md"

FUNCTION_ORDER = ["GOVERN", "MAP", "MEASURE", "MANAGE"]
FUNCTION_TITLE = {
    "GOVERN": "GOVERN \u2014 cultivate a culture of GenAI risk management",
    "MAP": "MAP \u2014 recognise context and identify GenAI risks",
    "MEASURE": "MEASURE \u2014 assess, analyse and track GenAI risks",
    "MANAGE": "MANAGE \u2014 prioritise and act on GenAI risks",
}


def _sub_sort(sub_id: str) -> tuple[int, int, int]:
    fn, num = sub_id.split()
    major, minor = num.split(".")
    return (FUNCTION_ORDER.index(fn), int(major), int(minor))


def _act_sort(act_id: str) -> tuple:
    # "GV-4.3-001" -> (function, major, minor, seq)
    prefix, num, seq = act_id.split("-")
    fn = {"GV": "GOVERN", "MP": "MAP", "MS": "MEASURE", "MG": "MANAGE"}[prefix]
    major, minor = num.split(".")
    return (FUNCTION_ORDER.index(fn), int(major), int(minor), int(seq))


def _dump(path: Path, item: dict) -> None:
    path.write_text(
        yaml.safe_dump(item, sort_keys=False, allow_unicode=True, width=90),
        encoding="utf-8",
    )


def _scan(dir_: Path) -> dict[str, str]:
    ref2uid: dict[str, str] = {}
    for f in dir_.glob("*.yml"):
        data = yaml.safe_load(f.read_text(encoding="utf-8"))
        ref = (data.get("attrs") or {}).get("source_ref")
        if ref:
            ref2uid[ref] = data["uid"]
    return ref2uid


def _max(ref2uid: dict[str, str], prefix: str) -> int:
    return max((int(u.split("-")[1]) for u in ref2uid.values()
               if u.startswith(prefix + "-")), default=0)


def generate() -> dict[str, int]:
    functions = json.loads((DATA_DIR / "functions.json").read_text(encoding="utf-8"))
    subcats = json.loads((DATA_DIR / "subcategories.json").read_text(encoding="utf-8"))
    actions = json.loads((DATA_DIR / "actions.json").read_text(encoding="utf-8"))

    int_ref = _scan(INTENTS_DIR)
    ur_ref = _scan(SUBCATS_DIR)
    sr_ref = _scan(ACTIONS_DIR)
    n_int = _max(int_ref, "INT") + 1
    n_ur = _max(ur_ref, "UR") + 1
    n_sr = _max(sr_ref, "SR") + 1
    counts = {"int": 0, "ur": 0, "sr": 0}

    # Functions -> root intents
    for fn in FUNCTION_ORDER:
        int_uid = int_ref.get(fn)
        if int_uid is None:
            int_uid = f"INT-{n_int:04d}"; n_int += 1; int_ref[fn] = int_uid
            counts["int"] += 1
        _dump(INTENTS_DIR / f"{int_uid}.yml", {
            "uid": int_uid,
            "type": "intent",
            "status": "approved",
            "title": FUNCTION_TITLE[fn],
            "text": functions[fn],
            "normative": False,
            "attrs": {"source_ref": fn},
        })

    # Subcategories the Profile addresses -> user_requirements
    fn_of_sub = {sub: sub.split()[0] for sub in subcats}
    for sub_id in sorted(subcats, key=_sub_sort):
        fn = fn_of_sub[sub_id]
        ur_uid = ur_ref.get(sub_id)
        if ur_uid is None:
            ur_uid = f"UR-{n_ur:04d}"; n_ur += 1; ur_ref[sub_id] = ur_uid
            counts["ur"] += 1
        _dump(SUBCATS_DIR / f"{ur_uid}.yml", {
            "uid": ur_uid,
            "type": "user_requirement",
            "status": "approved",
            "title": sub_id,
            "text": subcats[sub_id],
            "links": [{"target": int_ref[fn], "type": "derives_from"}],
            "attrs": {"source_ref": sub_id},
        })

    # Suggested Actions -> system_requirements
    for act in sorted(actions, key=lambda a: _act_sort(a["id"])):
        act_id = act["id"]
        sub_id = act["subcat"]
        sr_uid = sr_ref.get(act_id)
        if sr_uid is None:
            sr_uid = f"SR-{n_sr:04d}"; n_sr += 1; sr_ref[act_id] = sr_uid
            counts["sr"] += 1
        attrs = {"source_ref": act_id, "subcategory": sub_id}
        if act.get("risks"):
            attrs["genai_risks"] = act["risks"]
        _dump(ACTIONS_DIR / f"{sr_uid}.yml", {
            "uid": sr_uid,
            "type": "system_requirement",
            "status": "approved",
            "title": f"NIST AI 600-1 {act_id}",
            "text": act["text"],
            "links": [{"target": ur_ref[sub_id], "type": "implements"}],
            "attrs": attrs,
        })

    return counts


SPEC_HEADER = """\
# NIST AI RMF Generative AI Profile (NIST AI 600-1) \u2014 throughline source

Generated from the graph. Prose between `tl:item` / `tl:table` markers is injected by
`tl docs` \u2014 edit the vendored data (`tools/airmf-genai-1.0/*.json`) + `tools/generate.py`,
not the injected regions.

The "why" spine is **multi-root by design**: the AI RMF's four Functions
(GOVERN / MAP / MEASURE / MANAGE) are four distinct reasons the framework exists \u2014 four
root `intent`s, not one umbrella. Each Subcategory the Generative AI Profile gives suggested
Actions for is a `user_requirement` that `derives_from` its Function; each suggested Action
is a `system_requirement` that `implements` its Subcategory, carrying the GenAI risks it
addresses in `attrs.genai_risks` and its parent Subcategory in `attrs.subcategory`. The NIST
AI 600-1 id lives in `attrs.source_ref` (the Subcategory `"GOVERN 4.3"`, the Action
`"GV-4.3-001"`); the Profile grades no Action by level.
"""


def generate_spec() -> None:
    subcats = json.loads((DATA_DIR / "subcategories.json").read_text(encoding="utf-8"))
    int_ref = _scan(INTENTS_DIR)
    ur_ref = _scan(SUBCATS_DIR)
    parts = [SPEC_HEADER]
    for fn in FUNCTION_ORDER:
        parts.append(f"# {fn} \u2014 the root\n")
        parts.append(f"<!-- tl:item {int_ref[fn]} -->\n<!-- tl:end -->\n")
        subs = sorted((s for s in subcats if s.split()[0] == fn), key=_sub_sort)
        for sub_id in subs:
            parts.append(f"## {sub_id}\n")
            parts.append(f"<!-- tl:item {ur_ref[sub_id]} -->\n<!-- tl:end -->\n")
            flt = ("type == 'system_requirement' and "
                   f"attrs.get('subcategory', '') == '{sub_id}'")
            parts.append(f"<!-- tl:table {flt} -->\n<!-- tl:end -->\n")
    SPEC.parent.mkdir(parents=True, exist_ok=True)
    SPEC.write_text("\n".join(parts) + "\n", encoding="utf-8")


def main() -> int:
    c = generate()
    generate_spec()
    print(f"intents:       {c['int']} new (Functions / root intents)")
    print(f"subcategories: {c['ur']} new (user_requirements)")
    print(f"actions:       {c['sr']} new (system_requirements)")
    print(f"totals: {len(list(INTENTS_DIR.glob('INT-*.yml')))} INT, "
          f"{len(list(SUBCATS_DIR.glob('UR-*.yml')))} UR, "
          f"{len(list(ACTIONS_DIR.glob('SR-*.yml')))} SR")
    print("next: run `tl docs` to inject content, then `tl check --strict`")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
