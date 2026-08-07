"""Context builder module for assembling the 5-layer SDR context package."""

import copy
from pathlib import Path
from typing import Any

import yaml

from widgetware_sdr.instructions import get_system_instructions


def _resolve_config_dir(config_dir: str | Path | None = None) -> Path:
    """Find the valid configuration directory containing YAML files."""
    if config_dir is not None:
        target = Path(config_dir)
        if target.exists() and target.is_dir():
            return target
        raise FileNotFoundError(f"Specified configuration directory does not exist: {config_dir}")

    # Search standard directory locations
    candidates = [
        Path.cwd() / "config",
        Path(__file__).resolve().parents[2] / "config",
        Path(__file__).resolve().parents[3] / "config",
    ]

    for candidate in candidates:
        if candidate.exists() and candidate.is_dir():
            if (
                (candidate / "products.yaml").exists()
                and (candidate / "icp.yaml").exists()
                and (candidate / "policies.yaml").exists()
            ):
                return candidate

    raise FileNotFoundError("Could not locate required 'config' directory with products.yaml, icp.yaml, and policies.yaml")


def _load_yaml(file_path: Path) -> dict[str, Any]:
    """Load a YAML configuration file safely."""
    if not file_path.exists():
        raise FileNotFoundError(f"Required configuration file missing: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        content = yaml.safe_load(f)
        return content if isinstance(content, dict) else {}


def build_context(
    account: dict[str, Any],
    objective: str,
    evidence: list[dict[str, Any]],
    state: dict[str, Any] | None = None,
    config_dir: str | Path | None = None,
) -> dict[str, Any]:
    """Build a structured 5-layer context package for SDR account qualification.

    Layers:
    1. system_instructions: Stable rules & governance.
    2. business_context: products, ICP, and policies loaded from YAML.
    3. task_context: account payload and analysis objective.
    4. retrieved_evidence: provenance-tracked evidence items.
    5. state: execution/workflow state dictionary (defaults to {} if omitted).
    """
    config_path = _resolve_config_dir(config_dir)

    products = _load_yaml(config_path / "products.yaml")
    icp = _load_yaml(config_path / "icp.yaml")
    policies = _load_yaml(config_path / "policies.yaml")

    return {
        "system_instructions": get_system_instructions(),
        "business_context": {
            "products": products,
            "icp": icp,
            "policies": policies,
        },
        "task_context": {
            "account": copy.deepcopy(account),
            "objective": objective,
        },
        "retrieved_evidence": copy.deepcopy(evidence),
        "state": copy.deepcopy(state) if state is not None else {},
    }
