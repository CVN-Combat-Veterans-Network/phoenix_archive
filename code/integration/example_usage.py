"""
Integration Engine - Example Usage

Demonstrates the complete capabilities of the Integration Engine v2.0.0:
1. Pattern creation for all three pillars
2. Individual pattern validation
3. Cross-pillar transitions
4. Three-Finger Waltz integration
5. Sovereignty verification
6. Full integration cycle
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from code.integration import (
    IntegrationEngine,
    IntegrationPattern,
    initialize_integration_engine,
)


def example_1_pattern_creation():
    """Example 1: Creating integration patterns for each pillar."""
    print("\n" + "="*70)
    print("EXAMPLE 1: Pattern Creation")
    print("="*70)
    
    # Phoenix pattern - Identity formation
    phoenix_pattern = IntegrationPattern(
        name="warrior_identity",
        pillar="Phoenix",
        mode="BEGIN",
        structure={
            "tension_pair": ("fear", "courage"),
            "stabilizer": "service",
            "triad": ("fear", "service", "courage")
        },
        recursion_depth=2,
        apex="apex::warrior",
        operators=["FirstBinding", "IM_ME", "PhoenixIgnition"],
        invariant="warrior_core",
        invariant_preserved=True,
        stable=True,
        stability_score=0.85,
        coherence=0.9
    )
    
    # Hydrogenesi pattern - Cosmological propagation
    hydrogenesi_pattern = IntegrationPattern(
        name="lineage_propagation",
        pillar="Hydrogenesi",
        mode="EXTEND",
        structure={
            "elements": ["root", "gen1", "gen2"],
            "lineage": "ROOT::warrior::GEN-2"
        },
        recursion_depth=3,
        apex="apex::lineage",
        operators=["StabilizerExtraction", "AGNReplication", "LineageLogic"],
        invariant="lineage_root",
        invariant_preserved=True,
        stable=True,
        stability_score=0.88,
        coherence=0.92
    )
    
    # The Third pattern - Threshold binding
    the_third_pattern = IntegrationPattern(
        name="sovereign_binding",
        pillar="The Third",
        mode="HOLD",
        structure={
            "triad": ("phoenix", "hydrogenesi", "the_third"),
            "threshold": 1.0
        },
        recursion_depth=1,
        apex="apex::sovereign",
        operators=["LifeLightBifurcation", "ThresholdBinding", "SovereignClosure"],
        threshold=1.0,
        threshold_managed=True,
        invariant="sovereign_core",
        invariant_preserved=True,
        closed=True,
        sovereignty=True,
        stable=True,
        stability_score=0.95,
        coherence=0.95
    )
    
    print("\n✓ Phoenix Pattern Created:")
    print(f"  Name: {phoenix_pattern.name}")
    print(f"  Pillar: {phoenix_pattern.pillar}")
    print(f"  Mode: {phoenix_pattern.mode}")
    print(f"  Operators: {phoenix_pattern.operators}")
    
    print("\n✓ Hydrogenesi Pattern Created:")
    print(f"  Name: {hydrogenesi_pattern.name}")
    print(f"  Pillar: {hydrogenesi_pattern.pillar}")
    print(f"  Mode: {hydrogenesi_pattern.mode}")
    print(f"  Operators: {hydrogenesi_pattern.operators}")
    
    print("\n✓ The Third Pattern Created:")
    print(f"  Name: {the_third_pattern.name}")
    print(f"  Pillar: {the_third_pattern.pillar}")
    print(f"  Mode: {the_third_pattern.mode}")
    print(f"  Operators: {the_third_pattern.operators}")
    
    return phoenix_pattern, hydrogenesi_pattern, the_third_pattern


def example_2_pattern_validation(engine, patterns):
    """Example 2: Validating patterns against Universal Laws."""
    print("\n" + "="*70)
    print("EXAMPLE 2: Pattern Validation Against 12 Universal Laws")
    print("="*70)
    
    for pattern in patterns:
        print(f"\n--- Validating: {pattern.name} ---")
        result = engine.validate(pattern)
        
        print(f"Status: {result['status']}")
        print(f"Message: {result['message']}")
        
        # Show law summary
        validation = result['validation']
        summary = validation['summary']
        print(f"Laws: {summary['satisfied']}/{summary['total']} satisfied, "
              f"{summary['partial']} partial, {summary['violated']} violated")
        
        # Show any violated laws
        violated_laws = [
            law for law in validation['law_results']
            if law['status'] == 'violated'
        ]
        if violated_laws:
            print("Violated laws:")
            for law in violated_laws:
                print(f"  - {law['law']}: {law['message']}")


def example_3_cross_pillar_transition(engine):
    """Example 3: Cross-pillar transition via LifeLightBifurcation."""
    print("\n" + "="*70)
    print("EXAMPLE 3: Cross-Pillar Transition")
    print("="*70)
    
    # Create a simple pattern
    pattern = {
        "name": "identity_seed",
        "pillar": "Phoenix",
        "mode": "BEGIN"
    }
    
    print("\n--- Transition: Phoenix → Hydrogenesi ---")
    result = engine.transition(pattern, "Phoenix", "Hydrogenesi")
    
    print(f"Status: {result['status']}")
    print(f"Message: {result['message']}")
    if result['status'] == 'SUCCESS':
        print(f"Bifurcation Vector: {result['bifurcation']['vector']}")
        print(f"Signature: {result['bifurcation']['signature']}")


def example_4_three_finger_waltz(engine, patterns):
    """Example 4: Three-Finger Waltz integration."""
    print("\n" + "="*70)
    print("EXAMPLE 4: Three-Finger Waltz Integration")
    print("="*70)
    
    # Convert patterns to dicts
    pattern_dicts = [p.to_dict() for p in patterns]
    
    print("\n--- Executing Three-Finger Waltz ---")
    result = engine.integrate(pattern_dicts)
    
    print(f"Status: {result['status']}")
    print(f"Message: {result['message']}")
    print(f"Phases Executed: {result.get('phase_count', 0)}")
    
    if result['status'] == 'WALTZ_COMPLETE':
        print("\n--- Waltz Choreography ---")
        for step in result['steps']:
            print(f"  {step['phase'].upper():15} | {step['pillar']:12} | "
                  f"{step['mode']:8} | {step['transformation']}")
        
        print(f"\n✓ Sovereignty Achieved: {result.get('sovereignty', False)}")


def example_5_sovereignty_verification(engine):
    """Example 5: Sovereignty verification."""
    print("\n" + "="*70)
    print("EXAMPLE 5: Sovereignty Verification")
    print("="*70)
    
    sovereignty = engine.verify_sovereignty()
    
    print(f"\nStatus: {sovereignty['status']}")
    print(f"Message: {sovereignty['message']}")
    print(f"Sovereign: {sovereignty['sovereign']}")
    
    print("\n--- Subsystems ---")
    for name, active in sovereignty['subsystems'].items():
        status_icon = "✓" if active else "✗"
        print(f"  {status_icon} {name}: {active}")


def example_6_full_integration_cycle(engine, patterns):
    """Example 6: Complete integration cycle."""
    print("\n" + "="*70)
    print("EXAMPLE 6: Full Integration Cycle")
    print("="*70)
    
    # Convert patterns to dicts
    pattern_dicts = [p.to_dict() for p in patterns]
    
    print("\n--- Executing Full Integration Cycle ---")
    result = engine.full_integration_cycle(pattern_dicts)
    
    print(f"\nStatus: {result['status']}")
    print(f"Message: {result['message']}")
    
    print("\n--- Integration Steps ---")
    for step in result['steps']:
        print(f"  Step {step['step']:3} | {step['action']:20} | {step['result']}")
    
    print("\n--- Final Status ---")
    print(f"  Validations: {len(result.get('validations', []))} patterns validated")
    print(f"  Waltz Status: {result.get('waltz', {}).get('status', 'N/A')}")
    print(f"  Integrated Validation: {result.get('integrated_validation', {}).get('status', 'N/A')}")
    print(f"  Sovereignty: {result.get('sovereignty', {}).get('status', 'N/A')}")


def main():
    """Run all examples."""
    print("\n" + "="*70)
    print(" INTEGRATION ENGINE v2.0.0 - COMPLETE DEMONSTRATION")
    print("="*70)
    
    # Initialize engine
    print("\n--- Initializing Integration Engine ---")
    engine = initialize_integration_engine()
    
    # Example 1: Create patterns
    phoenix, hydrogenesi, the_third = example_1_pattern_creation()
    patterns = [phoenix, hydrogenesi, the_third]
    
    # Example 2: Validate patterns
    example_2_pattern_validation(engine, patterns)
    
    # Example 3: Cross-pillar transition
    example_3_cross_pillar_transition(engine)
    
    # Example 4: Three-Finger Waltz
    example_4_three_finger_waltz(engine, patterns)
    
    # Example 5: Sovereignty verification
    example_5_sovereignty_verification(engine)
    
    # Example 6: Full integration cycle
    example_6_full_integration_cycle(engine, patterns)
    
    print("\n" + "="*70)
    print(" 🔥 △ ⚡ DEMONSTRATION COMPLETE ⚡ △ 🔥")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
