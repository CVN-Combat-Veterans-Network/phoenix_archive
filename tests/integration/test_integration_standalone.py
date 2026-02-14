"""Standalone tests for integration operators."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from code.integration.operators import (
    TransitionMap, Pillar, CompositionValidator, LawValidator,
    Operator, CompositionType
)


def test_phoenix_to_hydrogenesi():
    print("Testing Phoenix → Hydrogenesi transition...")
    tm = TransitionMap()
    
    result = tm.transition(
        Pillar.PHOENIX, 
        Pillar.HYDROGENESI, 
        {"a": "fear", "stabilizer": "service", "b": "courage", "stable": True}, 
        depth=2
    )
    
    assert result["source"] == "Phoenix", f"Expected Phoenix, got {result['source']}"
    assert result["target"] == "Hydrogenesi", f"Expected Hydrogenesi, got {result['target']}"
    assert result["depth_out"] == 2, f"Expected depth 2, got {result['depth_out']}"
    assert result["fidelity"] >= 0.95, f"Expected fidelity ≥0.95, got {result['fidelity']}"
    print("✓ Phoenix → Hydrogenesi transition works")


def test_third_to_phoenix_depth_increase():
    print("Testing The Third → Phoenix (depth increase)...")
    tm = TransitionMap()
    
    result = tm.transition(
        Pillar.THE_THIRD,
        Pillar.PHOENIX,
        {"hold_target": "service", "avoid_patterns": ["fear"], "hold_duration": 3, "needs_refresh": True},
        depth=2
    )
    
    assert result["depth_out"] == 3, f"Expected depth 3, got {result['depth_out']}"
    print("✓ The Third → Phoenix increases depth")


def test_composition_validation():
    print("Testing operator composition...")
    validator = CompositionValidator()
    
    op1 = Operator("First Binding", "Phoenix", "tension_pair", "triad", 0, 1)
    op2 = Operator("Three-Finger Waltz", "Phoenix", "triad", "rhythm", 1, 1)
    
    result = validator.compose([op1, op2], CompositionType.SEQUENTIAL)
    
    assert result["valid"] is True, f"Expected valid=True, got {result}"
    assert result["type"] == "sequential"
    print("✓ Sequential composition works")


def test_law_validation():
    print("Testing Universal Law validation...")
    validator = LawValidator()
    
    operation = {
        "name": "Test Op",
        "a": "tension1",
        "b": "tension2",
        "stabilizer": "stabilizer_s",
        "depth_in": 2,
        "depth_out": 3
    }
    
    result = validator.validate_all_laws(operation)
    
    assert result["validation_passed"] is True, f"Expected validation_passed=True, got {result}"
    print("✓ Law validation works")


def test_depth_reversal_caught():
    print("Testing depth reversal detection...")
    validator = CompositionValidator()
    
    op1 = Operator("High Depth", "Phoenix", "any", "any", 3, 3)
    op2 = Operator("Low Depth", "Phoenix", "any", "any", 1, 1)
    
    result = validator.compose([op1, op2], CompositionType.SEQUENTIAL)
    
    assert "error" in result, f"Expected error in result, got {result}"
    print("✓ Depth reversal caught")


if __name__ == "__main__":
    print("=" * 60)
    print("INTEGRATION TESTS - STANDALONE")
    print("=" * 60)
    
    tests = [
        test_phoenix_to_hydrogenesi,
        test_third_to_phoenix_depth_increase,
        test_composition_validation,
        test_law_validation,
        test_depth_reversal_caught
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ {test.__name__} failed: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__} error: {e}")
            failed += 1
    
    print("=" * 60)
    print(f"Results: {passed} passed, {failed} failed")
    print("=" * 60)
    
    if failed == 0:
        print("All tests passed! ✓")
        exit(0)
    else:
        print(f"{failed} test(s) failed")
        exit(1)
