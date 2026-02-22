"""Tests for Hydrogenesi StabilizerExtraction operator."""

import pytest
from code.hydrogenesi.operators import StabilizerExtraction, OperatorStatus


def test_stabilizer_extraction_basic():
    """Test basic stabilizer extraction."""
    op = StabilizerExtraction()
    state = {"core": "neutron", "shell": "proton-electron"}
    result = op.apply(state)
    
    assert result["pre_seed"] == "proton-electron"
    assert result["core_void"] is None
    assert result["extracted_core"] == "neutron"
    assert result["status"] == OperatorStatus.COMPLETED.value
    assert result["pattern"] == "core_extraction"


def test_stabilizer_extraction_missing_core():
    """Test that missing core raises ValueError."""
    op = StabilizerExtraction()
    state = {"shell": "proton-electron"}
    
    with pytest.raises(ValueError, match="State must contain 'core' and 'shell' keys"):
        op.apply(state)


def test_stabilizer_extraction_missing_shell():
    """Test that missing shell raises ValueError."""
    op = StabilizerExtraction()
    state = {"core": "neutron"}
    
    with pytest.raises(ValueError, match="State must contain 'core' and 'shell' keys"):
        op.apply(state)


def test_stabilizer_extraction_empty_dict():
    """Test that empty dict raises ValueError."""
    op = StabilizerExtraction()
    state = {}
    
    with pytest.raises(ValueError, match="State must contain 'core' and 'shell' keys"):
        op.apply(state)
