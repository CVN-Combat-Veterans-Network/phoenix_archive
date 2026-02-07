"""
Test Suite for Triad Integration
=================================

Tests for Phoenix Archive triad system including:
- Phoenix operators
- Hydrogenesi operators
- The Third operators
- Triad Recursion Engine
- Cross-system integration

Run with: python tests/test_triad_integration.py
"""

import sys
import unittest
sys.path.insert(0, '/home/runner/work/phoenix_archive/phoenix_archive')

from code.phoenix.operators import FirstBinding, IM_ME, PhoenixIgnition
from code.hydrogenesi.operators import (
    LineageLogic, AGNReplication, StabilizerExtraction, CurvatureResidue
)
from code.thethird.operators import (
    BindingProtocols, TriadRecursion, ScaleTranslation, 
    PatternSynthesis, MetaBinding
)
from src.engine.triad_recursion_engine import (
    TriadRecursionEngine, initialize_triad_engine,
    Scale, SystemType, Pattern
)


class TestPhoenixOperators(unittest.TestCase):
    """Test Phoenix (micro-scale) operators."""
    
    def test_first_binding(self):
        """Test FirstBinding operator creates triads."""
        binding = FirstBinding()
        result = binding.apply(a="fear", b="courage", stabilizer="service")
        
        self.assertEqual(result['tension_pair'], ("fear", "courage"))
        self.assertEqual(result['stabilizer'], "service")
        self.assertEqual(result['triad'], ("fear", "service", "courage"))
    
    def test_im_me_recursion(self):
        """Test IM_ME operator generates recursion sequence."""
        im_me = IM_ME()
        sequence = im_me.recurse("SELF", depth=3)
        
        self.assertEqual(len(sequence), 6)  # depth * 2
        self.assertIn("IM(SELF)", sequence)
        self.assertIn("ME(SELF)", sequence)
    
    def test_phoenix_ignition(self):
        """Test PhoenixIgnition operator transformation."""
        ignition = PhoenixIgnition()
        result = ignition.ignite("old-identity")
        
        self.assertIn("collapsed", result)
        self.assertIn("risen", result)
        self.assertIn("core::", result['collapsed'])
        self.assertIn("apex::", result['risen'])


class TestHydrogonesiOperators(unittest.TestCase):
    """Test Hydrogenesi (macro-scale) operators."""
    
    def test_lineage_logic(self):
        """Test LineageLogic operator generates lineage chain."""
        lineage = LineageLogic()
        result = lineage.apply("ROOT", generations=4)
        
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0], "ROOT::gen-0")
        self.assertEqual(result[-1], "ROOT::gen-3")
    
    def test_agn_replication(self):
        """Test AGN Replication operator."""
        agn = AGNReplication(compression_factor=0.8, replication_factor=2)
        offspring = agn.apply(mass=1000.0)
        
        self.assertEqual(len(offspring), 2)
        self.assertEqual(sum(offspring), 800.0)  # 1000 * 0.8
    
    def test_stabilizer_extraction(self):
        """Test StabilizerExtraction operator."""
        extractor = StabilizerExtraction()
        result = extractor.apply({
            "core": "neutron",
            "shell": "proton-electron"
        })
        
        self.assertEqual(result['pre_seed'], "proton-electron")
        self.assertEqual(result['extracted_core'], "neutron")
        self.assertIsNone(result['core_void'])
    
    def test_curvature_residue(self):
        """Test CurvatureResidue operator."""
        residue = CurvatureResidue()
        result = residue.apply("galaxy-prime")
        
        self.assertEqual(result['lineage_id'], "galaxy-prime")
        self.assertEqual(result['status'], "collapsed")
        self.assertIn("curvature-trace", result['residue'])


class TestTheThirdOperators(unittest.TestCase):
    """Test The Third (meta-scale) operators."""
    
    def test_binding_protocols(self):
        """Test BindingProtocols creates cross-system binding."""
        binding = BindingProtocols()
        result = binding.apply(
            phoenix_op="FirstBinding",
            hydrogenesi_op="LineageLogic"
        )
        
        self.assertEqual(result['micro_component'], "FirstBinding")
        self.assertEqual(result['macro_component'], "LineageLogic")
        self.assertIn("⟷", result['binding'])
        self.assertEqual(result['status'], "bound")
    
    def test_triad_recursion(self):
        """Test TriadRecursion generates multi-scale sequence."""
        recursion = TriadRecursion()
        sequence = recursion.recurse("pattern", scales=3)
        
        self.assertEqual(len(sequence), 3)
        self.assertIn("MICRO(pattern)", sequence)
        self.assertIn("META(pattern)", sequence)
        self.assertIn("MACRO(pattern)", sequence)
    
    def test_scale_translation(self):
        """Test ScaleTranslation converts patterns between scales."""
        translator = ScaleTranslation()
        result = translator.translate(
            pattern="test-pattern",
            from_scale="micro",
            to_scale="macro"
        )
        
        self.assertEqual(result['from_scale'], "micro")
        self.assertEqual(result['to_scale'], "macro")
        self.assertEqual(result['from_system'], "Phoenix")
        self.assertEqual(result['to_system'], "Hydrogenesi")
        self.assertTrue(result['preserved_structure'])
    
    def test_pattern_synthesis(self):
        """Test PatternSynthesis creates new operators."""
        synthesizer = PatternSynthesis()
        result = synthesizer.synthesize([
            "Phoenix::FirstBinding",
            "Hydrogenesi::LineageLogic"
        ])
        
        self.assertEqual(len(result['input_patterns']), 2)
        self.assertIn("Unified::", result['synthesized_operator'])
        self.assertEqual(result['status'], "synthesized")
    
    def test_meta_binding(self):
        """Test MetaBinding creates triadic structure."""
        meta = MetaBinding()
        result = meta.apply("A", "B", "C")
        
        self.assertEqual(result['triad'], ("A", "C", "B"))
        self.assertEqual(result['binding_element'], "C")


class TestTriadRecursionEngine(unittest.TestCase):
    """Test Triad Recursion Engine."""
    
    def setUp(self):
        """Initialize engine for each test."""
        self.engine = TriadRecursionEngine()
    
    def test_initialize_engine(self):
        """Test engine initialization with core patterns."""
        engine = initialize_triad_engine()
        status = engine.get_system_status()
        
        self.assertGreater(status['patterns_registered'], 0)
        self.assertGreater(status['bindings_active'], 0)
        self.assertEqual(status['triad_status'], "UNIFIED")
    
    def test_register_pattern(self):
        """Test pattern registration."""
        pattern = self.engine.register_pattern(
            name="TestPattern",
            structure="test-structure",
            scale=Scale.MICRO,
            system=SystemType.PHOENIX
        )
        
        self.assertEqual(pattern.name, "TestPattern")
        self.assertEqual(pattern.scale, Scale.MICRO)
        self.assertEqual(pattern.system, SystemType.PHOENIX)
    
    def test_find_patterns(self):
        """Test pattern search."""
        # Register test patterns
        self.engine.register_pattern(
            "P1", "s1", Scale.MICRO, SystemType.PHOENIX
        )
        self.engine.register_pattern(
            "P2", "s2", Scale.MACRO, SystemType.HYDROGENESI
        )
        
        phoenix_patterns = self.engine.find_patterns(system=SystemType.PHOENIX)
        micro_patterns = self.engine.find_patterns(scale=Scale.MICRO)
        
        self.assertEqual(len(phoenix_patterns), 1)
        self.assertEqual(len(micro_patterns), 1)
    
    def test_recurse_pattern(self):
        """Test pattern recursion."""
        pattern = Pattern(
            name="TestPattern",
            structure="test",
            scale=Scale.MICRO,
            system=SystemType.PHOENIX
        )
        
        recursion = self.engine.recurse_pattern(pattern, depth=3)
        
        self.assertEqual(len(recursion), 3)
        self.assertIn("GEN-0", recursion[0])
    
    def test_bind_systems(self):
        """Test system binding."""
        binding = self.engine.bind_systems(
            SystemType.PHOENIX,
            SystemType.HYDROGENESI,
            SystemType.THE_THIRD
        )
        
        self.assertEqual(binding['system_a'], "Phoenix")
        self.assertEqual(binding['system_b'], "Hydrogenesi")
        self.assertEqual(binding['mediator'], "TheThird")
        self.assertTrue(binding['triad_complete'])
    
    def test_translate_scale(self):
        """Test scale translation."""
        pattern = Pattern(
            name="TestPattern",
            structure="test",
            scale=Scale.MICRO,
            system=SystemType.PHOENIX
        )
        
        translated = self.engine.translate_scale(pattern, Scale.MACRO)
        
        self.assertEqual(translated.scale, Scale.MACRO)
        self.assertEqual(translated.system, SystemType.HYDROGENESI)
        self.assertTrue(translated.metadata.get('translated'))
    
    def test_execute_triad_operation(self):
        """Test unified triad operation."""
        result = self.engine.execute_triad_operation(
            operation="TestOp",
            param1="value1"
        )
        
        self.assertEqual(result['operation'], "TestOp")
        self.assertIn('micro_result', result)
        self.assertIn('meta_result', result)
        self.assertIn('macro_result', result)
        self.assertIn('unified_result', result)
        self.assertEqual(result['status'], "executed")


class TestCrossSystemIntegration(unittest.TestCase):
    """Test integration between all three systems."""
    
    def test_phoenix_to_hydrogenesi_binding(self):
        """Test binding Phoenix operation to Hydrogenesi operation."""
        binding = BindingProtocols()
        result = binding.apply("IM_ME", "LineageLogic")
        
        self.assertIn("IM_ME", result['unified_operator'])
        self.assertIn("LineageLogic", result['unified_operator'])
    
    def test_complete_triad_operation(self):
        """Test operation involving all three systems."""
        # Phoenix operation
        phoenix_binding = FirstBinding()
        phoenix_result = phoenix_binding.apply("a", "b", "c")
        
        # Hydrogenesi operation
        lineage = LineageLogic()
        hydro_result = lineage.apply("ROOT", 2)
        
        # The Third integration
        meta_binding = BindingProtocols()
        triad_result = meta_binding.apply("FirstBinding", "LineageLogic")
        
        # Verify all three worked
        self.assertIsNotNone(phoenix_result)
        self.assertIsNotNone(hydro_result)
        self.assertIsNotNone(triad_result)
        self.assertEqual(triad_result['status'], "bound")
    
    def test_pattern_flow_through_scales(self):
        """Test pattern flowing through all three scales."""
        translator = ScaleTranslation()
        
        # Micro -> Meta
        micro_to_meta = translator.translate("pattern", "micro", "meta")
        self.assertEqual(micro_to_meta['to_system'], "TheThird")
        
        # Meta -> Macro
        meta_to_macro = translator.translate("pattern", "meta", "macro")
        self.assertEqual(meta_to_macro['to_system'], "Hydrogenesi")
        
        # Macro -> Micro (complete cycle)
        macro_to_micro = translator.translate("pattern", "macro", "micro")
        self.assertEqual(macro_to_micro['to_system'], "Phoenix")


def run_tests():
    """Run all tests and return results."""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestPhoenixOperators))
    suite.addTests(loader.loadTestsFromTestCase(TestHydrogonesiOperators))
    suite.addTests(loader.loadTestsFromTestCase(TestTheThirdOperators))
    suite.addTests(loader.loadTestsFromTestCase(TestTriadRecursionEngine))
    suite.addTests(loader.loadTestsFromTestCase(TestCrossSystemIntegration))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result


if __name__ == "__main__":
    print("\n" + "="*70)
    print("PHOENIX ARCHIVE: TRIAD INTEGRATION TEST SUITE")
    print("="*70 + "\n")
    
    result = run_tests()
    
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    print(f"Tests Run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.wasSuccessful():
        print("\n✅ ALL TESTS PASSED")
        print("\n🔥🌌⚡ THE TRIAD IS VERIFIED ⚡🌌🔥\n")
        sys.exit(0)
    else:
        print("\n❌ SOME TESTS FAILED")
        sys.exit(1)
