"""Tests for Hydrogenesi operators."""
from __future__ import annotations
import pytest
import math
from code.hydrogenesi.operators import (
    StabilizerExtraction,
    AGNReplication,
    CurvatureResidue,
    LineageLogic,
    HarmonicRecursion,
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


class TestHarmonicRecursion:
    """Test Harmonic Recursion operator (v2.3)."""

    def test_harmonic_basic(self):
        """Test basic harmonic recursion."""
        harmonic = HarmonicRecursion(frequency=1.0, amplitude=1.0, damping=0.1)
        result = harmonic.apply(n=5, max_depth=10)
        
        assert result["generation"] == 5
        assert "normalized_depth" in result
        assert 0 <= result["normalized_depth"] <= 10
        assert result["pattern"] == "harmonic_recursion"
        assert result["recursion_mode"] == "harmonic"

    def test_harmonic_at_zero(self):
        """Test harmonic recursion at generation 0."""
        harmonic = HarmonicRecursion(frequency=1.0, amplitude=1.0, damping=0.1)
        result = harmonic.apply(n=0, max_depth=10)
        
        # sin(0) = 0, so depth should be near zero
        assert abs(result["raw_depth"]) < 0.001
        assert result["normalized_depth"] >= 0

    def test_harmonic_frequency_control(self):
        """Test frequency parameter control."""
        harmonic = HarmonicRecursion(frequency=1.0, amplitude=1.0, damping=0.1)
        
        # Test set_frequency
        harmonic.set_frequency(2.0)
        assert harmonic.frequency == 2.0
        
        # Test invalid frequency
        with pytest.raises(ValueError):
            harmonic.set_frequency(-1.0)
        
        with pytest.raises(ValueError):
            harmonic.set_frequency(0.0)

    def test_harmonic_amplitude_modulation(self):
        """Test amplitude parameter control."""
        harmonic = HarmonicRecursion(frequency=1.0, amplitude=1.0, damping=0.1)
        
        # Test set_amplitude
        harmonic.set_amplitude(2.0)
        assert harmonic.amplitude == 2.0
        
        # Test modulate_amplitude
        new_amp = harmonic.modulate_amplitude(1.5)
        assert new_amp == 3.0
        assert harmonic.amplitude == 3.0
        
        # Test invalid amplitude
        with pytest.raises(ValueError):
            harmonic.set_amplitude(-1.0)
        
        with pytest.raises(ValueError):
            harmonic.modulate_amplitude(0.0)

    def test_harmonic_damping_control(self):
        """Test damping parameter control."""
        harmonic = HarmonicRecursion(frequency=1.0, amplitude=1.0, damping=0.1)
        
        # Test set_damping
        harmonic.set_damping(0.2)
        assert harmonic.damping == 0.2
        
        # Test invalid damping (negative)
        with pytest.raises(ValueError):
            harmonic.set_damping(-0.1)
        
        # Zero damping should be valid
        harmonic.set_damping(0.0)
        assert harmonic.damping == 0.0

    def test_harmonic_damping_factor(self):
        """Test damping factor calculation."""
        harmonic = HarmonicRecursion(frequency=1.0, amplitude=1.0, damping=0.1)
        
        # At generation 0, damping factor should be 1.0
        factor_0 = harmonic.calculate_damping_factor(0)
        assert abs(factor_0 - 1.0) < 0.001
        
        # At later generations, should decay exponentially
        factor_10 = harmonic.calculate_damping_factor(10)
        expected = math.exp(-0.1 * 10)
        assert abs(factor_10 - expected) < 0.001
        assert factor_10 < factor_0

    def test_harmonic_frequency_characteristics(self):
        """Test frequency characteristics extraction."""
        harmonic = HarmonicRecursion(frequency=1.0, amplitude=1.0, damping=0.1)
        
        chars = harmonic.get_frequency_characteristics()
        assert "frequency" in chars
        assert "period" in chars
        assert "cycles_per_unit" in chars
        assert "category" in chars
        assert chars["frequency"] == 1.0

    def test_harmonic_amplitude_characteristics(self):
        """Test amplitude characteristics extraction."""
        harmonic = HarmonicRecursion(frequency=1.0, amplitude=2.0, damping=0.1)
        
        chars = harmonic.get_amplitude_characteristics()
        assert "amplitude" in chars
        assert "max_potential_depth" in chars
        assert "category" in chars
        assert "energy_level" in chars
        assert chars["amplitude"] == 2.0

    def test_harmonic_damping_characteristics(self):
        """Test damping characteristics extraction."""
        harmonic = HarmonicRecursion(frequency=1.0, amplitude=1.0, damping=0.1)
        
        chars = harmonic.get_damping_characteristics()
        assert "damping" in chars
        assert "half_life" in chars
        assert "decay_rate" in chars
        assert "category" in chars
        assert chars["damping"] == 0.1
        
        # Half-life should be ln(2)/damping
        expected_half_life = math.log(2) / 0.1
        assert abs(chars["half_life"] - expected_half_life) < 0.001

    def test_harmonic_energy_conservation(self):
        """Test that damping enforces energy conservation."""
        harmonic = HarmonicRecursion(frequency=1.0, amplitude=5.0, damping=0.2)
        
        # Get depths at increasing generations
        depths = []
        for n in range(0, 20, 2):
            result = harmonic.apply(n, max_depth=100)
            depths.append(abs(result["raw_depth"]))
        
        # Check that amplitude generally decreases due to damping
        # (accounting for oscillations, check trend)
        later_avg = sum(depths[-3:]) / 3
        earlier_avg = sum(depths[:3]) / 3
        assert later_avg < earlier_avg

    def test_harmonic_max_depth_clamping(self):
        """Test that normalized depth is clamped to max_depth."""
        # Use very high amplitude to test clamping
        harmonic = HarmonicRecursion(frequency=1.0, amplitude=100.0, damping=0.01)
        
        max_depth = 5
        result = harmonic.apply(n=2, max_depth=max_depth)
        
        # Normalized depth should never exceed max_depth
        assert result["normalized_depth"] <= max_depth
        assert result["normalized_depth"] >= 0

    def test_harmonic_invalid_generation(self):
        """Test that negative generation raises error."""
        harmonic = HarmonicRecursion(frequency=1.0, amplitude=1.0, damping=0.1)
        
        with pytest.raises(ValueError):
            harmonic.apply(n=-1, max_depth=10)

    def test_harmonic_invalid_max_depth(self):
        """Test that invalid max_depth raises error."""
        harmonic = HarmonicRecursion(frequency=1.0, amplitude=1.0, damping=0.1)
        
        with pytest.raises(ValueError):
            harmonic.apply(n=5, max_depth=0)
        
        with pytest.raises(ValueError):
            harmonic.apply(n=5, max_depth=-5)

