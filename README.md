# standard-nist-genai-profile

The **NIST AI RMF Generative AI Profile** (NIST AI 600-1) expressed as a
[throughline](https://pypi.org/project/throughline/) **source** — a standalone, grounded
requirements graph that a consuming project composes with
[throughline-compose](https://github.com/timebacksolutions/throughline-compose).

NIST AI 600-1 is a *cross-sectoral profile* of the AI RMF: for the Subcategories where
generative AI raises distinct concerns, it lists **suggested Actions** and the **GenAI risks**
each Action helps address. This repository re-expresses those Actions as a grounded IDD graph.

This repository holds no application code. It is a directory of small YAML items with
permanent UIDs, validated by `tl check`. Consumers import it under a namespace and
reference its outcomes as `genai:SR-0007`.

## Status

A grounded graph of
<!-- tl:count type == 'intent' -->
4
<!-- tl:end --> Function intents,
<!-- tl:count type == 'user_requirement' -->
49
<!-- tl:end --> Subcategory requirements and
<!-- tl:count type == 'system_requirement' -->
212
<!-- tl:end --> suggested Actions, published to [`docs/spec.md`](docs/spec.md). The
counts are rendered from the live graph by `tl:count`, so they cannot drift.

## Why this source is multi-root

A throughline source gets **as many root intents as the standard has genuine "why"s** — a
single umbrella root would throw away the reason each outcome exists, which is the whole
point of IDD. A single artificial `INT-0001` that every requirement ultimately hangs off is
the **anti-pattern**: it flattens four distinct governance purposes into one bland "…exists".

The AI RMF Core is organised under **four Functions**, and those are four genuinely
different reasons the framework exists — governing the programme is not the same "why" as
mapping context, measuring risk, or managing response. The Generative AI Profile hangs its
Actions onto that same Core, so this graph has **four co-equal root intents** (all
`normative: false`), each carrying its Function's AI RMF statement as its `text`:

| Root | Function |
|---|---|
| `INT-0001` | **GOVERN** — cultivate a culture of GenAI risk management |
| `INT-0002` | **MAP** — recognise context and identify GenAI risks |
| `INT-0003` | **MEASURE** — assess, analyse and track GenAI risks |
| `INT-0004` | **MANAGE** — prioritise and act on GenAI risks |

- Each **Subcategory the Profile gives Actions for** (`GOVERN 4.3`, `MEASURE 2.7`, …) is a
  `user_requirement` that `derives_from` **its own Function** (a `MAP 4.1` subcategory →
  `INT-0002`, never a catch-all), carrying the Subcategory's AI RMF outcome statement as its
  `text`. The Profile addresses 49 of the AI RMF's 72 Subcategories.
- Each **suggested Action** (`GV-4.3-001`, …) is a `system_requirement` that `implements` its
  Subcategory. A Subcategory belongs to exactly one Function, so an Action grounds up to a
  Function through `implements` → `derives_from` with no extra edge.

## GenAI risks are a cross-cut, not roots

Every Action is tagged with the **GenAI risks** it addresses, carried in
`attrs.genai_risks` (a list). The twelve risks NIST AI 600-1 defines are:

CBRN Information or Capabilities · Confabulation · Dangerous, Violent, or Hateful Content ·
Data Privacy · Environmental · Harmful Bias and Homogenization · Human-AI Configuration ·
Information Integrity · Information Security · Intellectual Property · Obscene, Degrading,
and/or Abusive Content · Value Chain and Component Integration.

They are a **many-to-many cross-cut** — one Action addresses several risks, one risk is
addressed by many Actions across all four Functions — so they are a sub-filter attribute,
**not** roots. Making them roots would either duplicate Actions or flatten the Function
spine, exactly the anti-pattern the four-Function split exists to avoid. (This is the same
role `attrs.level` plays in ASVS and `attrs.wcag_version` in WCAG.)

## No levels — editions are git tags

NIST AI 600-1 **grades no Action by an assurance level**, so there is no `attrs.level`. The
metadata carried on each Action is:

- `attrs.source_ref` — the published AI 600-1 Action id (`GV-4.3-001`), never the UID.
- `attrs.subcategory` — the parent AI RMF Subcategory id (`GOVERN 4.3`).
- `attrs.genai_risks` — the GenAI risks the Action addresses.

**Editions are git tags of this one repo.** `v1.0` tags the NIST AI 600-1 (2024) edition; a
future revision would be a new tag on this same repo. A consumer pins `genai@v1.0`. This is
the same editions-as-tags model as `standard-asvs`, `standard-nist-ai-rmf` and `standard-wcag`.

## Modelling conventions

- **throughline UIDs are this source's own** (`SR-0007`…), immutable and never the AI 600-1
  id. The AI 600-1 id lives in `attrs.source_ref`.
- **Item `text`** is the AI RMF Function / Subcategory statement or the suggested-Action text,
  taken from the authoritative NIST source (see `NOTICE`).
- The graph is generated from the vendored NIST data under `tools/airmf-genai-1.0/`
  (`functions.json` + `subcategories.json` = the AI RMF Core statements, `actions.json` = the
  212 suggested Actions extracted from NIST AI 600-1 by `extract_actions.py` from the vendored
  `nist-ai-600-1.layout.txt`) by `tools/generate.py` (permanent-UID, additive). Editing the
  graph means editing the vendored data + generator, not the YAML by hand.

## Composing it

In a consuming project's `throughline.toml`:

```toml
[sources.genai]
url = "https://github.com/timebacksolutions/standard-nist-genai-profile"
ref = "v1.0"
```

Then reference a suggested Action as `genai:SR-0001` from your own items. This Profile is the
GenAI-specific **operational partner** to
[`standard-nist-ai-rmf`](https://github.com/timebacksolutions/standard-nist-ai-rmf): the base
AI RMF frames the governance outcomes, this Profile lists the concrete GenAI Actions that
satisfy them. It also pairs with
[`standard-aisvs`](https://github.com/timebacksolutions/standard-aisvs), which verifies an AI
application's *controls* — a consumer can compose all three.

## Licence

Repository structure, tooling and configuration: Apache-2.0 (see `LICENSE`). The AI RMF
statements and NIST AI 600-1 suggested Actions are works of the US Federal Government in the
**public domain** (17 U.S.C. § 105) — see `NOTICE`. Authoritative source:
https://www.nist.gov/itl/ai-risk-management-framework and NIST AI 600-1.
