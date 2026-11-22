# SPDX-License-Identifier: AGPL-3.0-or-later
# Commercial license available
# © Concepts 1996–2026 Miroslav Šotek. All rights reserved.
# © Code 2020–2026 Miroslav Šotek. All rights reserved.
# ORCID: 0009-0009-3560-0851
# Contact: www.anulum.li | protoscience@anulum.li
# CIRCUIT-MIXED-SIGNAL — selected documentation configuration
"""Select documentation policy and inspect fixed inputs without executing them."""

from __future__ import annotations

import hashlib
import os
import re
import stat
from dataclasses import dataclass
from pathlib import Path

MAX_BYTES = 2_097_152
SELECTED_INPUTS = {
    "mkdocs.yml": "d4bada8de092b1650f1aa26d4566b4bf7c6f6bb9c694de1910fac6e2fe1353d7",
    "tools/documentation_hooks.py": "f89b164f5941842b135201c2b2ac64fff8c410fd5987346af06aeec50d992543",
    "CITATION.cff": "a550e89e38197215f0f1e91b0e9a9eafad4636a0ff6ddb7150cd526801d8eee4",
    ".zenodo.json": "1bf8a0ec2961af085fde92ea78ccc4cd20951df2858d1aaeeb501f849e5940a2",
}
ROOT_DOCUMENTS = frozenset(
    {
        "ARCHITECTURE.md",
        "CHANGELOG.md",
        "CODE_OF_CONDUCT.md",
        "CONTRIBUTING.md",
        "CONTRIBUTORS.md",
        "GOVERNANCE.md",
        "NOTICE.md",
        "README.md",
        "ROADMAP.md",
        "SECURITY.md",
        "SUPPORT.md",
        "VALIDATION.md",
    }
)
RENDERED_ROOT_DOCUMENTS = frozenset(
    {
        "CODE_OF_CONDUCT.md",
        "CONTRIBUTING.md",
        "CONTRIBUTORS.md",
        "GOVERNANCE.md",
        "SECURITY.md",
        "SUPPORT.md",
        "VALIDATION.md",
    }
)
API_MODULES = frozenset(
    {
        "check_repository_metadata",
        "check_source_provenance",
        "bootstrap_native_tools",
        "check_dependency_alignment",
        "check_workflow_policy",
        "workflow_rules",
        "workflow_yaml",
        "check_documentation",
        "documentation_html",
        "documentation_policy",
        "documentation_hooks",
        "check_repository_inventory",
        "preflight",
        "preflight_checks",
        "repository_policy",
        "repository_tree",
        "repository_git",
    }
)
PRIVATE_PARTS = frozenset({"internal", ".coordination", "agentic-shared", "agentic_project_memory"})
FORBIDDEN_TEXT = re.compile(
    r"SPDX-License-Identifier:|© Concepts|© Code|docs/internal/|\.coordination/|"
    r"agentic-shared/|/home/anulum|/media/anulum|user/terminal-|"
    r"\b(?:codex|claude|openai|chatgpt|gemini)\b|\b(?:INFRA-|RWARCH-\d+\b)",
    re.IGNORECASE,
)
UNSUPPORTED_CLAIM = re.compile(
    r"10\.\d{4,9}/|doi\.org/|img\.shields\.io/|/releases/tag/|"
    r"pypi\.org/project/circuit[-_]mixed[-_]signal|"
    r"(?:pip3?|uv\s+pip)\s+install\s+circuit[-_]mixed[-_]signal|"
    r"circuit-mixed-signal\s+(?:cosimulate|calibrate|sequence|verify|run)\b",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class DocumentationIssue:
    """Locate a documentation refusal without including received contents.

    Parameters
    ----------
    path : str
        Repository-relative document/input, optionally with a link index.
    code : str
        Fixed diagnostic identifier.
    exit_code : int
        Refusal (2), unavailable input/output (3), or invalid invocation (4).
    """

    path: str
    code: str
    exit_code: int = 2


@dataclass(frozen=True)
class DocumentationReport:
    """Describe source/rendered-document inspection, never builder execution.

    Parameters
    ----------
    reasons : tuple of DocumentationIssue
        Complete deterministic diagnoses.
    configuration_only : bool
        Whether only selected configuration and publication metadata were inspected.
    """

    reasons: tuple[DocumentationIssue, ...]
    configuration_only: bool = False

    @property
    def exit_code(self) -> int:
        """Return configuration, availability, refusal, then success precedence."""
        return max((x.exit_code for x in self.reasons), default=0)

    def as_dict(self) -> dict[str, object]:
        """Return the named content scope and actual located diagnoses."""
        return {
            "gate": "documentation",
            "scope": (
                "selected_documentation_configuration"
                if self.configuration_only
                else "source_and_rendered_documentation"
            ),
            "builder_execution_attested": False,
            "status": {0: "pass", 2: "refused", 3: "unavailable", 4: "invalid"}[self.exit_code],
            "reasons": [{"path": x.path, "code": x.code} for x in self.reasons],
        }


def _linked(root: Path, path: Path) -> bool:
    while path != root:
        if path.is_symlink():
            return True
        path = path.parent
    return root.is_symlink()


def _read(root: Path, name: str) -> bytes | DocumentationIssue:
    path = root / name
    if _linked(root, path):
        return DocumentationIssue(name, "documentation_link_refused")
    try:
        if not stat.S_ISREG(path.stat().st_mode):
            return DocumentationIssue(name, "document_not_regular")
        with path.open("rb") as stream:
            data = stream.read(MAX_BYTES + 1)
    except OSError:
        return DocumentationIssue(name, "document_unavailable", 3)
    if len(data) > MAX_BYTES:
        return DocumentationIssue(name, "document_limit_exceeded")
    return data


def validate_documentation_configuration(root: Path) -> DocumentationReport:
    """Inspect selected renderer/publication bytes before any native build.

    Parameters
    ----------
    root : pathlib.Path
        Caller-selected checkout; no builder or documented module is invoked.

    Returns
    -------
    DocumentationReport
        Configuration-only outcome. Success never inspects or qualifies HTML.
    """
    try:
        if b"\0" in os.fsencode(root):
            raise ValueError("invalid root")
    except ValueError:
        return DocumentationReport((DocumentationIssue("invocation", "invalid_root", 4),), True)
    root = Path(os.path.abspath(root))
    reasons: list[DocumentationIssue] = []
    for name, digest in SELECTED_INPUTS.items():
        data = _read(root, name)
        if isinstance(data, DocumentationIssue):
            reasons.append(data)
        elif hashlib.sha256(data).hexdigest() != digest:
            reasons.append(DocumentationIssue(name, "documentation_configuration_not_selected"))
    return DocumentationReport(tuple(reasons), True)
