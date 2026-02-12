"""
LNS_OP Test Suite — Comprehensive Introspection Testing

Tests all operator families, recursion patterns, and introspection modes.
"""

import pytest
from code.lns_op.operators import (
    LNS_OP,
    IntrospectionMode,
    OperatorFamily,
    AuditResult,
)


class TestLNSOperatorIntrospection:
    """Test suite for LNS_OP introspection system."""

    def test_phx_op_ignite_depth_0_trace(self):
        """Test PHX_OP_IGNITE at depth 0 with trace mode."""
        result = LNS_OP("PHX_OP_IGNITE", 0, IntrospectionMode.TRACE)
        
        assert isinstance(result, AuditResult)
        assert result.op_family == "PHX"
        assert result.op_version == "2.1.0"
        assert len(result.invocation_trace) == 1
        assert result.invocation_trace[0].operator == "PHX_OP_IGNITE"
        assert result.invocation_trace[0].depth == 0
        assert result.invocation_trace[0].mode == IntrospectionMode.TRACE
        
        # Should pass integrity checks
        recognition_check = next(
            (c for c in result.integrity_checks if c.check_type == "operator_recognition"),
            None
        )
        assert recognition_check is not None
        assert recognition_check.passed is True
        
        recursion_check = next(
            (c for c in result.integrity_checks if c.check_type == "recursion_safety"),
            None
        )
        assert recursion_check is not None
        assert recursion_check.passed is True

    def test_phx_op_ignite_depth_1_trace(self):
        """Test PHX_OP_IGNITE at depth 1 with trace mode."""
        result = LNS_OP("PHX_OP_IGNITE", 1, IntrospectionMode.TRACE)
        
        assert result.op_family == "PHX"
        assert result.invocation_trace[0].depth == 1
        assert len(result.integrity_checks) >= 2

    def test_sub_op_prime_depth_2_map(self):
        """Test SUB_OP_PRIME at depth 2 with map mode."""
        result = LNS_OP("SUB_OP_PRIME", 2, IntrospectionMode.MAP)
        
        assert result.op_family == "SUB"
        assert result.invocation_trace[0].operator == "SUB_OP_PRIME"
        assert result.invocation_trace[0].depth == 2
        assert result.invocation_trace[0].mode == IntrospectionMode.MAP

    def test_waltz_op_depth_3_audit(self):
        """Test WALTZ_OP at depth 3 with audit mode."""
        result = LNS_OP("WALTZ_OP", 3, IntrospectionMode.AUDIT)
        
        assert result.op_family == "WALTZ"
        assert result.invocation_trace[0].operator == "WALTZ_OP"
        assert result.invocation_trace[0].depth == 3
        assert result.invocation_trace[0].mode == IntrospectionMode.AUDIT
        
        # Depth 3 should be within WALTZ recursion limit
        recursion_check = next(
            (c for c in result.integrity_checks if c.check_type == "recursion_safety"),
            None
        )
        assert recursion_check is not None
        assert recursion_check.passed is True

    def test_uni_op_bifurcate_depth_1_trace(self):
        """Test UNI_OP_BIFURCATE at depth 1 with trace mode."""
        result = LNS_OP("UNI_OP_BIFURCATE", 1, IntrospectionMode.TRACE)
        
        assert result.op_family == "UNI"
        assert result.invocation_trace[0].operator == "UNI_OP_BIFURCATE"
        assert result.invocation_trace[0].depth == 1

    def test_phx_op_ignite_depth_1_profile(self):
        """Test PHX_OP_IGNITE at depth 1 with profile mode."""
        result = LNS_OP("PHX_OP_IGNITE", 1, IntrospectionMode.PROFILE)
        
        assert result.op_family == "PHX"
        assert result.invocation_trace[0].mode == IntrospectionMode.PROFILE

    def test_hydrogenesis_depth_2_map(self):
        """Test HYDROGENESIS operator at depth 2 with map mode."""
        result = LNS_OP("HYDROGENESIS", 2, IntrospectionMode.MAP)
        
        assert result.op_family == "HGN"
        assert result.invocation_trace[0].operator == "HYDROGENESIS"
        assert result.invocation_trace[0].depth == 2

    def test_unknown_operator_depth_1_trace(self):
        """Test UNKNOWN_OP at depth 1 with trace mode."""
        result = LNS_OP("UNKNOWN_OP", 1, IntrospectionMode.TRACE)
        
        assert result.op_family == "UNKNOWN"
        
        # Should fail operator recognition
        recognition_check = next(
            (c for c in result.integrity_checks if c.check_type == "operator_recognition"),
            None
        )
        assert recognition_check is not None
        assert recognition_check.passed is False
        
        # Should have unknown operator anomaly
        unknown_anomaly = next(
            (a for a in result.anomalies if a.anomaly_type == "unknown_operator"),
            None
        )
        assert unknown_anomaly is not None
        assert unknown_anomaly.severity == "warning"

    def test_phx_op_ignite_depth_4_trace_recursion_exceeded(self):
        """Test PHX_OP_IGNITE at depth 4 (exceeds limit) with trace mode."""
        result = LNS_OP("PHX_OP_IGNITE", 4, IntrospectionMode.TRACE)
        
        assert result.op_family == "PHX"
        
        # Should fail recursion safety check (PHX limit is 3)
        recursion_check = next(
            (c for c in result.integrity_checks if c.check_type == "recursion_safety"),
            None
        )
        assert recursion_check is not None
        assert recursion_check.passed is False
        
        # Should have recursion fracture anomaly
        fracture_anomaly = next(
            (a for a in result.anomalies if a.anomaly_type == "recursion_fracture"),
            None
        )
        assert fracture_anomaly is not None
        assert fracture_anomaly.severity == "error"

    def test_phx_op_ignite_depth_0_audit_unusual_pattern(self):
        """Test PHX_OP_IGNITE at depth 0 with audit mode (unusual pattern)."""
        result = LNS_OP("PHX_OP_IGNITE", 0, IntrospectionMode.AUDIT)
        
        assert result.op_family == "PHX"
        
        # Should have unusual pattern anomaly
        unusual_anomaly = next(
            (a for a in result.anomalies if a.anomaly_type == "unusual_pattern"),
            None
        )
        assert unusual_anomaly is not None
        assert unusual_anomaly.severity == "info"

    def test_lns_op_depth_3_audit(self):
        """Test LNS_OP operator introspecting itself at depth 3."""
        result = LNS_OP("LNS_OP", 3, IntrospectionMode.AUDIT)
        
        assert result.op_family == "LNS"
        assert result.invocation_trace[0].operator == "LNS_OP"
        
        # LNS has high recursion limit (10), so depth 3 should pass
        recursion_check = next(
            (c for c in result.integrity_checks if c.check_type == "recursion_safety"),
            None
        )
        assert recursion_check is not None
        assert recursion_check.passed is True


class TestAuditArtifactStructure:
    """Test audit artifact structure and completeness."""

    def test_audit_artifact_has_all_required_fields(self):
        """Verify audit artifact contains all required schema fields."""
        result = LNS_OP("PHX_OP_IGNITE", 1, IntrospectionMode.TRACE)
        
        # Required fields per schema
        assert hasattr(result, 'artifact_id')
        assert hasattr(result, 'op_family')
        assert hasattr(result, 'op_version')
        assert hasattr(result, 'audit_cycle')
        assert hasattr(result, 'invocation_trace')
        assert hasattr(result, 'state_deltas')
        assert hasattr(result, 'integrity_checks')
        assert hasattr(result, 'anomalies')
        assert hasattr(result, 'signing_block')
        
        # Verify types
        assert isinstance(result.artifact_id, str)
        assert isinstance(result.op_family, str)
        assert isinstance(result.op_version, str)
        assert isinstance(result.audit_cycle, str)
        assert isinstance(result.invocation_trace, list)
        assert isinstance(result.state_deltas, list)
        assert isinstance(result.integrity_checks, list)
        assert isinstance(result.anomalies, list)
        assert isinstance(result.signing_block, dict)

    def test_signing_block_structure(self):
        """Verify signing block has required components."""
        result = LNS_OP("WALTZ_OP", 2, IntrospectionMode.AUDIT)
        
        signing = result.signing_block
        assert 'signature' in signing
        assert 'timestamp' in signing
        assert 'protocol_version' in signing
        assert 'ceremonial_seal' in signing
        assert signing['protocol_version'] == "2.1.0"
        assert "🜂" in signing['ceremonial_seal']

    def test_state_delta_captured(self):
        """Verify state deltas are captured correctly."""
        result = LNS_OP("SUB_OP_PRIME", 1, IntrospectionMode.MAP)
        
        assert len(result.state_deltas) > 0
        delta = result.state_deltas[0]
        assert hasattr(delta, 'before')
        assert hasattr(delta, 'after')
        assert hasattr(delta, 'operator')
        assert delta.operator == "SUB_OP_PRIME"


class TestIntrospectionModes:
    """Test different introspection modes."""

    def test_trace_mode(self):
        """Test trace mode produces invocation traces."""
        result = LNS_OP("PHX_OP_IGNITE", 1, "trace")
        assert result.invocation_trace[0].mode == IntrospectionMode.TRACE

    def test_map_mode(self):
        """Test map mode."""
        result = LNS_OP("HYDROGENESIS", 2, "map")
        assert result.invocation_trace[0].mode == IntrospectionMode.MAP

    def test_audit_mode(self):
        """Test audit mode."""
        result = LNS_OP("WALTZ_OP", 3, "audit")
        assert result.invocation_trace[0].mode == IntrospectionMode.AUDIT

    def test_profile_mode(self):
        """Test profile mode."""
        result = LNS_OP("PHX_OP_IGNITE", 1, "profile")
        assert result.invocation_trace[0].mode == IntrospectionMode.PROFILE

    def test_string_mode_conversion(self):
        """Test that string modes are converted to IntrospectionMode enums."""
        result = LNS_OP("PHX_OP_IGNITE", 1, "trace")
        assert isinstance(result.invocation_trace[0].mode, IntrospectionMode)
        assert result.invocation_trace[0].mode == IntrospectionMode.TRACE


class TestRecursionLimits:
    """Test recursion depth validation across operator families."""

    def test_phx_recursion_limit(self):
        """PHX operators have recursion limit of 3."""
        # Within limit
        result = LNS_OP("PHX_OP_IGNITE", 3, IntrospectionMode.TRACE)
        recursion_check = next(
            c for c in result.integrity_checks if c.check_type == "recursion_safety"
        )
        assert recursion_check.passed is True
        
        # Exceeds limit
        result = LNS_OP("PHX_OP_IGNITE", 4, IntrospectionMode.TRACE)
        recursion_check = next(
            c for c in result.integrity_checks if c.check_type == "recursion_safety"
        )
        assert recursion_check.passed is False

    def test_hgn_recursion_limit(self):
        """HGN operators have recursion limit of 5."""
        result = LNS_OP("HYDROGENESIS", 5, IntrospectionMode.TRACE)
        recursion_check = next(
            c for c in result.integrity_checks if c.check_type == "recursion_safety"
        )
        assert recursion_check.passed is True

    def test_lns_recursion_limit(self):
        """LNS operators have recursion limit of 10."""
        result = LNS_OP("LNS_OP", 10, IntrospectionMode.TRACE)
        recursion_check = next(
            c for c in result.integrity_checks if c.check_type == "recursion_safety"
        )
        assert recursion_check.passed is True

    def test_unknown_recursion_limit(self):
        """Unknown operators have recursion limit of 1."""
        # Within limit
        result = LNS_OP("UNKNOWN_OP", 1, IntrospectionMode.TRACE)
        recursion_check = next(
            c for c in result.integrity_checks if c.check_type == "recursion_safety"
        )
        assert recursion_check.passed is True
        
        # Exceeds limit
        result = LNS_OP("UNKNOWN_OP", 2, IntrospectionMode.TRACE)
        recursion_check = next(
            c for c in result.integrity_checks if c.check_type == "recursion_safety"
        )
        assert recursion_check.passed is False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
