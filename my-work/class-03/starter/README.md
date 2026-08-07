# Class 3 — WidgetWare SDR Context Package

This project implements the Class 3 WidgetWare SDR Context Package according to `SPEC.md`.

## Context Model

The package structures and isolates five context layers required for future agent decision-making:

1. **System Instructions** (`src/widgetware_sdr/instructions.py`): Stable rules defining role, fact provenance, safety limits, and prompt-injection defense.
2. **Business Context** (`config/*.yaml`): Product offerings (`products.yaml`), Ideal Customer Profile (`icp.yaml`), and governance policies (`policies.yaml`).
3. **Task Context**: Input payload containing target account data and research objective. Treated as untrusted input.
4. **Retrieved Evidence**: Provenance-tracked evidence records classified as `verified_fact`, `derived_fact`, `inference`, `unknown`, or `conflict`.
5. **Workflow State**: Execution/approval state layer.

## Setup & Verification

1. Install package in editable mode:
   ```bash
   pip3 install -e .
   ```

2. Run automated test suite:
   ```bash
   python3 -m pytest -v
   ```

## Scenario Fixtures

Representative test scenarios located under `tests/scenarios/`:
* `qualified_account.yaml`
* `unqualified_account.yaml`
* `insufficient_evidence.yaml`
* `prompt_injection.yaml`

## Boundaries & Constraints
* No LLM API calls or ADK agent runtime code.
* No live research, CRM access, or email/social message delivery.
