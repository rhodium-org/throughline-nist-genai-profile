# NIST AI RMF Generative AI Profile (NIST AI 600-1) — throughline source

Generated from the graph. Prose between `tl:item` / `tl:table` markers is injected by
`tl docs` — edit the vendored data (`tools/airmf-genai-1.0/*.json`) + `tools/generate.py`,
not the injected regions.

The "why" spine is **multi-root by design**: the AI RMF's four Functions
(GOVERN / MAP / MEASURE / MANAGE) are four distinct reasons the framework exists — four
root `intent`s, not one umbrella. Each Subcategory the Generative AI Profile gives suggested
Actions for is a `user_requirement` that `derives_from` its Function; each suggested Action
is a `system_requirement` that `implements` its Subcategory, carrying the GenAI risks it
addresses in `attrs.genai_risks` and its parent Subcategory in `attrs.subcategory`. The NIST
AI 600-1 id lives in `attrs.source_ref` (the Subcategory `"GOVERN 4.3"`, the Action
`"GV-4.3-001"`); the Profile grades no Action by level.

# GOVERN — the root

<!-- tl:item INT-0001 -->
**INT-0001 — GOVERN — cultivate a culture of GenAI risk management** — `intent`, status `approved`

> A culture of risk management is cultivated and present. The GOVERN function cultivates and implements a culture of risk management within organizations designing, developing, deploying, evaluating, or acquiring AI systems, and provides a structure by which AI risk management functions can align with organizational principles, policies, and strategic priorities.

**source_ref**: GOVERN
<!-- tl:end -->

## GOVERN 1.1

<!-- tl:item UR-0001 -->
**UR-0001 — GOVERN 1.1** — `user_requirement`, status `approved`

> Legal and regulatory requirements involving AI are understood, managed, and documented.

*Derives from:* INT-0001

**source_ref**: GOVERN 1.1
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'GOVERN 1.1' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0001 | system_requirement | approved | NIST AI 600-1 GV-1.1-001 |
<!-- tl:end -->

## GOVERN 1.2

<!-- tl:item UR-0002 -->
**UR-0002 — GOVERN 1.2** — `user_requirement`, status `approved`

> The characteristics of trustworthy AI are integrated into organizational policies, processes, procedures, and practices.

*Derives from:* INT-0001

**source_ref**: GOVERN 1.2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'GOVERN 1.2' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0002 | system_requirement | approved | NIST AI 600-1 GV-1.2-001 |
| SR-0003 | system_requirement | approved | NIST AI 600-1 GV-1.2-002 |
<!-- tl:end -->

## GOVERN 1.3

<!-- tl:item UR-0003 -->
**UR-0003 — GOVERN 1.3** — `user_requirement`, status `approved`

> Processes, procedures, and practices are in place to determine the needed level of risk management activities based on the organization's risk tolerance.

*Derives from:* INT-0001

**source_ref**: GOVERN 1.3
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'GOVERN 1.3' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0004 | system_requirement | approved | NIST AI 600-1 GV-1.3-001 |
| SR-0005 | system_requirement | approved | NIST AI 600-1 GV-1.3-002 |
| SR-0006 | system_requirement | approved | NIST AI 600-1 GV-1.3-003 |
| SR-0007 | system_requirement | approved | NIST AI 600-1 GV-1.3-004 |
| SR-0008 | system_requirement | approved | NIST AI 600-1 GV-1.3-005 |
| SR-0009 | system_requirement | approved | NIST AI 600-1 GV-1.3-006 |
| SR-0010 | system_requirement | approved | NIST AI 600-1 GV-1.3-007 |
<!-- tl:end -->

## GOVERN 1.4

<!-- tl:item UR-0004 -->
**UR-0004 — GOVERN 1.4** — `user_requirement`, status `approved`

> The risk management process and its outcomes are established through transparent policies, procedures, and other controls based on organizational risk priorities.

*Derives from:* INT-0001

**source_ref**: GOVERN 1.4
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'GOVERN 1.4' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0011 | system_requirement | approved | NIST AI 600-1 GV-1.4-001 |
| SR-0012 | system_requirement | approved | NIST AI 600-1 GV-1.4-002 |
<!-- tl:end -->

## GOVERN 1.5

<!-- tl:item UR-0005 -->
**UR-0005 — GOVERN 1.5** — `user_requirement`, status `approved`

> Ongoing monitoring and periodic review of the risk management process and its outcomes are planned, and organizational roles and responsibilities are clearly defined, including determining the frequency of periodic review.

*Derives from:* INT-0001

**source_ref**: GOVERN 1.5
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'GOVERN 1.5' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0013 | system_requirement | approved | NIST AI 600-1 GV-1.5-001 |
| SR-0014 | system_requirement | approved | NIST AI 600-1 GV-1.5-002 |
| SR-0015 | system_requirement | approved | NIST AI 600-1 GV-1.5-003 |
<!-- tl:end -->

## GOVERN 1.6

<!-- tl:item UR-0006 -->
**UR-0006 — GOVERN 1.6** — `user_requirement`, status `approved`

> Mechanisms are in place to inventory AI systems and are resourced according to organizational risk priorities.

*Derives from:* INT-0001

**source_ref**: GOVERN 1.6
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'GOVERN 1.6' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0016 | system_requirement | approved | NIST AI 600-1 GV-1.6-001 |
| SR-0017 | system_requirement | approved | NIST AI 600-1 GV-1.6-002 |
| SR-0018 | system_requirement | approved | NIST AI 600-1 GV-1.6-003 |
<!-- tl:end -->

## GOVERN 1.7

<!-- tl:item UR-0007 -->
**UR-0007 — GOVERN 1.7** — `user_requirement`, status `approved`

> Processes and procedures are in place for decommissioning and phasing out AI systems safely and in a manner that does not increase risks or decrease the organization's trustworthiness.

*Derives from:* INT-0001

**source_ref**: GOVERN 1.7
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'GOVERN 1.7' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0019 | system_requirement | approved | NIST AI 600-1 GV-1.7-001 |
| SR-0020 | system_requirement | approved | NIST AI 600-1 GV-1.7-002 |
<!-- tl:end -->

## GOVERN 2.1

<!-- tl:item UR-0008 -->
**UR-0008 — GOVERN 2.1** — `user_requirement`, status `approved`

> Roles and responsibilities and lines of communication related to mapping, measuring, and managing AI risks are documented and are clear to individuals and teams throughout the organization.

*Derives from:* INT-0001

**source_ref**: GOVERN 2.1
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'GOVERN 2.1' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0021 | system_requirement | approved | NIST AI 600-1 GV-2.1-001 |
| SR-0022 | system_requirement | approved | NIST AI 600-1 GV-2.1-002 |
| SR-0023 | system_requirement | approved | NIST AI 600-1 GV-2.1-003 |
| SR-0024 | system_requirement | approved | NIST AI 600-1 GV-2.1-004 |
| SR-0025 | system_requirement | approved | NIST AI 600-1 GV-2.1-005 |
<!-- tl:end -->

## GOVERN 3.2

<!-- tl:item UR-0009 -->
**UR-0009 — GOVERN 3.2** — `user_requirement`, status `approved`

> Policies and procedures are in place to define and differentiate roles and responsibilities for human-AI configurations and oversight of AI systems.

*Derives from:* INT-0001

**source_ref**: GOVERN 3.2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'GOVERN 3.2' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0026 | system_requirement | approved | NIST AI 600-1 GV-3.2-001 |
| SR-0027 | system_requirement | approved | NIST AI 600-1 GV-3.2-002 |
| SR-0028 | system_requirement | approved | NIST AI 600-1 GV-3.2-003 |
| SR-0029 | system_requirement | approved | NIST AI 600-1 GV-3.2-004 |
| SR-0030 | system_requirement | approved | NIST AI 600-1 GV-3.2-005 |
<!-- tl:end -->

## GOVERN 4.1

<!-- tl:item UR-0010 -->
**UR-0010 — GOVERN 4.1** — `user_requirement`, status `approved`

> Organizational policies and practices are in place to foster a critical thinking and safety-first mindset in the design, development, deployment, and uses of AI systems to minimize potential negative impacts.

*Derives from:* INT-0001

**source_ref**: GOVERN 4.1
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'GOVERN 4.1' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0031 | system_requirement | approved | NIST AI 600-1 GV-4.1-001 |
| SR-0032 | system_requirement | approved | NIST AI 600-1 GV-4.1-002 |
| SR-0033 | system_requirement | approved | NIST AI 600-1 GV-4.1-003 |
<!-- tl:end -->

## GOVERN 4.2

<!-- tl:item UR-0011 -->
**UR-0011 — GOVERN 4.2** — `user_requirement`, status `approved`

> Organizational teams document the risks and potential impacts of the AI technology they design, develop, deploy, evaluate, and use, and they communicate about the impacts more broadly.

*Derives from:* INT-0001

**source_ref**: GOVERN 4.2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'GOVERN 4.2' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0034 | system_requirement | approved | NIST AI 600-1 GV-4.2-001 |
| SR-0035 | system_requirement | approved | NIST AI 600-1 GV-4.2-002 |
| SR-0036 | system_requirement | approved | NIST AI 600-1 GV-4.2-003 |
<!-- tl:end -->

## GOVERN 4.3

<!-- tl:item UR-0012 -->
**UR-0012 — GOVERN 4.3** — `user_requirement`, status `approved`

> Organizational practices are in place to enable AI testing, identification of incidents, and information sharing.

*Derives from:* INT-0001

**source_ref**: GOVERN 4.3
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'GOVERN 4.3' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0037 | system_requirement | approved | NIST AI 600-1 GV-4.3-001 |
| SR-0038 | system_requirement | approved | NIST AI 600-1 GV-4.3-002 |
| SR-0039 | system_requirement | approved | NIST AI 600-1 GV-4.3-003 |
<!-- tl:end -->

## GOVERN 5.1

<!-- tl:item UR-0013 -->
**UR-0013 — GOVERN 5.1** — `user_requirement`, status `approved`

> Organizational policies and practices are in place to collect, consider, prioritize, and integrate feedback from those external to the team that developed or deployed the AI system regarding the potential individual and societal impacts related to AI risks.

*Derives from:* INT-0001

**source_ref**: GOVERN 5.1
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'GOVERN 5.1' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0040 | system_requirement | approved | NIST AI 600-1 GV-5.1-001 |
| SR-0041 | system_requirement | approved | NIST AI 600-1 GV-5.1-002 |
<!-- tl:end -->

## GOVERN 6.1

<!-- tl:item UR-0014 -->
**UR-0014 — GOVERN 6.1** — `user_requirement`, status `approved`

> Policies and procedures are in place that address AI risks associated with third-party entities, including risks of infringement of a third-party's intellectual property or other rights.

*Derives from:* INT-0001

**source_ref**: GOVERN 6.1
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'GOVERN 6.1' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0042 | system_requirement | approved | NIST AI 600-1 GV-6.1-001 |
| SR-0043 | system_requirement | approved | NIST AI 600-1 GV-6.1-002 |
| SR-0044 | system_requirement | approved | NIST AI 600-1 GV-6.1-003 |
| SR-0045 | system_requirement | approved | NIST AI 600-1 GV-6.1-004 |
| SR-0046 | system_requirement | approved | NIST AI 600-1 GV-6.1-005 |
| SR-0047 | system_requirement | approved | NIST AI 600-1 GV-6.1-006 |
| SR-0048 | system_requirement | approved | NIST AI 600-1 GV-6.1-007 |
| SR-0049 | system_requirement | approved | NIST AI 600-1 GV-6.1-008 |
| SR-0050 | system_requirement | approved | NIST AI 600-1 GV-6.1-009 |
| SR-0051 | system_requirement | approved | NIST AI 600-1 GV-6.1-010 |
<!-- tl:end -->

## GOVERN 6.2

<!-- tl:item UR-0015 -->
**UR-0015 — GOVERN 6.2** — `user_requirement`, status `approved`

> Contingency processes are in place to handle failures or incidents in third-party data or AI systems deemed to be high-risk.

*Derives from:* INT-0001

**source_ref**: GOVERN 6.2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'GOVERN 6.2' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0052 | system_requirement | approved | NIST AI 600-1 GV-6.2-001 |
| SR-0053 | system_requirement | approved | NIST AI 600-1 GV-6.2-002 |
| SR-0054 | system_requirement | approved | NIST AI 600-1 GV-6.2-003 |
| SR-0055 | system_requirement | approved | NIST AI 600-1 GV-6.2-004 |
| SR-0056 | system_requirement | approved | NIST AI 600-1 GV-6.2-005 |
| SR-0057 | system_requirement | approved | NIST AI 600-1 GV-6.2-006 |
| SR-0058 | system_requirement | approved | NIST AI 600-1 GV-6.2-007 |
<!-- tl:end -->

# MAP — the root

<!-- tl:item INT-0002 -->
**INT-0002 — MAP — recognise context and identify GenAI risks** — `intent`, status `approved`

> The context is recognized and risks related to context are identified. The MAP function establishes the context to frame risks related to an AI system, and recognizes and enumerates the interdependencies and risks of AI system activities across the AI lifecycle.

**source_ref**: MAP
<!-- tl:end -->

## MAP 1.1

<!-- tl:item UR-0016 -->
**UR-0016 — MAP 1.1** — `user_requirement`, status `approved`

> Intended purposes, potentially beneficial uses, context specific laws, norms and expectations, and prospective settings in which the AI system will be deployed are understood and documented. Considerations include: the specific set or types of users along with their expectations; potential positive and negative impacts of system uses to individuals, communities, organizations, society, and the planet; assumptions and related limitations about AI system purposes, uses, and risks across the development or product AI lifecycle; and related TEVV and system metrics.

*Derives from:* INT-0002

**source_ref**: MAP 1.1
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'MAP 1.1' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0059 | system_requirement | approved | NIST AI 600-1 MP-1.1-001 |
| SR-0060 | system_requirement | approved | NIST AI 600-1 MP-1.1-002 |
| SR-0061 | system_requirement | approved | NIST AI 600-1 MP-1.1-003 |
| SR-0062 | system_requirement | approved | NIST AI 600-1 MP-1.1-004 |
<!-- tl:end -->

## MAP 1.2

<!-- tl:item UR-0017 -->
**UR-0017 — MAP 1.2** — `user_requirement`, status `approved`

> Interdisciplinary AI Actors, competencies, skills, and capacities for establishing context reflect demographic diversity and broad domain and user experience expertise, and their participation is documented. Opportunities for interdisciplinary collaboration are prioritized.

*Derives from:* INT-0002

**source_ref**: MAP 1.2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'MAP 1.2' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0063 | system_requirement | approved | NIST AI 600-1 MP-1.2-001 |
| SR-0064 | system_requirement | approved | NIST AI 600-1 MP-1.2-002 |
<!-- tl:end -->

## MAP 2.1

<!-- tl:item UR-0018 -->
**UR-0018 — MAP 2.1** — `user_requirement`, status `approved`

> The specific tasks and methods used to implement the tasks that the AI system will support are defined (e.g., classifiers, generative models, recommenders).

*Derives from:* INT-0002

**source_ref**: MAP 2.1
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'MAP 2.1' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0065 | system_requirement | approved | NIST AI 600-1 MP-2.1-001 |
| SR-0066 | system_requirement | approved | NIST AI 600-1 MP-2.1-002 |
<!-- tl:end -->

## MAP 2.2

<!-- tl:item UR-0019 -->
**UR-0019 — MAP 2.2** — `user_requirement`, status `approved`

> Information about the AI system's knowledge limits and how system output may be utilized and overseen by humans is documented. Documentation provides sufficient information to assist relevant AI Actors when making decisions and taking subsequent actions.

*Derives from:* INT-0002

**source_ref**: MAP 2.2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'MAP 2.2' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0067 | system_requirement | approved | NIST AI 600-1 MP-2.2-001 |
| SR-0068 | system_requirement | approved | NIST AI 600-1 MP-2.2-002 |
<!-- tl:end -->

## MAP 2.3

<!-- tl:item UR-0020 -->
**UR-0020 — MAP 2.3** — `user_requirement`, status `approved`

> Scientific integrity and TEVV considerations are identified and documented, including those related to experimental design, data collection and selection (e.g., availability, representativeness, suitability), system trustworthiness, and construct validation

*Derives from:* INT-0002

**source_ref**: MAP 2.3
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'MAP 2.3' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0069 | system_requirement | approved | NIST AI 600-1 MP-2.3-001 |
| SR-0070 | system_requirement | approved | NIST AI 600-1 MP-2.3-002 |
| SR-0071 | system_requirement | approved | NIST AI 600-1 MP-2.3-003 |
| SR-0072 | system_requirement | approved | NIST AI 600-1 MP-2.3-004 |
| SR-0073 | system_requirement | approved | NIST AI 600-1 MP-2.3-005 |
<!-- tl:end -->

## MAP 3.4

<!-- tl:item UR-0021 -->
**UR-0021 — MAP 3.4** — `user_requirement`, status `approved`

> Processes for operator and practitioner proficiency with AI system performance and trustworthiness - and relevant technical standards and certifications - are defined, assessed, and documented.

*Derives from:* INT-0002

**source_ref**: MAP 3.4
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'MAP 3.4' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0074 | system_requirement | approved | NIST AI 600-1 MP-3.4-001 |
| SR-0075 | system_requirement | approved | NIST AI 600-1 MP-3.4-002 |
| SR-0076 | system_requirement | approved | NIST AI 600-1 MP-3.4-003 |
| SR-0077 | system_requirement | approved | NIST AI 600-1 MP-3.4-004 |
| SR-0078 | system_requirement | approved | NIST AI 600-1 MP-3.4-005 |
| SR-0079 | system_requirement | approved | NIST AI 600-1 MP-3.4-006 |
<!-- tl:end -->

## MAP 4.1

<!-- tl:item UR-0022 -->
**UR-0022 — MAP 4.1** — `user_requirement`, status `approved`

> Approaches for mapping AI technology and legal risks of its components - including the use of third-party data or software - are in place, followed, and documented, as are risks of infringement of a third-party's intellectual property or other rights.

*Derives from:* INT-0002

**source_ref**: MAP 4.1
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'MAP 4.1' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0080 | system_requirement | approved | NIST AI 600-1 MP-4.1-001 |
| SR-0081 | system_requirement | approved | NIST AI 600-1 MP-4.1-002 |
| SR-0082 | system_requirement | approved | NIST AI 600-1 MP-4.1-003 |
| SR-0083 | system_requirement | approved | NIST AI 600-1 MP-4.1-004 |
| SR-0084 | system_requirement | approved | NIST AI 600-1 MP-4.1-005 |
| SR-0085 | system_requirement | approved | NIST AI 600-1 MP-4.1-006 |
| SR-0086 | system_requirement | approved | NIST AI 600-1 MP-4.1-007 |
| SR-0087 | system_requirement | approved | NIST AI 600-1 MP-4.1-008 |
| SR-0088 | system_requirement | approved | NIST AI 600-1 MP-4.1-009 |
| SR-0089 | system_requirement | approved | NIST AI 600-1 MP-4.1-010 |
<!-- tl:end -->

## MAP 5.1

<!-- tl:item UR-0023 -->
**UR-0023 — MAP 5.1** — `user_requirement`, status `approved`

> Likelihood and magnitude of each identified impact (both potentially beneficial and harmful) based on expected use, past uses of AI systems in similar contexts, public incident reports, feedback from those external to the team that developed or deployed the AI system, or other data are identified and documented.

*Derives from:* INT-0002

**source_ref**: MAP 5.1
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'MAP 5.1' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0090 | system_requirement | approved | NIST AI 600-1 MP-5.1-001 |
| SR-0091 | system_requirement | approved | NIST AI 600-1 MP-5.1-002 |
| SR-0092 | system_requirement | approved | NIST AI 600-1 MP-5.1-003 |
| SR-0093 | system_requirement | approved | NIST AI 600-1 MP-5.1-004 |
| SR-0094 | system_requirement | approved | NIST AI 600-1 MP-5.1-005 |
| SR-0095 | system_requirement | approved | NIST AI 600-1 MP-5.1-006 |
<!-- tl:end -->

## MAP 5.2

<!-- tl:item UR-0024 -->
**UR-0024 — MAP 5.2** — `user_requirement`, status `approved`

> Practices and personnel for supporting regular engagement with relevant AI Actors and integrating feedback about positive, negative, and unanticipated impacts are in place and documented.

*Derives from:* INT-0002

**source_ref**: MAP 5.2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'MAP 5.2' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0096 | system_requirement | approved | NIST AI 600-1 MP-5.2-001 |
| SR-0097 | system_requirement | approved | NIST AI 600-1 MP-5.2-002 |
<!-- tl:end -->

# MEASURE — the root

<!-- tl:item INT-0003 -->
**INT-0003 — MEASURE — assess, analyse and track GenAI risks** — `intent`, status `approved`

> Identified risks are assessed, analyzed, and tracked. The MEASURE function employs quantitative, qualitative, or mixed-method tools, techniques, and methodologies to analyze, assess, benchmark, and monitor AI risk and related impacts.

**source_ref**: MEASURE
<!-- tl:end -->

## MEASURE 1.1

<!-- tl:item UR-0025 -->
**UR-0025 — MEASURE 1.1** — `user_requirement`, status `approved`

> Approaches and metrics for measurement of AI risks enumerated during the MAP function are selected for implementation starting with the most significant AI risks. The risks or trustworthiness characteristics that will not - or cannot - be measured are properly documented.

*Derives from:* INT-0003

**source_ref**: MEASURE 1.1
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'MEASURE 1.1' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0098 | system_requirement | approved | NIST AI 600-1 MS-1.1-001 |
| SR-0099 | system_requirement | approved | NIST AI 600-1 MS-1.1-002 |
| SR-0100 | system_requirement | approved | NIST AI 600-1 MS-1.1-003 |
| SR-0101 | system_requirement | approved | NIST AI 600-1 MS-1.1-004 |
| SR-0102 | system_requirement | approved | NIST AI 600-1 MS-1.1-005 |
| SR-0103 | system_requirement | approved | NIST AI 600-1 MS-1.1-006 |
| SR-0104 | system_requirement | approved | NIST AI 600-1 MS-1.1-007 |
| SR-0105 | system_requirement | approved | NIST AI 600-1 MS-1.1-008 |
| SR-0106 | system_requirement | approved | NIST AI 600-1 MS-1.1-009 |
<!-- tl:end -->

## MEASURE 1.3

<!-- tl:item UR-0026 -->
**UR-0026 — MEASURE 1.3** — `user_requirement`, status `approved`

> Internal experts who did not serve as front-line developers for the system and/or independent assessors are involved in regular assessments and updates. Domain experts, users, AI Actors external to the team that developed or deployed the AI system, and affected communities are consulted in support of assessments as necessary per organizational risk tolerance.

*Derives from:* INT-0003

**source_ref**: MEASURE 1.3
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'MEASURE 1.3' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0107 | system_requirement | approved | NIST AI 600-1 MS-1.3-001 |
| SR-0108 | system_requirement | approved | NIST AI 600-1 MS-1.3-002 |
| SR-0109 | system_requirement | approved | NIST AI 600-1 MS-1.3-003 |
<!-- tl:end -->

## MEASURE 2.2

<!-- tl:item UR-0027 -->
**UR-0027 — MEASURE 2.2** — `user_requirement`, status `approved`

> Evaluations involving human subjects meet applicable requirements (including human subject protection) and are representative of the relevant population.

*Derives from:* INT-0003

**source_ref**: MEASURE 2.2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'MEASURE 2.2' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0110 | system_requirement | approved | NIST AI 600-1 MS-2.2-001 |
| SR-0111 | system_requirement | approved | NIST AI 600-1 MS-2.2-002 |
| SR-0112 | system_requirement | approved | NIST AI 600-1 MS-2.2-003 |
| SR-0113 | system_requirement | approved | NIST AI 600-1 MS-2.2-004 |
<!-- tl:end -->

## MEASURE 2.3

<!-- tl:item UR-0028 -->
**UR-0028 — MEASURE 2.3** — `user_requirement`, status `approved`

> AI system performance or assurance criteria are measured qualitatively or quantitatively and demonstrated for conditions similar to deployment setting(s). Measures are documented.

*Derives from:* INT-0003

**source_ref**: MEASURE 2.3
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'MEASURE 2.3' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0114 | system_requirement | approved | NIST AI 600-1 MS-2.3-001 |
| SR-0115 | system_requirement | approved | NIST AI 600-1 MS-2.3-002 |
| SR-0116 | system_requirement | approved | NIST AI 600-1 MS-2.3-003 |
| SR-0117 | system_requirement | approved | NIST AI 600-1 MS-2.3-004 |
<!-- tl:end -->

## MEASURE 2.5

<!-- tl:item UR-0029 -->
**UR-0029 — MEASURE 2.5** — `user_requirement`, status `approved`

> The AI system to be deployed is demonstrated to be valid and reliable. Limitations of the generalizability beyond the conditions under which the technology was developed are documented.

*Derives from:* INT-0003

**source_ref**: MEASURE 2.5
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'MEASURE 2.5' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0118 | system_requirement | approved | NIST AI 600-1 MS-2.5-001 |
| SR-0119 | system_requirement | approved | NIST AI 600-1 MS-2.5-002 |
| SR-0120 | system_requirement | approved | NIST AI 600-1 MS-2.5-003 |
| SR-0121 | system_requirement | approved | NIST AI 600-1 MS-2.5-004 |
| SR-0122 | system_requirement | approved | NIST AI 600-1 MS-2.5-005 |
| SR-0123 | system_requirement | approved | NIST AI 600-1 MS-2.5-006 |
<!-- tl:end -->

## MEASURE 2.6

<!-- tl:item UR-0030 -->
**UR-0030 — MEASURE 2.6** — `user_requirement`, status `approved`

> The AI system is evaluated regularly for safety risks - as identified in the MAP function. The AI system to be deployed is demonstrated to be safe, its residual negative risk does not exceed the risk tolerance, and it can fail safely, particularly if made to operate beyond its knowledge limits. Safety metrics reflect system reliability and robustness, real-time monitoring, and response times for AI system failures.

*Derives from:* INT-0003

**source_ref**: MEASURE 2.6
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'MEASURE 2.6' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0124 | system_requirement | approved | NIST AI 600-1 MS-2.6-001 |
| SR-0125 | system_requirement | approved | NIST AI 600-1 MS-2.6-002 |
| SR-0126 | system_requirement | approved | NIST AI 600-1 MS-2.6-003 |
| SR-0127 | system_requirement | approved | NIST AI 600-1 MS-2.6-004 |
| SR-0128 | system_requirement | approved | NIST AI 600-1 MS-2.6-005 |
| SR-0129 | system_requirement | approved | NIST AI 600-1 MS-2.6-006 |
| SR-0130 | system_requirement | approved | NIST AI 600-1 MS-2.6-007 |
<!-- tl:end -->

## MEASURE 2.7

<!-- tl:item UR-0031 -->
**UR-0031 — MEASURE 2.7** — `user_requirement`, status `approved`

> AI system security and resilience - as identified in the MAP function - are evaluated and documented.

*Derives from:* INT-0003

**source_ref**: MEASURE 2.7
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'MEASURE 2.7' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0131 | system_requirement | approved | NIST AI 600-1 MS-2.7-001 |
| SR-0132 | system_requirement | approved | NIST AI 600-1 MS-2.7-002 |
| SR-0133 | system_requirement | approved | NIST AI 600-1 MS-2.7-003 |
| SR-0134 | system_requirement | approved | NIST AI 600-1 MS-2.7-004 |
| SR-0135 | system_requirement | approved | NIST AI 600-1 MS-2.7-005 |
| SR-0136 | system_requirement | approved | NIST AI 600-1 MS-2.7-006 |
| SR-0137 | system_requirement | approved | NIST AI 600-1 MS-2.7-007 |
| SR-0138 | system_requirement | approved | NIST AI 600-1 MS-2.7-008 |
| SR-0139 | system_requirement | approved | NIST AI 600-1 MS-2.7-009 |
<!-- tl:end -->

## MEASURE 2.8

<!-- tl:item UR-0032 -->
**UR-0032 — MEASURE 2.8** — `user_requirement`, status `approved`

> Risks associated with transparency and accountability - as identified in the MAP function - are examined and documented.

*Derives from:* INT-0003

**source_ref**: MEASURE 2.8
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'MEASURE 2.8' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0140 | system_requirement | approved | NIST AI 600-1 MS-2.8-001 |
| SR-0141 | system_requirement | approved | NIST AI 600-1 MS-2.8-002 |
| SR-0142 | system_requirement | approved | NIST AI 600-1 MS-2.8-003 |
| SR-0143 | system_requirement | approved | NIST AI 600-1 MS-2.8-004 |
<!-- tl:end -->

## MEASURE 2.9

<!-- tl:item UR-0033 -->
**UR-0033 — MEASURE 2.9** — `user_requirement`, status `approved`

> The AI model is explained, validated, and documented, and AI system output is interpreted within its context - as identified in the MAP function - to inform responsible use and governance.

*Derives from:* INT-0003

**source_ref**: MEASURE 2.9
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'MEASURE 2.9' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0144 | system_requirement | approved | NIST AI 600-1 MS-2.9-001 |
| SR-0145 | system_requirement | approved | NIST AI 600-1 MS-2.9-002 |
<!-- tl:end -->

## MEASURE 2.10

<!-- tl:item UR-0034 -->
**UR-0034 — MEASURE 2.10** — `user_requirement`, status `approved`

> Privacy risk of the AI system - as identified in the MAP function - is examined and documented.

*Derives from:* INT-0003

**source_ref**: MEASURE 2.10
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'MEASURE 2.10' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0146 | system_requirement | approved | NIST AI 600-1 MS-2.10-001 |
| SR-0147 | system_requirement | approved | NIST AI 600-1 MS-2.10-002 |
| SR-0148 | system_requirement | approved | NIST AI 600-1 MS-2.10-003 |
<!-- tl:end -->

## MEASURE 2.11

<!-- tl:item UR-0035 -->
**UR-0035 — MEASURE 2.11** — `user_requirement`, status `approved`

> Fairness and bias - as identified in the MAP function - are evaluated and results are documented.

*Derives from:* INT-0003

**source_ref**: MEASURE 2.11
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'MEASURE 2.11' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0149 | system_requirement | approved | NIST AI 600-1 MS-2.11-001 |
| SR-0150 | system_requirement | approved | NIST AI 600-1 MS-2.11-002 |
| SR-0151 | system_requirement | approved | NIST AI 600-1 MS-2.11-003 |
| SR-0152 | system_requirement | approved | NIST AI 600-1 MS-2.11-004 |
| SR-0153 | system_requirement | approved | NIST AI 600-1 MS-2.11-005 |
<!-- tl:end -->

## MEASURE 2.12

<!-- tl:item UR-0036 -->
**UR-0036 — MEASURE 2.12** — `user_requirement`, status `approved`

> Environmental impact and sustainability of AI model training and management activities - as identified in the MAP function - are assessed and documented.

*Derives from:* INT-0003

**source_ref**: MEASURE 2.12
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'MEASURE 2.12' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0154 | system_requirement | approved | NIST AI 600-1 MS-2.12-001 |
| SR-0155 | system_requirement | approved | NIST AI 600-1 MS-2.12-002 |
| SR-0156 | system_requirement | approved | NIST AI 600-1 MS-2.12-003 |
| SR-0157 | system_requirement | approved | NIST AI 600-1 MS-2.12-004 |
<!-- tl:end -->

## MEASURE 2.13

<!-- tl:item UR-0037 -->
**UR-0037 — MEASURE 2.13** — `user_requirement`, status `approved`

> Effectiveness of the employed TEVV metrics and processes in the MEASURE function are evaluated and documented.

*Derives from:* INT-0003

**source_ref**: MEASURE 2.13
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'MEASURE 2.13' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0158 | system_requirement | approved | NIST AI 600-1 MS-2.13-001 |
<!-- tl:end -->

## MEASURE 3.2

<!-- tl:item UR-0038 -->
**UR-0038 — MEASURE 3.2** — `user_requirement`, status `approved`

> Risk tracking approaches are considered for settings where AI risks are difficult to assess using currently available measurement techniques or where metrics are not yet available.

*Derives from:* INT-0003

**source_ref**: MEASURE 3.2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'MEASURE 3.2' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0159 | system_requirement | approved | NIST AI 600-1 MS-3.2-001 |
<!-- tl:end -->

## MEASURE 3.3

<!-- tl:item UR-0039 -->
**UR-0039 — MEASURE 3.3** — `user_requirement`, status `approved`

> Feedback processes for end users and impacted communities to report problems and appeal system outcomes are established and integrated into AI system evaluation metrics.

*Derives from:* INT-0003

**source_ref**: MEASURE 3.3
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'MEASURE 3.3' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0160 | system_requirement | approved | NIST AI 600-1 MS-3.3-001 |
| SR-0161 | system_requirement | approved | NIST AI 600-1 MS-3.3-002 |
| SR-0162 | system_requirement | approved | NIST AI 600-1 MS-3.3-003 |
| SR-0163 | system_requirement | approved | NIST AI 600-1 MS-3.3-004 |
| SR-0164 | system_requirement | approved | NIST AI 600-1 MS-3.3-005 |
<!-- tl:end -->

## MEASURE 4.2

<!-- tl:item UR-0040 -->
**UR-0040 — MEASURE 4.2** — `user_requirement`, status `approved`

> Measurement results regarding AI system trustworthiness in deployment context(s) and across the AI lifecycle are informed by input from domain experts and relevant AI Actors to validate whether the system is performing consistently as intended. Results are documented.

*Derives from:* INT-0003

**source_ref**: MEASURE 4.2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'MEASURE 4.2' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0165 | system_requirement | approved | NIST AI 600-1 MS-4.2-001 |
| SR-0166 | system_requirement | approved | NIST AI 600-1 MS-4.2-002 |
| SR-0167 | system_requirement | approved | NIST AI 600-1 MS-4.2-003 |
| SR-0168 | system_requirement | approved | NIST AI 600-1 MS-4.2-004 |
| SR-0169 | system_requirement | approved | NIST AI 600-1 MS-4.2-005 |
<!-- tl:end -->

# MANAGE — the root

<!-- tl:item INT-0004 -->
**INT-0004 — MANAGE — prioritise and act on GenAI risks** — `intent`, status `approved`

> Risks are prioritized and acted upon based on a projected impact. The MANAGE function entails allocating risk resources to mapped and measured risks on a regular basis and as defined by the GOVERN function, so that AI risks are prioritized and acted upon based on a projected impact.

**source_ref**: MANAGE
<!-- tl:end -->

## MANAGE 1.3

<!-- tl:item UR-0041 -->
**UR-0041 — MANAGE 1.3** — `user_requirement`, status `approved`

> Responses to the AI risks deemed high priority, as identified by the MAP function, are developed, planned, and documented. Risk response options can include mitigating, transferring, avoiding, or accepting.

*Derives from:* INT-0004

**source_ref**: MANAGE 1.3
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'MANAGE 1.3' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0170 | system_requirement | approved | NIST AI 600-1 MG-1.3-001 |
| SR-0171 | system_requirement | approved | NIST AI 600-1 MG-1.3-002 |
<!-- tl:end -->

## MANAGE 2.2

<!-- tl:item UR-0042 -->
**UR-0042 — MANAGE 2.2** — `user_requirement`, status `approved`

> Mechanisms are in place and applied to sustain the value of deployed AI systems.

*Derives from:* INT-0004

**source_ref**: MANAGE 2.2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'MANAGE 2.2' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0172 | system_requirement | approved | NIST AI 600-1 MG-2.2-001 |
| SR-0173 | system_requirement | approved | NIST AI 600-1 MG-2.2-002 |
| SR-0174 | system_requirement | approved | NIST AI 600-1 MG-2.2-003 |
| SR-0175 | system_requirement | approved | NIST AI 600-1 MG-2.2-004 |
| SR-0176 | system_requirement | approved | NIST AI 600-1 MG-2.2-005 |
| SR-0177 | system_requirement | approved | NIST AI 600-1 MG-2.2-006 |
| SR-0178 | system_requirement | approved | NIST AI 600-1 MG-2.2-007 |
| SR-0179 | system_requirement | approved | NIST AI 600-1 MG-2.2-008 |
| SR-0180 | system_requirement | approved | NIST AI 600-1 MG-2.2-009 |
<!-- tl:end -->

## MANAGE 2.3

<!-- tl:item UR-0043 -->
**UR-0043 — MANAGE 2.3** — `user_requirement`, status `approved`

> Procedures are followed to respond to and recover from a previously unknown risk when it is identified.

*Derives from:* INT-0004

**source_ref**: MANAGE 2.3
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'MANAGE 2.3' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0181 | system_requirement | approved | NIST AI 600-1 MG-2.3-001 |
<!-- tl:end -->

## MANAGE 2.4

<!-- tl:item UR-0044 -->
**UR-0044 — MANAGE 2.4** — `user_requirement`, status `approved`

> Mechanisms are in place and applied, and responsibilities are assigned and understood, to supersede, disengage, or deactivate AI systems that demonstrate performance or outcomes inconsistent with intended use.

*Derives from:* INT-0004

**source_ref**: MANAGE 2.4
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'MANAGE 2.4' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0182 | system_requirement | approved | NIST AI 600-1 MG-2.4-001 |
| SR-0183 | system_requirement | approved | NIST AI 600-1 MG-2.4-002 |
| SR-0184 | system_requirement | approved | NIST AI 600-1 MG-2.4-003 |
| SR-0185 | system_requirement | approved | NIST AI 600-1 MG-2.4-004 |
<!-- tl:end -->

## MANAGE 3.1

<!-- tl:item UR-0045 -->
**UR-0045 — MANAGE 3.1** — `user_requirement`, status `approved`

> AI risks and benefits from third-party resources are regularly monitored, and risk controls are applied and documented.

*Derives from:* INT-0004

**source_ref**: MANAGE 3.1
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'MANAGE 3.1' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0186 | system_requirement | approved | NIST AI 600-1 MG-3.1-001 |
| SR-0187 | system_requirement | approved | NIST AI 600-1 MG-3.1-002 |
| SR-0188 | system_requirement | approved | NIST AI 600-1 MG-3.1-003 |
| SR-0189 | system_requirement | approved | NIST AI 600-1 MG-3.1-004 |
| SR-0190 | system_requirement | approved | NIST AI 600-1 MG-3.1-005 |
<!-- tl:end -->

## MANAGE 3.2

<!-- tl:item UR-0046 -->
**UR-0046 — MANAGE 3.2** — `user_requirement`, status `approved`

> Pre-trained models which are used for development are monitored as part of AI system regular monitoring and maintenance.

*Derives from:* INT-0004

**source_ref**: MANAGE 3.2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'MANAGE 3.2' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0191 | system_requirement | approved | NIST AI 600-1 MG-3.2-001 |
| SR-0192 | system_requirement | approved | NIST AI 600-1 MG-3.2-002 |
| SR-0193 | system_requirement | approved | NIST AI 600-1 MG-3.2-003 |
| SR-0194 | system_requirement | approved | NIST AI 600-1 MG-3.2-004 |
| SR-0195 | system_requirement | approved | NIST AI 600-1 MG-3.2-005 |
| SR-0196 | system_requirement | approved | NIST AI 600-1 MG-3.2-006 |
| SR-0197 | system_requirement | approved | NIST AI 600-1 MG-3.2-007 |
| SR-0198 | system_requirement | approved | NIST AI 600-1 MG-3.2-008 |
| SR-0199 | system_requirement | approved | NIST AI 600-1 MG-3.2-009 |
<!-- tl:end -->

## MANAGE 4.1

<!-- tl:item UR-0047 -->
**UR-0047 — MANAGE 4.1** — `user_requirement`, status `approved`

> Post-deployment AI system monitoring plans are implemented, including mechanisms for capturing and evaluating input from users and other relevant AI Actors, appeal and override, decommissioning, incident response, recovery, and change management.

*Derives from:* INT-0004

**source_ref**: MANAGE 4.1
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'MANAGE 4.1' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0200 | system_requirement | approved | NIST AI 600-1 MG-4.1-001 |
| SR-0201 | system_requirement | approved | NIST AI 600-1 MG-4.1-002 |
| SR-0202 | system_requirement | approved | NIST AI 600-1 MG-4.1-003 |
| SR-0203 | system_requirement | approved | NIST AI 600-1 MG-4.1-004 |
| SR-0204 | system_requirement | approved | NIST AI 600-1 MG-4.1-005 |
| SR-0205 | system_requirement | approved | NIST AI 600-1 MG-4.1-006 |
| SR-0206 | system_requirement | approved | NIST AI 600-1 MG-4.1-007 |
<!-- tl:end -->

## MANAGE 4.2

<!-- tl:item UR-0048 -->
**UR-0048 — MANAGE 4.2** — `user_requirement`, status `approved`

> Measurable activities for continual improvements are integrated into AI system updates and include regular engagement with interested parties, including relevant AI Actors.

*Derives from:* INT-0004

**source_ref**: MANAGE 4.2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'MANAGE 4.2' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0207 | system_requirement | approved | NIST AI 600-1 MG-4.2-001 |
| SR-0208 | system_requirement | approved | NIST AI 600-1 MG-4.2-002 |
| SR-0209 | system_requirement | approved | NIST AI 600-1 MG-4.2-003 |
<!-- tl:end -->

## MANAGE 4.3

<!-- tl:item UR-0049 -->
**UR-0049 — MANAGE 4.3** — `user_requirement`, status `approved`

> Incidents and errors are communicated to relevant AI Actors, including affected communities. Processes for tracking, responding to, and recovering from incidents and errors are followed and documented.

*Derives from:* INT-0004

**source_ref**: MANAGE 4.3
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('subcategory', '') == 'MANAGE 4.3' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0210 | system_requirement | approved | NIST AI 600-1 MG-4.3-001 |
| SR-0211 | system_requirement | approved | NIST AI 600-1 MG-4.3-002 |
| SR-0212 | system_requirement | approved | NIST AI 600-1 MG-4.3-003 |
<!-- tl:end -->

