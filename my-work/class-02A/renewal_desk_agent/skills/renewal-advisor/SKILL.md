---
name: renewal-advisor
description: Evaluates enterprise software renewal requests, discount approval routing, renewal timelines, commercial risk escalations, quote calculations, and renewal briefs. Trigger for renewal pricing, discount, escalation, or brief questions. Do not trigger for technical product troubleshooting.
---

# Renewal Advisor

This skill provides step-by-step guidance for Customer Success Managers evaluating renewal requests, routing discount approvals, assessing commercial risk, calculating quotes, and creating renewal briefs.

## When to use

Use this skill when responding to queries about:
- Enterprise contract renewal timeline and commercial steps.
- Approval routing for requested renewal discounts.
- Risk escalation for high-churn risk, regulated accounts, or non-standard terms.
- Generating renewal approval briefs using official templates.
- Calculating net ARR or dollar discount amounts using the quote calculator.

## When not to use

Do not use this skill for:
- Product technical troubleshooting or feature bugs.
- General legal inquiries unrelated to renewal contract terms.
- New customer prospect sales qualification.

## Required inputs

Identify the necessary inputs from the customer inquiry:
- Account name and regulated status.
- Current ARR and requested discount percentage.
- Renewal date or days remaining until expiration.
- Specific non-standard requests (e.g., auto-renewal removal, custom SLAs).
- If required inputs are missing, ask for clarification before proceeding.

## Procedure

1. Identify the core question type (discount approval, renewal process, risk escalation, brief creation, or calculation).
2. Load only the minimum necessary L3 resource needed for the specific request.
3. Apply the policy rules from the loaded L3 resource to formulate the recommendation.
4. For net ARR or dollar discount arithmetic, run the deterministic calculator script rather than doing manual math.
5. Cite every policy conclusion using the exact relative path, e.g., `[Source: references/discount-policy.md]`.
6. Distinguish clearly between requested, routed, and approved statuses.

## Resource routing map

Load only the specific L3 resource required for the inquiry:
- For discount percentage thresholds and approval authority levels: load `references/discount-policy.md`.
- For renewal timeline milestones, commercial steps, and auto-renewal rules: load `references/renewal-process.md`.
- For high-churn risk, regulated customer compliance, or SLA escalations: load `references/risk-escalation.md`.
- For formatting approval-ready renewal briefs: load `assets/renewal-brief-template.md`.
- For calculating net ARR and dollar discount amounts: run `scripts/calculate_quote.py`.

## Minimum resource rule

Load the minimum L3 resources required to answer the question. Do not load irrelevant references or assets.

## Output contract

Every response must:
- Cite all policy claims using exact file paths like `[Source: references/discount-policy.md]`.
- Use exact status labels: requested, routed, or approved.

## Unsupported and missing-source behavior

If a question asks for information not present in the supplied resources (e.g., SOC 2 control IDs, 24-hour RTO guarantees), explicitly state that the provided sources do not support the request and route to Legal and Service Reliability. Do not invent policies or approvals.

## Examples

### Positive

User: "The renewal ARR is $92,000 and requested discount is 12%. Which approval path is required?"
Action: Load `references/discount-policy.md`. State that VP Sales and Finance Business Partner approval is required. Cite `[Source: references/discount-policy.md]`.

### Negative

User: "How do I fix a bug in WidgetWare software?"
Action: State that this skill is for renewal desk advice, not product technical troubleshooting.

### Ambiguous

User: "We need a discount on our contract."
Action: State that the requested discount percentage is missing. Ask for the specific discount percentage and current ARR before determining the required approval level.
