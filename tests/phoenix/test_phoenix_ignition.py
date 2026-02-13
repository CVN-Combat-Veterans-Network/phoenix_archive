"""Tests for Phoenix PhoenixIgnition operator."""

import pytest
from code.phoenix.operators import PhoenixIgnition


def test_phoenix_ignition_basic():
    """Test basic Phoenix Ignition."""
    op = PhoenixIgnition()
    result = op.ignite("false-identity")
    
    assert result["original"] == "false-identity"
    assert result["collapsed"] == "core::false-identity"
    assert result["risen"] == "apex::false-identity"
    assert result["pattern"] == "burn_collapse_rise"
    assert result["status"] == "ignited"


def test_phoenix_ignition_different_state():
    """Test ignition with different state."""
    op = PhoenixIgnition()
    result = op.ignite("wounded-self")
    
    assert result["original"] == "wounded-self"
    assert result["collapsed"] == "core::wounded-self"
    assert result["risen"] == "apex::wounded-self"


def test_phoenix_ignition_complex_state():
    """Test ignition with complex state name."""
    op = PhoenixIgnition()
    result = op.ignite("fragmented-warrior-identity")
    
    assert result["original"] == "fragmented-warrior-identity"
    assert result["collapsed"] == "core::fragmented-warrior-identity"
    assert result["risen"] == "apex::fragmented-warrior-identity"


def test_phoenix_ignition_empty_state():
    """Test that empty state raises ValueError."""
    op = PhoenixIgnition()
    
    with pytest.raises(ValueError, match="State cannot be empty"):
        op.ignite("")


def test_phoenix_ignition_transformation_chain():
    """Test that ignition creates proper transformation chain."""
    op = PhoenixIgnition()
    result = op.ignite("old-self")
    
    # Verify the transformation chain is logical
    assert "old-self" in result["collapsed"]
    assert "old-self" in result["risen"]
    assert result["collapsed"] != result["risen"]
    assert result["pattern"] == "burn_collapse_rise"
