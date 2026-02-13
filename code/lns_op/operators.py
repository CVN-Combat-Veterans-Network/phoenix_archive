"""
LNS_OP Operators — Local Node Sovereignty Introspection System

Core operator introspection and audit functionality.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Any, Optional
from datetime import datetime, timezone


class IntrospectionMode(Enum):
    """Introspection modes for LNS_OP."""
    TRACE = "trace"
    MAP = "map"
    AUDIT = "audit"
    PROFILE = "profile"


class OperatorFamily(Enum):
    """Known operator families in the Phoenix Archive."""
    PHX = "PHX"  # Phoenix family
    HGN = "HGN"  # Hydrogenesis family
    LNS = "LNS"  # Local Node Sovereignty family
    UNI = "UNI"  # Universal/Cross-family operators
    SUB = "SUB"  # Substrate operators
    WALTZ = "WALTZ"  # Three-Finger Waltz meta-operators
    UNKNOWN = "UNKNOWN"  # Unknown operator


@dataclass
class InvocationTrace:
    """Single invocation trace entry."""
    timestamp: str
    operator: str
    depth: int
    mode: IntrospectionMode
    inputs: Dict[str, Any] = field(default_factory=dict)
    outputs: Dict[str, Any] = field(default_factory=dict)
    

@dataclass
class StateDelta:
    """State transition record."""
    before: Dict[str, Any]
    after: Dict[str, Any]
    operator: str
    delta_type: str = "operator_execution"


@dataclass
class IntegrityCheck:
    """Integrity validation result."""
    check_type: str
    passed: bool
    details: str
    severity: str = "info"


@dataclass
class Anomaly:
    """Anomaly detection result."""
    anomaly_type: str
    severity: str
    description: str
    operator: str
    depth: int


@dataclass
class AuditResult:
    """Complete audit result from LNS_OP introspection."""
    artifact_id: str
    op_family: str
    op_version: str
    audit_cycle: str
    invocation_trace: List[InvocationTrace] = field(default_factory=list)
    state_deltas: List[StateDelta] = field(default_factory=list)
    integrity_checks: List[IntegrityCheck] = field(default_factory=list)
    anomalies: List[Anomaly] = field(default_factory=list)
    signing_block: Dict[str, Any] = field(default_factory=dict)


# Known operator registry
OPERATOR_REGISTRY = {
    "PHX_OP_IGNITE": OperatorFamily.PHX,
    "SUB_OP_PRIME": OperatorFamily.SUB,
    "WALTZ_OP": OperatorFamily.WALTZ,
    "UNI_OP_BIFURCATE": OperatorFamily.UNI,
    "HYDROGENESIS": OperatorFamily.HGN,
    "LNS_OP": OperatorFamily.LNS,
}

# Recursion depth limits by operator family
RECURSION_LIMITS = {
    OperatorFamily.PHX: 3,
    OperatorFamily.HGN: 5,
    OperatorFamily.LNS: 10,
    OperatorFamily.UNI: 2,
    OperatorFamily.SUB: 4,
    OperatorFamily.WALTZ: 3,
    OperatorFamily.UNKNOWN: 1,
}


def LNS_OP(operator: str, depth: int, mode: IntrospectionMode | str) -> AuditResult:
    """
    LNS_OP — Local Node Sovereignty Operator Protocol
    
    Introspects operator invocations, validates recursion patterns,
    and generates audit artifacts for operator lineage tracking.
    
    Args:
        operator: Name of the operator to introspect
        depth: Recursion depth of the invocation
        mode: Introspection mode (trace, map, audit, profile)
    
    Returns:
        AuditResult containing introspection data
    """
    # Normalize mode
    if isinstance(mode, str):
        try:
            mode = IntrospectionMode(mode.lower())
        except ValueError:
            mode = IntrospectionMode.TRACE
    
    # Identify operator family
    op_family = OPERATOR_REGISTRY.get(operator, OperatorFamily.UNKNOWN)
    
    # Generate artifact ID
    timestamp = datetime.now(timezone.utc).isoformat()
    artifact_id = f"LNS_OP::{operator}::{depth}::{mode.value}::{timestamp}"
    
    # Create audit result
    audit = AuditResult(
        artifact_id=artifact_id,
        op_family=op_family.value,
        op_version="2.1.0",
        audit_cycle=timestamp,
    )
    
    # Record invocation trace
    trace = InvocationTrace(
        timestamp=timestamp,
        operator=operator,
        depth=depth,
        mode=mode,
        inputs={"operator": operator, "depth": depth, "mode": mode.value},
        outputs={"status": "introspected"}
    )
    audit.invocation_trace.append(trace)
    
    # Perform integrity checks
    checks = _perform_integrity_checks(operator, depth, mode, op_family)
    audit.integrity_checks.extend(checks)
    
    # Detect anomalies
    anomalies = _detect_anomalies(operator, depth, mode, op_family)
    audit.anomalies.extend(anomalies)
    
    # Record state deltas
    delta = StateDelta(
        before={"operator": None, "depth": None},
        after={"operator": operator, "depth": depth, "mode": mode.value},
        operator=operator,
    )
    audit.state_deltas.append(delta)
    
    # Generate signing block
    audit.signing_block = {
        "signature": f"LNS_OP_v2.1::{artifact_id}",
        "timestamp": timestamp,
        "protocol_version": "2.1.0",
        "ceremonial_seal": "🜂 LNS Sovereignty Confirmed",
    }
    
    return audit


def _perform_integrity_checks(
    operator: str, 
    depth: int, 
    mode: IntrospectionMode,
    op_family: OperatorFamily
) -> List[IntegrityCheck]:
    """Perform structural and semantic integrity checks."""
    checks = []
    
    # Check 1: Operator recognition
    if op_family == OperatorFamily.UNKNOWN:
        checks.append(IntegrityCheck(
            check_type="operator_recognition",
            passed=False,
            details=f"Operator '{operator}' not in registry",
            severity="warning"
        ))
    else:
        checks.append(IntegrityCheck(
            check_type="operator_recognition",
            passed=True,
            details=f"Operator '{operator}' recognized as {op_family.value}",
            severity="info"
        ))
    
    # Check 2: Recursion depth validation
    max_depth = RECURSION_LIMITS.get(op_family, 1)
    if depth > max_depth:
        checks.append(IntegrityCheck(
            check_type="recursion_safety",
            passed=False,
            details=f"Depth {depth} exceeds limit {max_depth} for {op_family.value}",
            severity="error"
        ))
    else:
        checks.append(IntegrityCheck(
            check_type="recursion_safety",
            passed=True,
            details=f"Depth {depth} within limit {max_depth} for {op_family.value}",
            severity="info"
        ))
    
    # Check 3: Mode validation
    checks.append(IntegrityCheck(
        check_type="mode_validation",
        passed=True,
        details=f"Mode '{mode.value}' is valid",
        severity="info"
    ))
    
    return checks


def _detect_anomalies(
    operator: str,
    depth: int,
    mode: IntrospectionMode,
    op_family: OperatorFamily
) -> List[Anomaly]:
    """Detect anomalies in operator invocation."""
    anomalies = []
    
    # Anomaly 1: Unknown operator
    if op_family == OperatorFamily.UNKNOWN:
        anomalies.append(Anomaly(
            anomaly_type="unknown_operator",
            severity="warning",
            description=f"Operator '{operator}' not registered in LNS_OP",
            operator=operator,
            depth=depth
        ))
    
    # Anomaly 2: Recursion depth exceeded
    max_depth = RECURSION_LIMITS.get(op_family, 1)
    if depth > max_depth:
        anomalies.append(Anomaly(
            anomaly_type="recursion_fracture",
            severity="error",
            description=f"Recursion depth {depth} exceeds safe limit {max_depth}",
            operator=operator,
            depth=depth
        ))
    
    # Anomaly 3: Depth 0 with audit mode (unusual pattern)
    if depth == 0 and mode == IntrospectionMode.AUDIT:
        anomalies.append(Anomaly(
            anomaly_type="unusual_pattern",
            severity="info",
            description="Audit mode at depth 0 is unusual but valid",
            operator=operator,
            depth=depth
        ))
    
    return anomalies
