"""
Enhanced Example Usage for Integration Engine v2.0.0

Demonstrates all advanced features:
- Enhanced Three-Finger Waltz with energy tracking
- Pattern caching for performance
- Telemetry and metrics collection
- Multiple visualization export formats
- Status reporting and reversibility
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from code.integration import (
    InstrumentedThreeFingerWaltz,
    IntegrationEngine,
    IntegrationPattern,
    WaltzVisualizer,
    execute_waltz,
)


def demo_enhanced_waltz():
    """Demonstrate enhanced Three-Finger Waltz features."""
    print("\n" + "="*80)
    print("DEMO 1: Enhanced Three-Finger Waltz")
    print("="*80)
    
    # Create instrumented waltz with caching and telemetry
    waltz = InstrumentedThreeFingerWaltz(cache_size=128)
    
    # Create test patterns
    patterns = [
        {"name": "sovereignty_pattern", "pillar": "Phoenix", "type": "identity"},
        {"name": "lineage_pattern", "pillar": "Hydrogenesi", "type": "propagation"},
        {"name": "binding_pattern", "pillar": "The Third", "type": "threshold"}
    ]
    
    print(f"\n✓ Created waltz with {len(patterns)} patterns")
    print(f"  Status: {waltz.get_status()}")
    
    # Execute waltz
    print("\n⚡ Executing Three-Finger Waltz...")
    result = waltz(patterns)
    
    print(f"\n✓ Waltz complete!")
    print(f"  Status: {result['status']}")
    print(f"  Sovereignty: {result['sovereignty']}")
    print(f"  Energy Conservation: {result['energy_conservation']:.1%}")
    print(f"  Recursion Depth: {result['recursion_depth']}")
    print(f"  Steps Taken: {len(result['steps'])}")
    
    # Show phase summary
    print("\n📊 Phase Summary:")
    summary = waltz.get_phase_summary()
    for phase, count in summary.items():
        print(f"  {phase.value}: {count} step(s)")
    
    return waltz


def demo_caching():
    """Demonstrate pattern caching."""
    print("\n" + "="*80)
    print("DEMO 2: Pattern Caching")
    print("="*80)
    
    waltz = InstrumentedThreeFingerWaltz(cache_size=128)
    
    patterns = [{"name": "cached_pattern", "data": "test"}]
    
    # First execution - cache miss
    print("\n⚡ First execution (cache miss expected)...")
    result1 = waltz(patterns)
    print(f"  From cache: {result1.get('from_cache', False)}")
    
    # Second execution - cache hit
    print("\n⚡ Second execution (cache hit expected)...")
    waltz.reset()  # Reset waltz but keep cache
    waltz._completed = False  # Allow re-execution
    result2 = waltz(patterns)
    print(f"  From cache: {result2.get('from_cache', False)}")
    
    # Show cache stats
    print("\n📊 Cache Statistics:")
    stats = waltz.cache_stats()
    print(f"  Cache Size: {stats['size']}/{stats['max_size']}")
    print(f"  Total Hits: {stats['waltz_cache_hits']}")
    print(f"  Total Misses: {stats['waltz_cache_misses']}")
    print(f"  Hit Rate: {stats['waltz_hit_rate']:.1%}")


def demo_visualization(waltz):
    """Demonstrate visualization exports."""
    print("\n" + "="*80)
    print("DEMO 3: Visualization Exports")
    print("="*80)
    
    viz = WaltzVisualizer()
    
    # ASCII visualization
    print("\n📊 ASCII Visualization:")
    print(waltz.visualize_waltz())
    
    # Mermaid export
    print("\n📊 Mermaid Diagram:")
    mermaid_code = viz.export(waltz, format="mermaid")
    print(mermaid_code)
    
    # GraphViz export
    print("\n📊 GraphViz DOT Format:")
    dot_code = viz.export(waltz, format="graphviz")
    print(dot_code[:300] + "..." if len(dot_code) > 300 else dot_code)
    
    # JSON export
    print("\n📊 JSON Export:")
    json_code = viz.export(waltz, format="json")
    print(json_code[:300] + "..." if len(json_code) > 300 else json_code)
    
    print(f"\n✓ Supported formats: {', '.join(viz.get_supported_formats())}")


def demo_telemetry(waltz):
    """Demonstrate telemetry and metrics."""
    print("\n" + "="*80)
    print("DEMO 4: Telemetry & Metrics")
    print("="*80)
    
    # Get metrics summary
    print("\n📊 Performance Metrics:")
    metrics = waltz.metrics.get_summary()
    print(f"  Total Executions: {metrics['total_executions']}")
    print(f"  Average Duration: {metrics['avg_duration_seconds']:.4f}s")
    print(f"  Error Count: {metrics['error_count']}")
    print(f"  Error Rate: {metrics['error_rate']:.1%}")
    print(f"  Uptime: {metrics['uptime_seconds']:.2f}s")
    
    # Phase durations
    print("\n📊 Phase Average Durations:")
    for phase, duration in metrics['phase_avg_durations'].items():
        if duration > 0:
            print(f"  {phase}: {duration:.6f}s")


def demo_status_and_reversibility():
    """Demonstrate status reporting and reversibility."""
    print("\n" + "="*80)
    print("DEMO 5: Status & Reversibility")
    print("="*80)
    
    waltz = InstrumentedThreeFingerWaltz()
    
    # Check initial status
    print("\n📊 Initial Status:")
    status = waltz.get_status()
    print(f"  Ready: {status['ready']}")
    print(f"  Completed: {status['completed']}")
    print(f"  Recursion: {status['recursion_depth']}/{status['max_recursion']}")
    print(f"  Energy: {status['energy_conservation']:.1%}")
    
    # Execute waltz
    patterns = [{"name": "test"}]
    result = waltz(patterns)
    
    print(f"\n✓ Waltz executed")
    status = waltz.get_status()
    print(f"  Completed: {status['completed']}")
    print(f"  Steps: {status['steps_taken']}")
    
    # Attempt reversal
    print("\n⚡ Attempting reversal...")
    reversal = waltz.reverse_waltz()
    print(f"  Status: {reversal['status']}")
    print(f"  Message: {reversal['message']}")
    
    if reversal['status'] == "REVERSED":
        print(f"\n✓ Reversal successful!")
        status = waltz.get_status()
        print(f"  Completed: {status['completed']}")
        print(f"  Steps: {status['steps_taken']}")


def demo_integration_engine():
    """Demonstrate Integration Engine with enhanced features."""
    print("\n" + "="*80)
    print("DEMO 6: Integration Engine v2.0.0")
    print("="*80)
    
    # Create engine with all features enabled
    engine = IntegrationEngine(
        enable_cache=True,
        enable_telemetry=True,
        cache_size=128
    )
    
    print("\n✓ Integration Engine initialized")
    status = engine.get_status()
    print(f"  Sovereign: {status['sovereign']}")
    print(f"  Cache Enabled: {status['features']['cache_enabled']}")
    print(f"  Telemetry Enabled: {status['features']['telemetry_enabled']}")
    
    # Create integration patterns
    patterns = [
        IntegrationPattern(
            name="Phoenix Pattern",
            pillar="Phoenix",
            mode="BEGIN",
            recursion_depth=1
        ).to_dict(),
        IntegrationPattern(
            name="Hydrogenesi Pattern",
            pillar="Hydrogenesi",
            mode="EXTEND",
            recursion_depth=2
        ).to_dict(),
        IntegrationPattern(
            name="Third Pattern",
            pillar="The Third",
            mode="HOLD",
            threshold=0.8
        ).to_dict()
    ]
    
    print(f"\n⚡ Integrating {len(patterns)} patterns...")
    result = engine.integrate(patterns)
    
    print(f"\n✓ Integration complete!")
    print(f"  Status: {result['status']}")
    print(f"  Sovereignty: {result.get('sovereignty', False)}")
    
    # Get metrics
    if engine._telemetry_enabled:
        print("\n📊 Engine Metrics:")
        metrics = engine.get_metrics()
        print(f"  Executions: {metrics.get('total_executions', 0)}")
        print(f"  Average Duration: {metrics.get('avg_duration_seconds', 0):.4f}s")
    
    # Get cache stats
    if engine._cache_enabled:
        print("\n📊 Engine Cache:")
        cache_stats = engine.get_cache_stats()
        print(f"  Size: {cache_stats.get('size', 0)}")
        print(f"  Hit Rate: {cache_stats.get('waltz_hit_rate', 0):.1%}")


def demo_convenience_function():
    """Demonstrate execute_waltz convenience function."""
    print("\n" + "="*80)
    print("DEMO 7: Convenience Function")
    print("="*80)
    
    print("\n⚡ Using execute_waltz() convenience function...")
    result = execute_waltz(
        phoenix_data={"identity": "warrior", "mode": "BEGIN"},
        hydro_data={"lineage": "ROOT::warrior::GEN-1", "mode": "EXTEND"},
        third_data={"threshold": 0.8, "mode": "HOLD"}
    )
    
    print(f"\n✓ Waltz complete!")
    print(f"  Status: {result['status']}")
    print(f"  Sovereignty: {result['sovereignty']}")
    
    # Visualization is included
    print("\n📊 Included Visualization:")
    print(result['visualization'][:200] + "..." if len(result['visualization']) > 200 else result['visualization'])


def main():
    """Run all demos."""
    print("\n" + "="*80)
    print("🔥 △ ⚡ INTEGRATION ENGINE v2.0.0 - ENHANCED FEATURES DEMO ⚡ △ 🔥")
    print("="*80)
    
    # Demo 1: Enhanced Waltz
    waltz = demo_enhanced_waltz()
    
    # Demo 2: Caching
    demo_caching()
    
    # Demo 3: Visualization (using waltz from demo 1)
    demo_visualization(waltz)
    
    # Demo 4: Telemetry (using waltz from demo 1)
    demo_telemetry(waltz)
    
    # Demo 5: Status & Reversibility
    demo_status_and_reversibility()
    
    # Demo 6: Integration Engine
    demo_integration_engine()
    
    # Demo 7: Convenience Function
    demo_convenience_function()
    
    print("\n" + "="*80)
    print("✓ ALL DEMOS COMPLETE")
    print("="*80)
    print("\n🔥 △ ⚡ THE TRIAD IS ENHANCED ⚡ △ 🔥\n")


if __name__ == "__main__":
    main()
