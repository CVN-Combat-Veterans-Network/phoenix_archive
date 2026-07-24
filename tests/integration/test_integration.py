"""Tests for integration operators."""

import pytest
from code.integration.operators import (
    TransitionMap, Pillar, CompositionValidator, LawValidator,
    Operator, CompositionType
)


def test_phoenix_to_hydrogenesi_transition():
    """Test Phoenix → Hydrogenesi transition."""
    tm = TransitionMap()
    
    phoenix_pattern = {
        "a": "fear",
        "stabilizer": "service",
        "b": "courage",
        "stable": True
    }
    
    result = tm.transition(Pillar.PHOENIX, Pillar.HYDROGENESI, phoenix_pattern, depth=2)
    
    assert result["source"] == "Phoenix"
    assert result["target"] == "Hydrogenesi"
    assert "attractor" in result["result"]
    assert result["fidelity"] >= 0.95
    assert result["depth_out"] == 2


def test_hydrogenesi_to_third_transition():
    """Test Hydrogenesi → The Third transition."""
    tm = TransitionMap()
    
    field_pattern = {
        "attractor": "service",
        "tensions": ["fear", "courage"],
        "established": True
    }
    
    result = tm.transition(Pillar.HYDROGENESI, Pillar.THE_THIRD, field_pattern, depth=2)
    
    assert result["source"] == "Hydrogenesi"
    assert result["target"] == "The Third"
    assert "hold_target" in result["result"]


def test_third_to_phoenix_renewal():
    """Test The Third → Phoenix renewal (increases depth)."""
    tm = TransitionMap()
    
    hold_pattern = {
        "hold_target": "service",
        "avoid_patterns": ["fear", "avoidance"],
        "hold_duration": 3,
        "needs_refresh": True
    }
    
    result = tm.transition(Pillar.THE_THIRD, Pillar.PHOENIX, hold_pattern, depth=2)
    
    assert result["source"] == "The Third"
    assert result["target"] == "Phoenix"
    assert result["depth_out"] == 3  # Depth increased!


def test_sequential_composition():
    """Test sequential operator composition."""
    validator = CompositionValidator()
    
    op1 = Operator("First Binding", "Phoenix", "tension_pair", "triad", 0, 1)
    op2 = Operator("Three-Finger Waltz", "Phoenix", "triad", "rhythm", 1, 1)
    
    result = validator.compose([op1, op2], CompositionType.SEQUENTIAL)
    
    assert result["type"] == "sequential"
    assert result["valid"] is True
    assert "∘" in result["composition"]


def test_triadic_composition():
    """Test triadic operator composition."""
    validator = CompositionValidator()
    
    op1 = Operator("Phoenix Op", "Phoenix", "any", "any", 0, 1)
    op2 = Operator("Hydrogenesi Op", "Hydrogenesi", "any", "any", 1, 1)
    op3 = Operator("Third Op", "The Third", "any", "any", 1, 1)
    
    result = validator.compose([op1, op2, op3], CompositionType.TRIADIC)
    
    assert result["type"] == "triadic"
    assert result["valid"] is True
    assert "⟨" in result["composition"]


def test_law_validation():
    """Test Universal Law validation."""
    validator = LawValidator()
    
    operation = {
        "name": "Test Op",
        "a": "tension1",
        "b": "tension2",
        "stabilizer": "stabilizer_s",
        "depth_in": 2,
        "depth_out": 3
    }
    
    result = validator.validate_all_laws(operation)
    
    assert result["operation"] == "Test Op"
    assert result["validation_passed"] is True
    assert len(result["violations"]) == 0


def test_depth_reversal_violation():
    """Test that depth reversal is caught."""
    validator = CompositionValidator()
    
    op1 = Operator("High Depth Op", "Phoenix", "any", "any", 3, 3)
    op2 = Operator("Low Depth Op", "Phoenix", "any", "any", 1, 1)
    
    result = validator.compose([op1, op2], CompositionType.SEQUENTIAL)
    
    assert "error" in result
    assert "violations" in result


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
