"""
LNS_OP — Local Node Sovereignty Operator Protocol v2.1

The introspection system for operator lineage, recursion patterns,
and cross-scale coherence validation.
"""

from .operators import (
    LNS_OP,
    IntrospectionMode,
    OperatorFamily,
    AuditResult,
)

__all__ = [
    "LNS_OP",
    "IntrospectionMode",
    "OperatorFamily",
    "AuditResult",
]

__version__ = "2.1.0"
