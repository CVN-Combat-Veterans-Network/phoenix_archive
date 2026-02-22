"""Tests for Hydrogenesi LineageLogic operator."""

import pytest
from code.hydrogenesi.operators import LineageLogic, OperatorStatus


def test_lineage_logic_basic():
    """Test basic lineage generation."""
    op = LineageLogic()
    result = op.apply("galaxy-prime", generations=4)
    
    assert result["root"] == "galaxy-prime"
    assert result["generations"] == 4
    assert result["depth"] == 4
    assert len(result["lineage_chain"]) == 4
    assert result["lineage_chain"][0] == "galaxy-prime::gen-0"
    assert result["lineage_chain"][3] == "galaxy-prime::gen-3"
    assert result["status"] == OperatorStatus.COMPLETED.value
    assert result["pattern"] == "root_recursion"


def test_lineage_logic_zero_generations():
    """Test lineage with zero generations."""
    op = LineageLogic()
    result = op.apply("root", generations=0)
    
    assert result["lineage_chain"] == []
    assert result["depth"] == 0
    assert result["root"] == "root"


def test_lineage_logic_empty_root():
    """Test that empty root raises ValueError."""
    op = LineageLogic()
    
    with pytest.raises(ValueError, match="Root identifier cannot be empty"):
        op.apply("", generations=3)


def test_lineage_logic_negative_generations():
    """Test that negative generations raises ValueError."""
    op = LineageLogic()
    
    with pytest.raises(ValueError, match="Generations must be non-negative"):
        op.apply("root", generations=-1)


def test_lineage_logic_single_generation():
    """Test lineage with single generation."""
    op = LineageLogic()
    result = op.apply("star-alpha", generations=1)
    
    assert result["depth"] == 1
    assert result["lineage_chain"] == ["star-alpha::gen-0"]
