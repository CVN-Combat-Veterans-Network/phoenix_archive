"""Tests for Phoenix IM_ME operator."""

import pytest
from code.phoenix.operators import IM_ME


def test_im_me_basic():
    """Test basic IM_ME recursion."""
    op = IM_ME()
    result = op.recurse("warrior")
    
    assert result["identity"] == "warrior"
    assert result["depth"] == 3
    assert len(result["sequence"]) == 6  # 3 levels * 2 (IM + ME)
    assert result["sequence"][0] == "IM(warrior)"
    assert result["sequence"][1] == "ME(warrior)"
    assert result["sequence"][4] == "IM(warrior)"
    assert result["sequence"][5] == "ME(warrior)"
    assert result["pattern"] == "observer_observed_recursion"
    assert result["status"] == "recursive"


def test_im_me_custom_depth():
    """Test IM_ME with custom depth."""
    op = IM_ME()
    result = op.recurse("sovereign", depth=5)
    
    assert result["depth"] == 5
    assert len(result["sequence"]) == 10  # 5 levels * 2
    assert result["sequence"][8] == "IM(sovereign)"
    assert result["sequence"][9] == "ME(sovereign)"


def test_im_me_depth_one():
    """Test IM_ME with minimum depth."""
    op = IM_ME()
    result = op.recurse("self", depth=1)
    
    assert result["depth"] == 1
    assert len(result["sequence"]) == 2
    assert result["sequence"] == ["IM(self)", "ME(self)"]


def test_im_me_empty_identity():
    """Test that empty identity raises ValueError."""
    op = IM_ME()
    
    with pytest.raises(ValueError, match="Identity cannot be empty"):
        op.recurse("")


def test_im_me_zero_depth():
    """Test that zero depth raises ValueError."""
    op = IM_ME()
    
    with pytest.raises(ValueError, match="Depth must be at least 1"):
        op.recurse("warrior", depth=0)


def test_im_me_negative_depth():
    """Test that negative depth raises ValueError."""
    op = IM_ME()
    
    with pytest.raises(ValueError, match="Depth must be at least 1"):
        op.recurse("warrior", depth=-1)
