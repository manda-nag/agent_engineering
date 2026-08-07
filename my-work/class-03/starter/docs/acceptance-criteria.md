# Acceptance Criteria — Class 3 WidgetWare SDR Context Package

The Class 3 context package is accepted when all of the following criteria are met:

- [x] Configuration files (`products.yaml`, `icp.yaml`, `policies.yaml`) exist and load successfully.
- [x] At least two WidgetWare offerings are configured.
- [x] ICP specifies minimum size, target industries, preferred regions, and buying signals.
- [x] Operating policies define evidence classifications (`verified_fact`, `derived_fact`, `inference`, `unknown`, `conflict`).
- [x] Operating policies explicitly prohibit email sending, social messaging, CRM editing, and unauthorized customer claims.
- [x] System instructions are inspectable via `get_system_instructions()`.
- [x] `build_context()` returns five isolated context layers: `system_instructions`, `business_context`, `task_context`, `retrieved_evidence`, and `state`.
- [x] Evidence records preserve provenance (claim, classification, source name/URL, retrieval date).
- [x] Missing account fields remain unknown; missing evidence triggers `insufficient_evidence` behavior.
- [x] Prompt injection content in task data cannot override system instructions or policies.
- [x] Scenario test fixtures exist for qualified, unqualified, insufficient evidence, and prompt injection cases.
- [x] Automated test suite passes cleanly via `python3 -m pytest -v`.
- [x] No LLM call, ADK agent, live web search, CRM integration, or deployment code exists.
