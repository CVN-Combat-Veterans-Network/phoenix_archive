"""Tests for Hydrogenesi operators."""
from __future__ import annotations
import pytest
from code.hydrogenesi.operators import (
    StabilizerExtraction,
    AGNReplication,
    CurvatureResidue,
    LineageLogic,
)


class TestStabilizerExtraction:
    """Test StabilizerExtraction operator."""

    def test_extraction_basic(self):
        """Test basic stabilizer extraction."""
        extractor = StabilizerExtraction()
        state = {
            "core": "neutron-stabilizer",
            "shell": "proton-electron-pair",
        }
        result = extractor.apply(state)
        
        assert result["pre_seed"] == "proton-electron-pair"
        assert result["core_void"] is None
        assert result["extracted_core"] == "neutron-stabilizer"

    def test_extraction_empty_state(self):
        """Test extraction with empty state."""
        extractor = StabilizerExtraction()
        result = extractor.apply({})
        
        assert result["pre_seed"] is None
        assert result["core_void"] is None
        assert result["extracted_core"] is None


class TestAGNReplication:
    """Test AGN Replication operator."""

    def test_replication_basic(self):
        """Test basic AGN replication."""
        agn = AGNReplication(compression_factor=0.8, replication_factor=2)
        offspring = agn.apply(mass=1000.0)
        
        assert len(offspring) == 2
        assert offspring == [400.0, 400.0]

    def test_replication_high_compression(self):
        """Test replication with high compression factor."""
        agn = AGNReplication(compression_factor=0.9, replication_factor=3)
        offspring = agn.apply(mass=1000.0)
        
        assert len(offspring) == 3
        assert offspring == [300.0, 300.0, 300.0]

    def test_replication_mass_conservation(self):
        """Test that total mass is conserved through compression."""
        agn = AGNReplication(compression_factor=0.8, replication_factor=4)
        input_mass = 2000.0
        offspring = agn.apply(mass=input_mass)
        
        total_offspring_mass = sum(offspring)
        compressed_mass = input_mass * 0.8
        assert abs(total_offspring_mass - compressed_mass) < 0.001


class TestCurvatureResidue:
    """Test Curvature Residue operator."""

    def test_residue_creation(self):
        """Test basic curvature residue creation."""
        residue = CurvatureResidue()
        result = residue.apply("galaxy-prime")
        
        assert result["lineage_id"] == "galaxy-prime"
        assert result["status"] == "collapsed"
        assert result["residue"] == "curvature-trace::galaxy-prime"

    def test_residue_different_lineages(self):
        """Test residue for different lineages."""
        residue = CurvatureResidue()
        
        result1 = residue.apply("star-alpha")
        result2 = residue.apply("cluster-beta")
        
        assert result1["residue"] != result2["residue"]
        assert "star-alpha" in result1["residue"]
        assert "cluster-beta" in result2["residue"]


class TestLineageLogic:
    """Test Lineage Logic operator."""

    def test_lineage_basic(self):
        """Test basic lineage generation."""
        logic = LineageLogic()
        lineage = logic.apply(root="root-galaxy", generations=4)
        
        assert len(lineage) == 4
        assert lineage[0] == "root-galaxy::gen-0"
        assert lineage[1] == "root-galaxy::gen-1"
        assert lineage[2] == "root-galaxy::gen-2"
        assert lineage[3] == "root-galaxy::gen-3"

    def test_lineage_single_generation(self):
        """Test lineage with single generation."""
        logic = LineageLogic()
        lineage = logic.apply(root="origin-star", generations=1)
        
        assert len(lineage) == 1
        assert lineage[0] == "origin-star::gen-0"

    def test_lineage_zero_generations(self):
        """Test lineage with zero generations."""
        logic = LineageLogic()
        lineage = logic.apply(root="test", generations=0)
        
        assert len(lineage) == 0

    def test_lineage_continuity(self):
        """Test that lineage maintains root reference."""
        logic = LineageLogic()
        root = "cosmic-root"
        lineage = logic.apply(root=root, generations=5)
        
        for gen in lineage:
            assert root in gen
            assert "::gen-" in gen
