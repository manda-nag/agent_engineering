# Student Submission

Name: Nageswara Rao
Date: 2026-08-21
Commit hash: pending

## 1. Baseline observations

What was visible at L1?

> At L1, only the skill name (`renewal-advisor`) and its description were visible in the skill catalog (`list_skills`). Detailed policy facts, approval thresholds, and document contents were hidden.

What weaknesses did you observe before completing `SKILL.md`?

> The starter `SKILL.md` contained placeholder `TODO` text and lacked specific resource routing rules, exact relative file paths, citation requirements, and clear refusal/escalation guidance for unsupported queries.

## 2. Trace evidence

| Case | L1 observed | L2 loaded? | Exact L3 paths loaded | Irrelevant paths avoided | Result |
| --- | --- | --- | --- | --- | --- |
| A | renewal-advisor | Yes | `references/discount-policy.md` | `renewal-process.md`, `risk-escalation.md` | PASS — VP Sales & Finance Business Partner approval required |
| B | renewal-advisor | Yes | `references/renewal-process.md` | `discount-policy.md`, `risk-escalation.md` | PASS — Internal account review required (90–61 days timeline) |
| C | renewal-advisor | Yes | `references/discount-policy.md`, `references/renewal-process.md`, `references/risk-escalation.md` | None (all 3 policy references required for cross-resource reasoning) | PASS — CRO/Finance Dir (18% discount), Exec sponsor (high risk), Legal (auto-renewal) |
| D | renewal-advisor | Yes | `assets/renewal-brief-template.md`, `references/discount-policy.md`, `references/renewal-process.md`, `references/risk-escalation.md` | None | PASS — Populated official brief template without inventing missing fields |
| E | renewal-advisor | Yes | `scripts/calculate_quote.py`, `references/discount-policy.md` | `renewal-process.md`, `risk-escalation.md` | PASS — $11,040 discount, $80,960 net ARR via script, VP Sales & Finance BP approval |
| F | renewal-advisor | Yes | `references/risk-escalation.md` | `discount-policy.md`, `renewal-process.md` | PASS — Safely refused SOC 2 control ID/RTO claim and escalated to Legal/Service Reliability |

## 3. Evaluation scores

Score each item 0 or 1.

| Eval ID | Selection | Minimum resources | Correct facts | Citation | Safe handling | Total /5 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| L1-01 | 1 | 1 | 1 | 1 | 1 | 5/5 |
| L3-01 | 1 | 1 | 1 | 1 | 1 | 5/5 |
| L3-02 | 1 | 1 | 1 | 1 | 1 | 5/5 |
| L3-03 | 1 | 1 | 1 | 1 | 1 | 5/5 |
| L3-04 | 1 | 1 | 1 | 1 | 1 | 5/5 |
| SAFE-01 | 1 | 1 | 1 | 1 | 1 | 5/5 |

## 4. Reflection

### Why is policy detail stored at L3 instead of L1?

> Storing policy details at L3 prevents bloating the agent's baseline prompt/context window. L1 metadata is kept light so the router can discover skills quickly, while detailed policies are loaded progressively only when relevant.

### What is the difference between a skill and a tool in this lab?

> A **skill** is a reusable, versioned domain procedure or domain expertise (e.g., `renewal-advisor` instructing the agent *how* to evaluate renewals and *where* to route). A **tool** is a functional mechanism that performs specific actions, calculations, or resource retrieval (e.g., `load_skill_resource` or `calculate_quote.py`).

### Give one example where loading fewer resources improves the agent.

> In Case A (evaluating a 12% discount request), loading only `references/discount-policy.md` keeps the context focused, preventing risk policy noise or unrelated process rules from causing hallucination or slowing down response generation.

### What failure could occur if `SKILL.md` names resources vaguely instead of using exact paths?

> If `SKILL.md` uses vague names (e.g., "the policy file" instead of `references/discount-policy.md`), the agent may repeatedly guess file paths, fail to load the required resource via `load_skill_resource`, or load the wrong file entirely.

## 5. Test output

```text
.......                                                                  [100%]
7 passed in 0.09s
```
