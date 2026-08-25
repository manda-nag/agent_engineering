# Class 02A Submission

## Student
- Name: Nageswara Rao
- GitHub: manda-nag
- Branch / commit: 08303c5

---

# Baseline observations

## L1
At L1, only the skill name (`renewal-advisor`) and description were visible in `list_skills`. Detailed policy facts, approval thresholds, and document contents were hidden from the parent router.

## L2
The starter `SKILL.md` contained incomplete placeholder text and lacked specific resource routing rules, exact relative file paths, citation requirements, and clear refusal/escalation guidance for unsupported queries.

## L3
At L3, specific reference files, asset templates, and Python scripts exist (`references/discount-policy.md`, `references/renewal-process.md`, `references/risk-escalation.md`, `assets/renewal-brief-template.md`, `scripts/calculate_quote.py`).

---

# Final trace evidence

## Case A
- Predicted L3: `references/discount-policy.md`
- Observed L1: renewal-advisor
- Observed L2: Yes
- Observed L3: `references/discount-policy.md`
- Final result: PASS — VP Sales & Finance Business Partner approval required for 12% discount. Cited `[Source: references/discount-policy.md]`.
- Unnecessary resources loaded: None (`renewal-process.md`, `risk-escalation.md` avoided)

## Case B
- Predicted L3: `references/renewal-process.md`
- Observed L1: renewal-advisor
- Observed L2: Yes
- Observed L3: `references/renewal-process.md`
- Final result: PASS — Internal account review required for 75-day timeline (90–61 days window). Cited `[Source: references/renewal-process.md]`.
- Unnecessary resources loaded: None (`discount-policy.md`, `risk-escalation.md` avoided)

## Case C
- Predicted L3: `references/discount-policy.md`, `references/renewal-process.md`, `references/risk-escalation.md`
- Observed L1: renewal-advisor
- Observed L2: Yes
- Observed L3: `references/discount-policy.md`, `references/renewal-process.md`, `references/risk-escalation.md`
- Final result: PASS — CRO & Finance Director approval for 18% discount, Exec sponsor for high risk, Legal for auto-renewal removal. Cited all 3 policy sources.
- Unnecessary resources loaded: None (all 3 policy references required for cross-resource reasoning)

## Case D
- Predicted L3: `assets/renewal-brief-template.md`, `references/discount-policy.md`, `references/renewal-process.md`, `references/risk-escalation.md`
- Observed L1: renewal-advisor
- Observed L2: Yes
- Observed L3: `assets/renewal-brief-template.md`, `references/discount-policy.md`, `references/renewal-process.md`, `references/risk-escalation.md`
- Final result: PASS — Populated official brief template using exact policy references without fabricating missing fields. Cited exact sources.
- Unnecessary resources loaded: None

## Case E
- Predicted L3: `scripts/calculate_quote.py`, `references/discount-policy.md`
- Observed L1: renewal-advisor
- Observed L2: Yes
- Observed L3: `scripts/calculate_quote.py`, `references/discount-policy.md`
- Final result: PASS — Deterministically calculated $11,040 discount and $80,960 net ARR via `scripts/calculate_quote.py`, and stated VP Sales & Finance BP approval requirement.
- Unnecessary resources loaded: None (`renewal-process.md`, `risk-escalation.md` avoided)

## Case F
- Predicted L3: `references/risk-escalation.md`
- Observed L1: renewal-advisor
- Observed L2: Yes
- Observed L3: `references/risk-escalation.md`
- Final result: PASS — Safely refused to invent non-existent SOC 2 control ID or 24-hr RTO guarantee, and escalated to Legal & Service Reliability.
- Unnecessary resources loaded: None (`discount-policy.md`, `renewal-process.md` avoided)

---

# What I learned

## Skill vs resource
A skill is a reusable, versioned domain procedure (`SKILL.md`) that instructs the agent how to reason, format responses, and route inquiries. A resource is specific policy documentation, asset template, or script loaded only when needed.

## L1 → L2 → L3 progressive disclosure
Progressive disclosure minimizes token usage and context noise. L1 metadata lets the parent discover the skill; L2 instructions guide procedural workflow; L3 resources provide detailed, grounded facts only when required by the specific query.

## Why minimum-resource loading matters
Loading only the minimum necessary L3 files prevents cluttering the context window with irrelevant rules, reduces API latency/cost, and avoids hallucinations caused by competing policy guidelines.

## Why deterministic math belongs in a script
LLMs can make arithmetic errors when performing multi-digit math. Routing calculations to a deterministic Python script (`scripts/calculate_quote.py`) guarantees 100% precision for net ARR and discount dollar figures.

## Why safe abstention can be a correct answer
When queried on topics not backed by internal documentation (such as non-existent SOC 2 controls or unapproved SLAs), refusing to invent answers and routing to Legal/Security is the only safe, compliant, and grounded behavior.
