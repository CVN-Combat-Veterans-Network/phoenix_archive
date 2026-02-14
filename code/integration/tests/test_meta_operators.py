"""
Comprehensive Unit Tests for Three-Finger Waltz Meta-Operator

Tests all functionality including:
- Basic initialization and execution
- Phase transitions
- Step tracking and numbering
- Energy conservation
- Recursion limits
- Visualization
- Status and reversibility
- Edge cases
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

from datetime import datetime
from code.integration.meta_operators import ThreeFingerWaltz, WaltzPhase, WaltzStep, execute_waltz

try:
    import pytest
    PYTEST_AVAILABLE = True
except ImportError:
    PYTEST_AVAILABLE = False
    # Create a dummy pytest module for decorator compatibility
    class pytest:
        @staticmethod
        def skip(msg):
            pass


class TestThreeFingerWaltzBasicFunctionality:
    """Test basic waltz functionality."""
    
    def test_waltz_initialization(self):
        """Test waltz initializes with correct default state."""
        waltz = ThreeFingerWaltz()
        assert waltz.is_ready()
        assert waltz.recursion_depth == 0
        assert len(waltz.waltz_history) == 0
        assert waltz._completed == False
        assert waltz._energy_conservation == 1.0
        assert waltz.max_recursion == 7
        assert waltz._step_counter == 0
    
    def test_waltz_is_ready(self):
        """Test readiness conditions."""
        waltz = ThreeFingerWaltz()
        assert waltz.is_ready() == True
        
        # Complete the waltz
        patterns = [{"name": "test"}]
        waltz.dance(patterns)
        assert waltz.is_ready() == False  # Not ready after completion
    
    def test_waltz_execution(self):
        """Test complete waltz execution."""
        waltz = ThreeFingerWaltz()
        patterns = [{"name": "pattern1"}]
        result = waltz(patterns)
        
        assert result["status"] == "WALTZ_COMPLETE"
        assert result["triadic_closure"] == True
        assert result["sovereignty"] == True
        assert len(waltz._steps) == 4  # 4 phases
    
    def test_waltz_with_three_patterns(self):
        """Test waltz with standard 3-pattern integration."""
        waltz = ThreeFingerWaltz()
        patterns = [
            {"name": "phoenix_pattern", "pillar": "Phoenix"},
            {"name": "hydro_pattern", "pillar": "Hydrogenesi"},
            {"name": "third_pattern", "pillar": "The Third"}
        ]
        result = waltz.dance(patterns)
        
        assert result["status"] == "WALTZ_COMPLETE"
        assert result["sovereignty"] == True
        assert len(waltz._steps) == 4
    
    def test_waltz_signature(self):
        """Test that triadic signature is present."""
        waltz = ThreeFingerWaltz()
        result = waltz.dance([{"name": "test"}])
        
        assert "signature" in result["pattern"]
        assert result["pattern"]["signature"] == "🜂🜁🜃"


class TestPhaseTransitions:
    """Test individual phase execution."""
    
    def test_initiation_phase(self):
        """Test Phoenix ignition phase."""
        waltz = ThreeFingerWaltz()
        pattern = {"name": "test_pattern"}
        
        ignited = waltz.execute_phase_1_initiation(pattern)
        
        assert ignited["pillar"] == "Phoenix"
        assert ignited["mode"] == "BEGIN"
        assert ignited["phase"] == "INITIATION"
        assert ignited["ignited"] == True
        assert "phoenix_signature" in ignited
        assert waltz._energy_conservation == 1.0
    
    def test_transformation_phase(self):
        """Test Hydrogenesi propagation phase."""
        waltz = ThreeFingerWaltz()
        ignited = {"core": "test", "name": "test_pattern"}
        
        propagated = waltz.execute_phase_2_transformation(ignited)
        
        assert propagated["pillar"] == "Hydrogenesi"
        assert propagated["mode"] == "EXTEND"
        assert propagated["phase"] == "TRANSFORMATION"
        assert propagated["propagated"] == True
        assert "hydrogenesi_signature" in propagated
        assert waltz._energy_conservation == 0.95
    
    def test_integration_phase(self):
        """Test The Third binding phase."""
        waltz = ThreeFingerWaltz()
        propagated = {"propagated": {"ignited": {"core": "test"}}}
        
        integrated = waltz.execute_phase_3_integration(propagated)
        
        assert integrated["pillar"] == "The Third"
        assert integrated["mode"] == "HOLD"
        assert integrated["phase"] == "INTEGRATION"
        assert integrated["bound"] == True
        assert integrated["sovereignty"] == True
        assert "the_third_signature" in integrated
        assert waltz._energy_conservation == 0.90
    
    def test_completion_phase(self):
        """Test triadic closure phase."""
        waltz = ThreeFingerWaltz()
        integrated = {
            "propagated": {
                "ignited": {"core": "test"}
            }
        }
        
        completed = waltz.execute_phase_4_completion(integrated)
        
        assert completed["phase"] == "COMPLETION"
        assert completed["triadic_closure"] == True
        assert completed["sovereignty_confirmed"] == True
        assert completed["waltz_complete"] == True
        assert "triad" in completed
        assert waltz._completed == True
    
    def test_phase_summary(self):
        """Test phase summary counts."""
        waltz = ThreeFingerWaltz()
        waltz.dance([{"name": "test"}])
        
        summary = waltz.get_phase_summary()
        
        assert summary[WaltzPhase.INITIATION] == 1
        assert summary[WaltzPhase.TRANSFORMATION] == 1
        assert summary[WaltzPhase.INTEGRATION] == 1
        assert summary[WaltzPhase.COMPLETION] == 1


class TestStepTracking:
    """Test step history and tracking."""
    
    def test_waltz_history_recorded(self):
        """Test that all steps are logged."""
        waltz = ThreeFingerWaltz()
        waltz.dance([{"name": "test"}])
        
        assert len(waltz.waltz_history) == 1
        assert len(waltz._steps) == 4
    
    def test_waltz_path(self):
        """Test path extraction is correct."""
        waltz = ThreeFingerWaltz()
        waltz.dance([{"name": "test"}])
        
        choreography = waltz.get_choreography()
        assert len(choreography) == 4
        
        # Verify order
        assert choreography[0]["phase"] == "initiation"
        assert choreography[1]["phase"] == "transformation"
        assert choreography[2]["phase"] == "integration"
        assert choreography[3]["phase"] == "completion"
    
    def test_step_numbering(self):
        """Test sequential step numbering."""
        waltz = ThreeFingerWaltz()
        waltz.dance([{"name": "test"}])
        
        assert waltz._steps[0].step_number == 1
        assert waltz._steps[1].step_number == 2
        assert waltz._steps[2].step_number == 3
        assert waltz._steps[3].step_number == 4
    
    def test_step_timestamps(self):
        """Test temporal ordering of steps."""
        waltz = ThreeFingerWaltz()
        waltz.dance([{"name": "test"}])
        
        # All steps should have timestamps
        for step in waltz._steps:
            assert isinstance(step.timestamp, datetime)
        
        # Steps should be in chronological order
        for i in range(len(waltz._steps) - 1):
            assert waltz._steps[i].timestamp <= waltz._steps[i + 1].timestamp


class TestEnergyConservation:
    """Test energy tracking through phases."""
    
    def test_energy_tracking(self):
        """Test energy decreases correctly through phases."""
        waltz = ThreeFingerWaltz()
        
        # Initial energy
        assert waltz._energy_conservation == 1.0
        
        # After phase 1 (Phoenix ignition)
        waltz.execute_phase_1_initiation({"name": "test"})
        assert waltz._energy_conservation == 1.0
        
        # After phase 2 (Hydrogenesi propagation)
        waltz.execute_phase_2_transformation({"core": "test"})
        assert waltz._energy_conservation == 0.95
        
        # After phase 3 (The Third binding)
        waltz.execute_phase_3_integration({"propagated": {"ignited": {}}})
        assert waltz._energy_conservation == 0.90
    
    def test_energy_in_final_metrics(self):
        """Test energy is included in completion result."""
        waltz = ThreeFingerWaltz()
        result = waltz.dance([{"name": "test"}])
        
        assert "energy_conservation" in result
        assert result["energy_conservation"] == 0.90
    
    def test_energy_conservation_bounds(self):
        """Test energy stays between 0.0 and 1.0."""
        waltz = ThreeFingerWaltz()
        waltz.dance([{"name": "test"}])
        
        assert 0.0 <= waltz._energy_conservation <= 1.0


class TestRecursionLimits:
    """Test recursion depth tracking and limits."""
    
    def test_recursion_depth_increment(self):
        """Test depth increases with each execution."""
        waltz = ThreeFingerWaltz()
        
        assert waltz.recursion_depth == 0
        waltz.dance([{"name": "test1"}])
        assert waltz.recursion_depth == 1
    
    def test_recursion_depth_limit(self):
        """Test waltz stops at max recursion."""
        waltz = ThreeFingerWaltz()
        waltz.recursion_depth = 7  # Set to max
        
        result = waltz.dance([{"name": "test"}])
        
        assert result["status"] == "MAX_RECURSION"
        assert "Maximum recursion depth" in result["message"]
    
    def test_max_recursion_error(self):
        """Test error at recursion limit."""
        waltz = ThreeFingerWaltz()
        
        # Execute up to limit
        for i in range(7):
            waltz.reset()
            waltz.recursion_depth = i
            result = waltz.dance([{"name": f"test{i}"}])
            if i < 7:
                assert result["status"] == "WALTZ_COMPLETE"
        
        # Now at limit
        waltz.reset()
        waltz.recursion_depth = 7
        result = waltz.dance([{"name": "test"}])
        assert result["status"] == "MAX_RECURSION"


class TestVisualization:
    """Test ASCII visualization methods."""
    
    def test_visualize_waltz(self):
        """Test ASCII output is generated."""
        waltz = ThreeFingerWaltz()
        waltz.dance([{"name": "test"}])
        
        viz = waltz.visualize_waltz()
        
        assert isinstance(viz, str)
        assert len(viz) > 0
        assert "THREE-FINGER WALTZ CHOREOGRAPHY" in viz
    
    def test_visualization_contains_steps(self):
        """Test all steps are present in visualization."""
        waltz = ThreeFingerWaltz()
        waltz.dance([{"name": "test"}])
        
        viz = waltz.visualize_waltz()
        
        # Should contain all 4 steps
        assert "Step 1" in viz
        assert "Step 2" in viz
        assert "Step 3" in viz
        assert "Step 4" in viz
    
    def test_visualization_format(self):
        """Test visualization has correct formatting."""
        waltz = ThreeFingerWaltz()
        waltz.dance([{"name": "test"}])
        
        viz = waltz.visualize_waltz()
        
        # Should have borders
        assert "=" * 80 in viz
        
        # Should show status
        assert "COMPLETE" in viz or "IN PROGRESS" in viz
        
        # Should show energy
        assert "Energy Conservation" in viz


class TestStatusAndReversibility:
    """Test status reporting and reversal methods."""
    
    def test_get_status(self):
        """Test status dictionary is complete."""
        waltz = ThreeFingerWaltz()
        status = waltz.get_status()
        
        assert "ready" in status
        assert "recursion_depth" in status
        assert "max_recursion" in status
        assert "steps_taken" in status
        assert "energy_conservation" in status
        assert "time_elapsed" in status
        assert "current_phase" in status
        assert "completed" in status
        
        assert status["ready"] == True
        assert status["recursion_depth"] == 0
        assert status["max_recursion"] == 7
    
    def test_reverse_waltz(self):
        """Test undo of last completion."""
        waltz = ThreeFingerWaltz()
        waltz.dance([{"name": "test"}])
        
        assert waltz._completed == True
        assert len(waltz.waltz_history) == 1
        
        result = waltz.reverse_waltz()
        
        assert result["status"] == "REVERSED"
        assert waltz._completed == False
        assert len(waltz.waltz_history) == 0
        assert waltz._step_counter == 0
    
    def test_reverse_empty_waltz(self):
        """Test reversal handles no history."""
        waltz = ThreeFingerWaltz()
        result = waltz.reverse_waltz()
        
        assert result["status"] == "NO_HISTORY"
        assert "No waltz history" in result["message"]
    
    def test_reset_waltz(self):
        """Test full reset to initial state."""
        waltz = ThreeFingerWaltz()
        waltz.dance([{"name": "test"}])
        
        # State should be modified
        assert waltz._completed == True
        assert len(waltz._steps) > 0
        
        # Reset
        waltz.reset()
        
        # State should be clean
        assert waltz._completed == False
        assert len(waltz._steps) == 0
        assert waltz._step_counter == 0
        assert waltz.recursion_depth == 0
        assert waltz._energy_conservation == 1.0


class TestEdgeCases:
    """Test edge cases and error handling."""
    
    def test_insufficient_patterns(self):
        """Test warning with < 3 patterns."""
        waltz = ThreeFingerWaltz()
        
        # Should warn but still execute with 1 pattern
        result = waltz.dance([{"name": "single"}])
        assert result["status"] == "WALTZ_COMPLETE"
    
    def test_empty_patterns(self):
        """Test handling of empty pattern list."""
        waltz = ThreeFingerWaltz()
        result = waltz.dance([])
        
        assert result["status"] == "NO_PATTERNS"
        assert "No patterns provided" in result["message"]
    
    def test_none_patterns(self):
        """Test handling of None patterns."""
        waltz = ThreeFingerWaltz()
        result = waltz.dance(None)
        
        # Should use stored patterns, which are empty
        assert result["status"] == "NO_PATTERNS"
    
    def test_already_complete(self):
        """Test double execution prevention."""
        waltz = ThreeFingerWaltz()
        waltz.dance([{"name": "test"}])
        
        # Try to execute again
        result = waltz.dance([{"name": "test2"}])
        
        assert result["status"] == "ALREADY_COMPLETE"
        assert "already completed" in result["message"]
    
    def test_call_method(self):
        """Test direct __call__ invocation."""
        waltz = ThreeFingerWaltz()
        result = waltz([{"name": "test"}])
        
        assert result["status"] == "WALTZ_COMPLETE"
        assert result["sovereignty"] == True


class TestConvenienceFunction:
    """Test the execute_waltz convenience function."""
    
    def test_execute_waltz_basic(self):
        """Test basic execute_waltz function."""
        result = execute_waltz("phoenix_data", "hydro_data", "third_data")
        
        assert result["status"] == "WALTZ_COMPLETE"
        assert "visualization" in result
        assert "phase_summary" in result
    
    def test_execute_waltz_patterns(self):
        """Test execute_waltz creates proper patterns."""
        result = execute_waltz(
            {"id": 1, "type": "phoenix"},
            {"id": 2, "type": "hydro"},
            {"id": 3, "type": "third"}
        )
        
        assert result["status"] == "WALTZ_COMPLETE"
        assert result["sovereignty"] == True


class TestStepStringRepresentation:
    """Test WaltzStep string methods."""
    
    def test_step_str_method(self):
        """Test WaltzStep __str__ output."""
        step = WaltzStep(
            phase=WaltzPhase.INITIATION,
            pillar="Phoenix",
            mode="BEGIN",
            input_pattern={},
            transformation_applied="Phoenix Ignition",
            step_number=1
        )
        
        step_str = str(step)
        assert "Step 1" in step_str
        assert "initiation" in step_str
        assert "Phoenix" in step_str
        assert "Phoenix Ignition" in step_str
    
    def test_step_repr_method(self):
        """Test WaltzStep __repr__ output."""
        step = WaltzStep(
            phase=WaltzPhase.TRANSFORMATION,
            pillar="Hydrogenesi",
            mode="EXTEND",
            input_pattern={},
            step_number=2
        )
        
        step_repr = repr(step)
        assert "WaltzStep" in step_repr
        assert "transformation" in step_repr
        assert "Hydrogenesi" in step_repr


class TestWaltzRepr:
    """Test ThreeFingerWaltz __repr__ method."""
    
    def test_waltz_repr(self):
        """Test waltz string representation."""
        waltz = ThreeFingerWaltz()
        
        repr_str = repr(waltz)
        assert "ThreeFingerWaltz" in repr_str
        assert "initiation" in repr_str
        assert "steps=0" in repr_str
        assert "completed=False" in repr_str
        assert "energy=" in repr_str
        assert "recursion=0/7" in repr_str


if __name__ == "__main__":
    # Run tests if pytest is available
    try:
        import pytest
        pytest.main([__file__, "-v"])
    except ImportError:
        print("pytest not installed. Running basic tests...")
        
        # Run a few basic tests manually
        test_basic = TestThreeFingerWaltzBasicFunctionality()
        test_basic.test_waltz_initialization()
        print("✓ test_waltz_initialization passed")
        
        test_basic.test_waltz_execution()
        print("✓ test_waltz_execution passed")
        
        test_phase = TestPhaseTransitions()
        test_phase.test_phase_summary()
        print("✓ test_phase_summary passed")
        
        print("\n✓ All basic tests passed!")
