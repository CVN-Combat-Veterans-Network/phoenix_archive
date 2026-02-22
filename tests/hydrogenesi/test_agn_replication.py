"""Tests for Hydrogenesi AGNReplication operator."""

import pytest
from code.hydrogenesi.operators import AGNReplication, OperatorStatus


def test_agn_replication_basic():
    """Test basic AGN replication."""
    op = AGNReplication()
    result = op.apply(100.0)
    
    assert result["original_mass"] == 100.0
    assert result["compressed_mass"] == 80.0
    assert result["offspring_count"] == 2
    assert len(result["offspring"]) == 2
    assert result["offspring"][0] == 40.0
    assert result["offspring"][1] == 40.0
    assert result["status"] == OperatorStatus.COMPLETED.value
    assert result["pattern"] == "compress_ignite_replicate"


def test_agn_replication_custom_factors():
    """Test AGN replication with custom factors."""
    op = AGNReplication(compression_factor=0.5, replication_factor=4)
    result = op.apply(200.0)
    
    assert result["original_mass"] == 200.0
    assert result["compressed_mass"] == 100.0
    assert result["offspring_count"] == 4
    assert len(result["offspring"]) == 4
    assert result["offspring"][0] == 25.0


def test_agn_replication_zero_mass():
    """Test that zero mass raises ValueError."""
    op = AGNReplication()
    
    with pytest.raises(ValueError, match="Mass must be positive"):
        op.apply(0.0)


def test_agn_replication_negative_mass():
    """Test that negative mass raises ValueError."""
    op = AGNReplication()
    
    with pytest.raises(ValueError, match="Mass must be positive"):
        op.apply(-50.0)
