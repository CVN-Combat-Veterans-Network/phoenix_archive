"""
Integration Test Suite — Codex v2.0.0

Comprehensive pytest-based testing framework for Phoenix Archive integration.

Test Coverage:
- Phoenix operator tests (6 tests)
- Hydrogenesi operator tests (3 tests)
- The Third operator tests (4 tests)
- Universal operator tests (1 test)
- Cross-pillar integration tests (3 tests)
- Universal Laws compliance tests (7 tests)
- Meta-operator tests (2 tests)
- Composition pattern tests (3 tests)

Total: 29+ test cases covering all three pillars

Usage:
    pytest tests/test_integration.py -v
    pytest tests/test_integration.py::TestPhoenixOperators -v
    pytest tests/test_integration.py -k "cross_pillar" -v
"""

import pytest
from typing import Tuple


# ============================================================================
# PHOENIX OPERATOR TESTS (6 tests)
# ============================================================================

class TestPhoenixOperators:
    """Test Phoenix pillar operators."""
    
    def test_first_binding_creates_triad(self):
        """Test First Binding creates proper triadic structure."""
        from code.phoenix.operators import FirstBinding
        
        op = FirstBinding()
        result = op.apply(a="tension_a", b="tension_b", stabilizer="binding_s")
        
        assert "triad" in result
        assert "tension_pair" in result
        assert "stabilizer" in result
        assert result["triad"] == ("tension_a", "binding_s", "tension_b")
        assert result["tension_pair"] == ("tension_a", "tension_b")
        assert result["stabilizer"] == "binding_s"
    
    def test_phoenix_ignition_collapse_and_rise(self):
        """Test Phoenix Ignition collapse and regeneration."""
        from code.phoenix.operators import PhoenixIgnition
        
        op = PhoenixIgnition()
        result = op.ignite(state="identity_state")
        
        assert "collapsed" in result
        assert "risen" in result
        assert "core::" in result["collapsed"]
        assert "apex::" in result["risen"]
    
    def test_im_me_recursion_sequence(self):
        """Test IM_ME identity recursion operator."""
        from code.phoenix.operators import IM_ME
        
        op = IM_ME()
        result = op.recurse(identity="test_identity", depth=3)
        
        assert len(result) == 6  # depth=3 means 3 IM + 3 ME = 6 total
        assert result[0] == "IM(test_identity)"
        assert result[1] == "ME(test_identity)"
    
    def test_apex_formation_from_triads(self):
        """Test Apex Formation creates sovereign structure."""
        from code.phoenix.operators import ApexFormation
        
        op = ApexFormation()
        triads = [
            ("a1", "s1", "b1"),
            ("a2", "s2", "b2"),
            ("a3", "s3", "b3"),
        ]
        result = op.apply(triads=triads)
        
        assert result["apex_formed"] is True
        assert result["sovereignty"] == "stable"
        assert len(result["foundation"]) == 3
        assert result["apex_symbol"] == "△"
    
    def test_three_finger_waltz_rhythm(self):
        """Test Three-Finger Waltz generates rhythm pattern."""
        from code.phoenix.operators import ThreeFingerWaltz
        
        op = ThreeFingerWaltz()
        triad = ("pulse", "pause", "pulse")
        result = op.apply(triad=triad, cycles=2)
        
        assert result["pattern"] == "●—○—●"
        assert result["rhythm"] == "pulse-pause-pulse"
        assert result["cycles"] == 2
        assert result["total_beats"] == 6  # 3 beats * 2 cycles
    
    def test_black_holed_imprint_creation(self):
        """Test Black-Holed Imprint records collapse."""
        from code.phoenix.operators import BlackHoledImprint
        
        op = BlackHoledImprint()
        result = op.apply(
            identity_collapse="trauma_event",
            context="childhood"
        )
        
        assert "imprint_id" in result
        assert "black-hole::" in result["imprint_id"]
        assert result["status"] == "collapsed"
        assert result["integration_required"] is True


# ============================================================================
# HYDROGENESI OPERATOR TESTS (3 tests)
# ============================================================================

class TestHydrogенesiOperators:
    """Test Hydrogenesi pillar operators."""
    
    def test_stabilizer_extraction_removes_core(self):
        """Test Stabilizer Extraction creates pre-seed state."""
        from code.hydrogenesi.operators import StabilizerExtraction
        
        op = StabilizerExtraction()
        result = op.apply({
            "core": "nucleus",
            "shell": "outer_layer"
        })
        
        assert result["pre_seed"] == "outer_layer"
        assert result["extracted_core"] == "nucleus"
        assert result["core_void"] is None
        assert result["status"] == "completed"
    
    def test_agn_replication_creates_offspring(self):
        """Test AGN Replication generates cosmic structures."""
        from code.hydrogenesi.operators import AGNReplication
        
        op = AGNReplication(compression_factor=0.8, replication_factor=3)
        result = op.apply(mass=100.0)
        
        assert result["original_mass"] == 100.0
        assert result["compressed_mass"] == 80.0
        assert result["offspring_count"] == 3
        assert len(result["offspring"]) == 3
        assert result["pattern"] == "compress_ignite_replicate"
    
    def test_lineage_logic_generates_chain(self):
        """Test Lineage Logic creates recursive lineage."""
        from code.hydrogenesi.operators import LineageLogic
        
        op = LineageLogic()
        result = op.apply(root="ROOT_SEED", generations=5)
        
        assert result["root"] == "ROOT_SEED"
        assert result["generations"] == 5
        assert result["depth"] == 5
        assert len(result["lineage_chain"]) == 5
        assert result["lineage_chain"][0] == "ROOT_SEED::gen-0"
        assert result["lineage_chain"][4] == "ROOT_SEED::gen-4"


# ============================================================================
# THE THIRD OPERATOR TESTS (4 tests)
# ============================================================================

class TestTheThirdOperators:
    """Test The Third pillar operators."""
    
    def test_meta_binder_binds_operators(self):
        """Test MetaBinder creates meta-binding structure."""
        from code.the_third.operators import MetaBinder
        
        op = MetaBinder()
        result = op.bind(
            operator_a="FirstBinding",
            operator_b="AGNReplication",
            binding_law="Binding"
        )
        
        assert result["bound_pair"] == ("FirstBinding", "AGNReplication")
        assert result["binding_law"] == "Binding"
        assert result["coherence"] == "aligned"
        assert "META" in result["meta_structure"]
    
    def test_meta_binder_triadic_binding(self):
        """Test MetaBinder creates triadic knot."""
        from code.the_third.operators import MetaBinder
        
        op = MetaBinder()
        result = op.bind_triad(
            operator_a="Phoenix",
            operator_b="Hydrogenesi",
            operator_c="TheThird"
        )
        
        assert result["triad"] == ("Phoenix", "Hydrogenesi", "TheThird")
        assert result["structure"] == "triadic"
        assert result["meta_coherence"] == "stable"
        assert len(result["binding_laws"]) == 3
    
    def test_law_compliance_validation(self):
        """Test Law Compliance validates operator behavior."""
        from code.the_third.operators import LawCompliance
        
        op = LawCompliance()
        result = op.validate(
            operator="TestOperator",
            behavior={
                "inputs": ["input1", "input2"],
                "stabilizer": "binding_element",
                "output": "result"
            }
        )
        
        assert result["operator"] == "TestOperator"
        assert "compliance" in result
        assert result["overall_status"] in ["compliant", "non-compliant"]
        assert "Tension" in result["compliance"]
        assert "Binding" in result["compliance"]
        assert "Apex" in result["compliance"]
    
    def test_coherence_validator_cross_family(self):
        """Test CoherenceValidator validates cross-family coherence."""
        from code.the_third.operators import CoherenceValidator
        
        op = CoherenceValidator()
        result = op.validate_cross_family(
            phx_ops=["FirstBinding", "PhoenixIgnition"],
            hgn_ops=["AGNReplication", "LineageLogic"],
            lns_ops=["MetaBinder"]
        )
        
        assert result["all_families_present"] is True
        assert result["total_operators"] == 5
        assert result["triadic_completion"] is True
        assert result["cross_family_coherence"] in ["aligned", "partial"]


# ============================================================================
# UNIVERSAL OPERATOR TESTS (1 test)
# ============================================================================

class TestUniversalOperators:
    """Test Universal operators."""
    
    def test_life_light_bifurcation_threshold(self):
        """Test Life-Light Bifurcation operator."""
        from code.universal.operators import LifeLightBifurcation, BifurcationVector
        
        # Test at threshold with high pressure (LIFE vector)
        op_life = LifeLightBifurcation(
            confinement_tension=1.0,
            stabilizing_symmetry=1.0,
            internal_pressure=0.85
        )
        assert op_life.at_threshold() is True
        
        result_life = op_life.bifurcate()
        assert result_life["vector"] == "LIFE"
        assert result_life["status"] == "LIFE"
        
        # Test at threshold with low pressure (LIGHT vector)
        op_light = LifeLightBifurcation(
            confinement_tension=1.0,
            stabilizing_symmetry=1.0,
            internal_pressure=0.5
        )
        result_light = op_light.bifurcate()
        assert result_light["vector"] == "LIGHT"
        assert result_light["status"] == "LIGHT"


# ============================================================================
# CROSS-PILLAR INTEGRATION TESTS (3 tests)
# ============================================================================

class TestCrossPillarIntegration:
    """Test cross-pillar integration patterns."""
    
    def test_phoenix_to_hydrogenesi_transition(self):
        """Test Example 1: Phoenix → Hydrogenesi transition."""
        from code.phoenix.operators import FirstBinding, PhoenixIgnition
        from code.hydrogenesi.operators import StabilizerExtraction
        
        # Phoenix: Create identity
        binding = FirstBinding()
        identity = binding.apply(a="chaos", b="order", stabilizer="balance")
        assert identity["triad"] == ("chaos", "balance", "order")
        
        # Phoenix: Ignite
        ignition = PhoenixIgnition()
        collapsed = ignition.ignite(state=str(identity["triad"]))
        assert "collapsed" in collapsed
        
        # Hydrogenesi: Extract stabilizer
        extraction = StabilizerExtraction()
        seed = extraction.apply({
            "core": identity["stabilizer"],
            "shell": identity["tension_pair"]
        })
        assert seed["extracted_core"] == "balance"
    
    def test_complete_three_pillar_cycle(self):
        """Test Example 3: Complete BEGIN → EXTEND → HOLD cycle."""
        from code.phoenix.operators import FirstBinding
        from code.hydrogenesi.operators import AGNReplication
        from code.the_third.operators import MetaBinder
        
        # BEGIN: Phoenix generates
        binding = FirstBinding()
        triad = binding.apply(a="start", b="end", stabilizer="middle")
        assert triad["triad"][1] == "middle"
        
        # EXTEND: Hydrogenesi propagates
        replicator = AGNReplication(replication_factor=2)
        propagated = replicator.apply(mass=100.0)
        assert propagated["offspring_count"] == 2
        
        # HOLD: The Third binds
        binder = MetaBinder()
        meta = binder.bind("FirstBinding", "AGNReplication", "Apex")
        assert meta["coherence"] == "aligned"
    
    def test_recursive_stability_with_apex(self):
        """Test Example 5: Recursive stability with apex formation."""
        from code.phoenix.operators import IM_ME, ApexFormation
        from code.hydrogenesi.operators import LineageLogic
        
        # Phoenix: Generate recursion
        im_me = IM_ME()
        recursion = im_me.recurse(identity="core", depth=3)
        assert len(recursion) == 6
        
        # Hydrogenesi: Map to lineage
        lineage = LineageLogic()
        cosmic = lineage.apply(root="APEX", generations=3)
        assert cosmic["depth"] == 3
        
        # Phoenix: Form apex
        apex_builder = ApexFormation()
        layers = [
            ("IM", "recursion", "ME"),
            ("depth-0", "progression", "depth-3"),
            ("micro", "scale", "macro")
        ]
        apex = apex_builder.apply(triads=layers)
        assert apex["apex_formed"] is True
        assert apex["sovereignty"] == "stable"


# ============================================================================
# UNIVERSAL LAWS COMPLIANCE TESTS (7 tests)
# ============================================================================

class TestUniversalLawsCompliance:
    """Test compliance with Twelve Universal Laws."""
    
    def test_law_1_tension_requires_two_forces(self):
        """Test Law 1: Tension requires binary pair."""
        from code.phoenix.operators import FirstBinding
        
        op = FirstBinding()
        result = op.apply(a="force_a", b="force_b", stabilizer="s")
        
        # Tension pair must exist
        assert "tension_pair" in result
        assert len(result["tension_pair"]) == 2
    
    def test_law_2_binding_requires_third_element(self):
        """Test Law 2: Binding requires third stabilizer."""
        from code.phoenix.operators import FirstBinding
        
        op = FirstBinding()
        result = op.apply(a="a", b="b", stabilizer="third")
        
        # Third element stabilizes
        assert result["stabilizer"] == "third"
        assert result["triad"][1] == "third"  # Middle position
    
    def test_law_3_apex_forms_sovereign_structure(self):
        """Test Law 3: Apex creates sovereign structure."""
        from code.phoenix.operators import ApexFormation
        
        op = ApexFormation()
        result = op.apply(triads=[("a", "s", "b")] * 3)
        
        assert result["apex_formed"] is True
        assert "sovereignty" in result
        assert result["apex_symbol"] == "△"
    
    def test_law_4_universal_triad_requires_three_pillars(self):
        """Test Law 4: Three pillars must be present."""
        from code.the_third.operators import CoherenceValidator
        
        validator = CoherenceValidator()
        result = validator.validate_cross_family(
            phx_ops=["Phoenix"],
            hgn_ops=["Hydrogenesi"],
            lns_ops=["TheThird"]
        )
        
        # All three families must be present
        assert result["all_families_present"] is True
        assert result["triadic_completion"] is True
    
    def test_law_5_recursion_depth_tracks_complexity(self):
        """Test Law 5: Recursion depth increases with complexity."""
        from code.hydrogenesi.operators import LineageLogic
        
        op = LineageLogic()
        shallow = op.apply(root="ROOT", generations=2)
        deep = op.apply(root="ROOT", generations=5)
        
        # Depth must increase
        assert shallow["depth"] == 2
        assert deep["depth"] == 5
        assert deep["depth"] > shallow["depth"]
    
    def test_law_6_self_similarity_across_scales(self):
        """Test Law 6: Self-similarity across recursive depths."""
        from code.phoenix.operators import IM_ME
        
        op = IM_ME()
        seq_3 = op.recurse(identity="self", depth=3)
        seq_5 = op.recurse(identity="self", depth=5)
        
        # Pattern repeats at different depths
        assert "IM(self)" in seq_3
        assert "IM(self)" in seq_5
        assert len(seq_3) < len(seq_5)
    
    def test_law_9_convergence_envelope_bounds_recursion(self):
        """Test Law 9: Convergence envelope contains all paths."""
        from code.phoenix.operators import ApexFormation
        
        op = ApexFormation()
        
        # Single triad - emerging sovereignty
        result_1 = op.apply(triads=[("a", "s", "b")])
        assert result_1["sovereignty"] == "emerging"
        
        # Five triads - sovereign apex
        result_5 = op.apply(triads=[("a", "s", "b")] * 5)
        assert result_5["sovereignty"] == "sovereign"
        
        # Sovereignty increases within bounded envelope


# ============================================================================
# META-OPERATOR TESTS (2 tests)
# ============================================================================

class TestMetaOperators:
    """Test meta-operator patterns."""
    
    def test_operator_composition_preserves_coherence(self):
        """Test that operator composition maintains coherence."""
        from code.phoenix.operators import FirstBinding
        from code.hydrogenesi.operators import StabilizerExtraction
        from code.the_third.operators import MetaBinder
        
        # Compose operators
        binding = FirstBinding()
        extraction = StabilizerExtraction()
        meta = MetaBinder()
        
        # Create structure
        triad = binding.apply(a="a", b="b", stabilizer="s")
        
        # Extract
        extracted = extraction.apply({
            "core": triad["stabilizer"],
            "shell": triad["tension_pair"]
        })
        
        # Meta-bind
        meta_struct = meta.bind("FirstBinding", "StabilizerExtraction", "Coherence")
        
        # Coherence preserved throughout
        assert meta_struct["coherence"] == "aligned"
    
    def test_cross_scale_behavior_analysis(self):
        """Test cross-scale behavior analysis."""
        from code.the_third.operators import CrossScaleBehavior
        
        analyzer = CrossScaleBehavior()
        
        # Test at different scales
        micro = analyzer.analyze(operator="TestOp", scale="micro")
        macro = analyzer.analyze(operator="TestOp", scale="macro")
        
        assert micro["scale"] == "micro"
        assert macro["scale"] == "macro"
        assert "cross_scale_impacts" in micro
        assert "cross_scale_impacts" in macro


# ============================================================================
# COMPOSITION PATTERN TESTS (3 tests)
# ============================================================================

class TestCompositionPatterns:
    """Test operator composition patterns."""
    
    def test_pattern_preservation_through_transformation(self):
        """Test Example 6: Pattern preservation during transformation."""
        from code.phoenix.operators import FirstBinding
        from code.hydrogenesi.operators import StabilizerExtraction, CurvatureResidue
        
        # Create pattern
        binding = FirstBinding()
        original = binding.apply(a="form", b="void", stabilizer="transform")
        
        # Transform
        extractor = StabilizerExtraction()
        transformed = extractor.apply({
            "core": original["stabilizer"],
            "shell": original["tension_pair"]
        })
        
        # Record trace
        residue = CurvatureResidue()
        trace = residue.apply(lineage_id="transform::001")
        
        # Pattern preserved through transformation
        assert transformed["extracted_core"] == "transform"
        assert "curvature-trace" in trace["residue"]
    
    def test_triadic_composition_rule(self):
        """Test that all stable structures resolve to triads."""
        from code.phoenix.operators import FirstBinding, ApexFormation
        
        # Single triad
        binding = FirstBinding()
        triad = binding.apply(a="1", b="2", stabilizer="3")
        assert len(triad["triad"]) == 3
        
        # Apex from triads
        apex = ApexFormation()
        result = apex.apply(triads=[triad["triad"]])
        assert result["apex_formed"] is True
        
        # Foundation is triadic
        assert all(len(t) == 3 for t in result["foundation"])
    
    def test_harmonic_resonance_across_pillars(self):
        """Test Example 7: Harmonic resonance pattern."""
        from code.phoenix.operators import FirstBinding, IM_ME
        from code.hydrogenesi.operators import AGNReplication, LineageLogic
        from code.the_third.operators import MetaBinder, CoherenceValidator
        
        # Phoenix operations
        binding = FirstBinding()
        triad = binding.apply(a="alpha", b="omega", stabilizer="unity")
        
        im_me = IM_ME()
        recursion = im_me.recurse(identity="harmonic", depth=2)
        
        # Hydrogenesi operations
        replication = AGNReplication()
        offspring = replication.apply(mass=100.0)
        
        lineage = LineageLogic()
        generations = lineage.apply(root="HARMONIC", generations=2)
        
        # The Third operations
        binder = MetaBinder()
        phx_bind = binder.bind("FirstBinding", "IM_ME", "Recursion")
        hgn_bind = binder.bind("AGNReplication", "LineageLogic", "Extension")
        
        # Validate global coherence
        validator = CoherenceValidator()
        coherence = validator.validate_cross_family(
            phx_ops=["FirstBinding", "IM_ME"],
            hgn_ops=["AGNReplication", "LineageLogic"],
            lns_ops=["MetaBinder", "CoherenceValidator"]
        )
        
        # All pillars must resonate
        assert coherence["all_families_present"] is True
        assert coherence["triadic_completion"] is True
        assert phx_bind["coherence"] == "aligned"
        assert hgn_bind["coherence"] == "aligned"


# ============================================================================
# TEST CONFIGURATION
# ============================================================================

def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line(
        "markers", "phoenix: mark test as Phoenix pillar test"
    )
    config.addinivalue_line(
        "markers", "hydrogenesi: mark test as Hydrogenesi pillar test"
    )
    config.addinivalue_line(
        "markers", "third: mark test as The Third pillar test"
    )
    config.addinivalue_line(
        "markers", "integration: mark test as cross-pillar integration test"
    )
    config.addinivalue_line(
        "markers", "laws: mark test as Universal Laws compliance test"
    )


if __name__ == "__main__":
    # Allow running as script for quick validation
    pytest.main([__file__, "-v", "--tb=short"])
