"""Tests for Phoenix FirstBinding operator."""

import pytest
from code.phoenix.operators import FirstBinding


def test_first_binding_basic():
    """Test basic triadic binding."""
    op = FirstBinding()
    result = op.apply(a="fear", b="courage", stabilizer="service")
    
    assert result["tension_pair"] == ("fear", "courage")
    assert result["stabilizer"] == "service"
    assert result["triad"] == ("fear", "service", "courage")
    assert result["pattern"] == "triadic_formation"
    assert result["status"] == "bound"


def test_first_binding_different_values():
    """Test binding with different values."""
    op = FirstBinding()
    result = op.apply(a="isolation", b="connection", stabilizer="vulnerability")
    
    assert result["tension_pair"] == ("isolation", "connection")
    assert result["stabilizer"] == "vulnerability"
    assert result["triad"] == ("isolation", "vulnerability", "connection")


def test_first_binding_empty_a():
    """Test that empty first parameter raises ValueError."""
    op = FirstBinding()
    
    with pytest.raises(ValueError, match="All parameters"):
        op.apply(a="", b="courage", stabilizer="service")


def test_first_binding_empty_b():
    """Test that empty second parameter raises ValueError."""
    op = FirstBinding()
    
    with pytest.raises(ValueError, match="All parameters"):
        op.apply(a="fear", b="", stabilizer="service")


def test_first_binding_empty_stabilizer():
    """Test that empty stabilizer raises ValueError."""
    op = FirstBinding()
    
    with pytest.raises(ValueError, match="All parameters"):
        op.apply(a="fear", b="courage", stabilizer="")


def test_first_binding_all_empty():
    """Test that all empty parameters raise ValueError."""
    op = FirstBinding()
    
    with pytest.raises(ValueError, match="All parameters"):
        op.apply(a="", b="", stabilizer="")
