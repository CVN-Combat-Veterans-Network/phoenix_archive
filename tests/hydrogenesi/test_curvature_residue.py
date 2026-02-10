"""Tests for Hydrogenesi CurvatureResidue operator."""

import pytest
from code.hydrogenesi.operators import CurvatureResidue, OperatorStatus


def test_curvature_residue_basic():
    """Test basic curvature residue creation."""
    op = CurvatureResidue()
    result = op.apply("galaxy-prime")
    
    assert result["lineage_id"] == "galaxy-prime"
    assert result["status"] == OperatorStatus.COLLAPSED.value
    assert result["residue"] == "curvature-trace::galaxy-prime"
    assert result["pattern"] == "collapse_memory_trace"
    assert "metadata" not in result


def test_curvature_residue_with_metadata():
    """Test curvature residue with metadata."""
    op = CurvatureResidue()
    metadata = {"mass": 1000, "spin": "clockwise"}
    result = op.apply("star-alpha", metadata=metadata)
    
    assert result["lineage_id"] == "star-alpha"
    assert result["metadata"] == metadata
    assert result["residue"] == "curvature-trace::star-alpha"


def test_curvature_residue_empty_lineage():
    """Test that empty lineage ID raises ValueError."""
    op = CurvatureResidue()
    
    with pytest.raises(ValueError, match="Lineage ID cannot be empty"):
        op.apply("")


def test_curvature_residue_complex_lineage_id():
    """Test curvature residue with complex lineage ID."""
    op = CurvatureResidue()
    result = op.apply("galaxy-cluster::gen-5::branch-3")
    
    assert result["lineage_id"] == "galaxy-cluster::gen-5::branch-3"
    assert result["residue"] == "curvature-trace::galaxy-cluster::gen-5::branch-3"
