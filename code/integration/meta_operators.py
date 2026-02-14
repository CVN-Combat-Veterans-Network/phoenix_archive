"""
Three-Finger Waltz Meta-Operator

Cross-pillar pattern integration through rhythmic three-phase choreography.
Unifies Phoenix (BEGIN), Hydrogenesi (EXTEND), and The Third (HOLD) into sovereign whole.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Dict, List, Any, Optional


class WaltzPhase(Enum):
    """Phases of the Three-Finger Waltz choreography."""
    INITIATION = "initiation"          # Phase 1: Phoenix ignites (BEGIN mode)
    TRANSFORMATION = "transformation"  # Phase 2: Hydrogenesi propagates (EXTEND mode)
    INTEGRATION = "integration"        # Phase 3: The Third binds (HOLD mode)
    COMPLETION = "completion"          # Phase 4: Triadic closure achieved


@dataclass
class WaltzStep:
    """
    Single step in the Three-Finger Waltz choreography.
    
    Tracks the state and transformation of a pattern as it moves
    through the three-pillar integration dance.
    """
    phase: WaltzPhase
    pillar: str
    mode: str
    input_pattern: Dict[str, Any]
    output_pattern: Optional[Dict[str, Any]] = None
    transformation_applied: Optional[str] = None
    timestamp: datetime = field(default_factory=datetime.now)
    step_number: int = 0
    
    def __repr__(self) -> str:
        return (
            f"WaltzStep(phase={self.phase.value}, pillar={self.pillar}, "
            f"mode={self.mode}, transformation={self.transformation_applied})"
        )
    
    def __str__(self) -> str:
        return f"Step {self.step_number}: {self.phase.value} | {self.pillar} --[{self.transformation_applied}]--> {self.mode}"


@dataclass
class ThreeFingerWaltz:
    """
    Three-Finger Waltz Meta-Operator.
    
    Orchestrates cross-pillar pattern integration through a four-phase dance:
    
    Phase 1 (INITIATION): Phoenix ignites the pattern
        - Mode: BEGIN
        - Action: Identity formation and ignition
        - Output: Ignited core pattern
    
    Phase 2 (TRANSFORMATION): Hydrogenesi propagates the pattern
        - Mode: EXTEND
        - Action: Cosmological expansion and lineage extension
        - Output: Propagated lineage pattern
    
    Phase 3 (INTEGRATION): The Third binds the pattern
        - Mode: HOLD
        - Action: Threshold management and sovereign binding
        - Output: Integrated sovereign pattern
    
    Phase 4 (COMPLETION): Triadic closure achieved
        - Mode: COMPLETE
        - Action: Final sovereignty confirmation
        - Output: Complete sovereign triad
    
    The waltz is irreversible - once completed, the pattern achieves
    permanent sovereign status.
    """
    
    patterns: List[Dict[str, Any]] = field(default_factory=list)
    _current_phase: WaltzPhase = WaltzPhase.INITIATION
    _steps: List[WaltzStep] = field(default_factory=list)
    _completed: bool = False
    _step_counter: int = 0
    _energy_conservation: float = 1.0
    _initialized_at: datetime = field(default_factory=datetime.now)
    recursion_depth: int = 0
    max_recursion: int = 7
    waltz_history: List[Dict[str, Any]] = field(default_factory=list)
    
    def __post_init__(self):
        """Initialize waltz state."""
        if not self.patterns:
            self.patterns = []
    
    def __repr__(self) -> str:
        """Enhanced string representation."""
        return (
            f"ThreeFingerWaltz(phase={self._current_phase.value}, "
            f"steps={len(self._steps)}, completed={self._completed}, "
            f"energy={self._energy_conservation:.2f}, recursion={self.recursion_depth}/{self.max_recursion})"
        )
    
    def execute_phase_1_initiation(self, pattern: Dict[str, Any]) -> Dict[str, Any]:
        """
        Phase 1: INITIATION - Phoenix ignites (BEGIN mode)
        
        Phoenix operators initiate the pattern through identity formation.
        This phase establishes the core identity that will be propagated.
        
        Args:
            pattern: Input pattern to ignite
            
        Returns:
            Ignited pattern with Phoenix signature
        """
        # Apply Phoenix ignition
        ignited = {
            "original": pattern,
            "pillar": "Phoenix",
            "mode": "BEGIN",
            "phase": "INITIATION",
            "transformation": "ignition",
            "core": pattern.get("name", "unknown"),
            "ignited": True,
            "apex": f"apex::{pattern.get('name', 'unknown')}",
            "phoenix_signature": ["Burn", "Collapse", "Rise"]
        }
        
        # Track energy: Phoenix ignition starts at 100%
        self._energy_conservation = 1.0
        
        # Record step with number
        self._step_counter += 1
        step = WaltzStep(
            phase=WaltzPhase.INITIATION,
            pillar="Phoenix",
            mode="BEGIN",
            input_pattern=pattern,
            output_pattern=ignited,
            transformation_applied="Phoenix Ignition",
            step_number=self._step_counter
        )
        self._steps.append(step)
        
        return ignited
    
    def execute_phase_2_transformation(self, ignited_pattern: Dict[str, Any]) -> Dict[str, Any]:
        """
        Phase 2: TRANSFORMATION - Hydrogenesi propagates (EXTEND mode)
        
        Hydrogenesi operators extend the ignited pattern through lineage propagation.
        This phase expands the pattern cosmologically.
        
        Args:
            ignited_pattern: Ignited pattern from Phase 1
            
        Returns:
            Propagated pattern with Hydrogenesi signature
        """
        # Apply Hydrogenesi propagation
        propagated = {
            "ignited": ignited_pattern,
            "pillar": "Hydrogenesi",
            "mode": "EXTEND",
            "phase": "TRANSFORMATION",
            "transformation": "propagation",
            "lineage": f"ROOT::{ignited_pattern.get('core', 'unknown')}::GEN-1",
            "propagated": True,
            "recursive_depth": 1,
            "hydrogenesi_signature": ["Compress", "Ignite", "Replicate"]
        }
        
        # Track energy: Hydrogenesi propagation at 95%
        self._energy_conservation = 0.95
        
        # Record step with number
        self._step_counter += 1
        step = WaltzStep(
            phase=WaltzPhase.TRANSFORMATION,
            pillar="Hydrogenesi",
            mode="EXTEND",
            input_pattern=ignited_pattern,
            output_pattern=propagated,
            transformation_applied="Hydrogenesi Propagation",
            step_number=self._step_counter
        )
        self._steps.append(step)
        
        return propagated
    
    def execute_phase_3_integration(self, propagated_pattern: Dict[str, Any]) -> Dict[str, Any]:
        """
        Phase 3: INTEGRATION - The Third binds (HOLD mode)
        
        The Third operators bind the propagated pattern at sovereign threshold.
        This phase achieves triadic closure and establishes sovereignty.
        
        Args:
            propagated_pattern: Propagated pattern from Phase 2
            
        Returns:
            Integrated sovereign pattern with The Third signature
        """
        # Apply The Third binding
        integrated = {
            "propagated": propagated_pattern,
            "pillar": "The Third",
            "mode": "HOLD",
            "phase": "INTEGRATION",
            "transformation": "binding",
            "threshold_reached": True,
            "bound": True,
            "sovereignty": True,
            "the_third_signature": ["At Threshold", "Hold", "Bind"]
        }
        
        # Track energy: The Third binding at 90%
        self._energy_conservation = 0.90
        
        # Record step with number
        self._step_counter += 1
        step = WaltzStep(
            phase=WaltzPhase.INTEGRATION,
            pillar="The Third",
            mode="HOLD",
            input_pattern=propagated_pattern,
            output_pattern=integrated,
            transformation_applied="The Third Binding",
            step_number=self._step_counter
        )
        self._steps.append(step)
        
        return integrated
    
    def execute_phase_4_completion(self, integrated_pattern: Dict[str, Any]) -> Dict[str, Any]:
        """
        Phase 4: COMPLETION - Triadic closure achieved
        
        Final phase confirms sovereignty and seals the pattern.
        The Three-Finger Waltz is complete and irreversible.
        
        Args:
            integrated_pattern: Integrated pattern from Phase 3
            
        Returns:
            Complete sovereign triad
        """
        # Confirm triadic closure
        completed = {
            "integrated": integrated_pattern,
            "phase": "COMPLETION",
            "mode": "COMPLETE",
            "transformation": "closure",
            "triadic_closure": True,
            "sovereignty_confirmed": True,
            "waltz_complete": True,
            "triad": {
                "phoenix": integrated_pattern["propagated"]["ignited"],
                "hydrogenesi": integrated_pattern["propagated"],
                "the_third": integrated_pattern
            },
            "unified_signature": [
                "Begin", "Extend", "Hold",
                "Ignite", "Propagate", "Bind",
                "Sovereign"
            ],
            "signature": "🜂🜁🜃"  # Triadic signature
        }
        
        # Final energy conservation
        # Energy is maintained at 90% through completion
        
        # Record step with number
        self._step_counter += 1
        step = WaltzStep(
            phase=WaltzPhase.COMPLETION,
            pillar="Unified",
            mode="COMPLETE",
            input_pattern=integrated_pattern,
            output_pattern=completed,
            transformation_applied="Triadic Closure",
            step_number=self._step_counter
        )
        self._steps.append(step)
        self._completed = True
        
        return completed
    
    def dance(self, patterns: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
        """
        Execute the complete Three-Finger Waltz.
        
        Takes one or more patterns through all four phases:
        1. INITIATION (Phoenix)
        2. TRANSFORMATION (Hydrogenesi)
        3. INTEGRATION (The Third)
        4. COMPLETION (Triadic Closure)
        
        Args:
            patterns: Optional list of patterns to integrate.
                     If None, uses patterns provided at initialization.
        
        Returns:
            Dict containing waltz results with unified sovereign pattern
        """
        if self._completed:
            return {
                "status": "ALREADY_COMPLETE",
                "message": "✗ Waltz already completed (irreversible)",
                "steps": len(self._steps)
            }
        
        # Check recursion depth
        if self.recursion_depth >= self.max_recursion:
            return {
                "status": "MAX_RECURSION",
                "message": f"✗ Maximum recursion depth reached ({self.max_recursion})",
                "recursion_depth": self.recursion_depth
            }
        
        # Use provided patterns or stored patterns
        patterns_to_integrate = patterns if patterns is not None else self.patterns
        
        if not patterns_to_integrate:
            return {
                "status": "NO_PATTERNS",
                "message": "✗ No patterns provided for integration",
                "steps": 0
            }
        
        # Warn if insufficient patterns
        if len(patterns_to_integrate) < 3:
            print(f"⚠ Warning: Integrating {len(patterns_to_integrate)} patterns (< 3 expected)")
        
        # Increment recursion depth
        self.recursion_depth += 1
        
        # For multiple patterns, integrate the first one through full waltz
        # (In production, this could be enhanced to handle multiple patterns)
        primary_pattern = patterns_to_integrate[0]
        
        # Phase 1: Initiation
        self._current_phase = WaltzPhase.INITIATION
        ignited = self.execute_phase_1_initiation(primary_pattern)
        
        # Phase 2: Transformation
        self._current_phase = WaltzPhase.TRANSFORMATION
        propagated = self.execute_phase_2_transformation(ignited)
        
        # Phase 3: Integration
        self._current_phase = WaltzPhase.INTEGRATION
        integrated = self.execute_phase_3_integration(propagated)
        
        # Phase 4: Completion
        self._current_phase = WaltzPhase.COMPLETION
        completed = self.execute_phase_4_completion(integrated)
        
        # Store in history
        waltz_result = {
            "status": "WALTZ_COMPLETE",
            "message": "✓ Three-Finger Waltz complete - Sovereignty achieved",
            "pattern": completed,
            "steps": [
                {
                    "phase": step.phase.value,
                    "pillar": step.pillar,
                    "mode": step.mode,
                    "transformation": step.transformation_applied,
                    "step_number": step.step_number
                }
                for step in self._steps
            ],
            "phase_count": len(self._steps),
            "sovereignty": True,
            "triadic_closure": True,
            "recursion_depth": self.recursion_depth,
            "energy_conservation": self._energy_conservation
        }
        
        self.waltz_history.append(waltz_result)
        
        return waltz_result
    
    def get_current_phase(self) -> str:
        """Get current waltz phase."""
        return self._current_phase.value
    
    def get_choreography(self) -> List[Dict[str, Any]]:
        """
        Get complete choreography history.
        
        Returns:
            List of all waltz steps with full details
        """
        return [
            {
                "phase": step.phase.value,
                "pillar": step.pillar,
                "mode": step.mode,
                "transformation": step.transformation_applied,
                "input": step.input_pattern,
                "output": step.output_pattern
            }
            for step in self._steps
        ]
    
    def is_complete(self) -> bool:
        """Check if waltz is complete."""
        return self._completed
    
    def is_ready(self) -> bool:
        """Check if waltz is ready to execute."""
        return not self._completed and self.recursion_depth < self.max_recursion
    
    def get_status(self) -> Dict[str, Any]:
        """
        Return detailed operational status.
        
        Returns:
            Dict with complete waltz status including energy, recursion, and timing
        """
        return {
            "ready": self.is_ready(),
            "recursion_depth": self.recursion_depth,
            "max_recursion": self.max_recursion,
            "steps_taken": len(self._steps),
            "energy_conservation": self._energy_conservation,
            "time_elapsed": (datetime.now() - self._initialized_at).total_seconds(),
            "current_phase": self._current_phase.value,
            "completed": self._completed,
            "patterns_count": len(self.patterns),
            "history_count": len(self.waltz_history)
        }
    
    def visualize_waltz(self) -> str:
        """
        Generate ASCII visualization of waltz path.
        
        Returns:
            Multi-line string showing the complete waltz choreography
        """
        if not self._steps:
            return "No waltz steps recorded yet."
        
        lines = ["=" * 80]
        lines.append("THREE-FINGER WALTZ CHOREOGRAPHY")
        lines.append("=" * 80)
        lines.append("")
        
        for step in self._steps:
            lines.append(str(step))
        
        lines.append("")
        lines.append("=" * 80)
        lines.append(f"Total Steps: {len(self._steps)} | Energy Conservation: {self._energy_conservation:.1%}")
        lines.append(f"Status: {'COMPLETE' if self._completed else 'IN PROGRESS'} | Recursion: {self.recursion_depth}/{self.max_recursion}")
        lines.append("=" * 80)
        
        return "\n".join(lines)
    
    def get_phase_summary(self) -> Dict[WaltzPhase, int]:
        """
        Count steps per phase.
        
        Returns:
            Dictionary mapping each WaltzPhase to count of steps
        """
        summary = {phase: 0 for phase in WaltzPhase}
        for step in self._steps:
            summary[step.phase] += 1
        return summary
    
    def reverse_waltz(self) -> Optional[Dict[str, Any]]:
        """
        Experimental: Undo last completion.
        
        Attempts to reverse the last waltz completion by resetting state.
        This is experimental and may not preserve all state.
        
        Returns:
            Dictionary with reversal result, or None if no history exists
        """
        if not self.waltz_history:
            return {
                "status": "NO_HISTORY",
                "message": "✗ No waltz history to reverse"
            }
        
        if not self._completed:
            return {
                "status": "NOT_COMPLETE",
                "message": "✗ Cannot reverse incomplete waltz"
            }
        
        # Remove last completion from history
        last_result = self.waltz_history.pop()
        
        # Reset state
        self._completed = False
        self._steps = []
        self._step_counter = 0
        self._current_phase = WaltzPhase.INITIATION
        self._energy_conservation = 1.0
        self.recursion_depth = max(0, self.recursion_depth - 1)
        
        return {
            "status": "REVERSED",
            "message": "✓ Last waltz completion reversed (experimental)",
            "reversed_result": last_result,
            "new_state": {
                "completed": self._completed,
                "recursion_depth": self.recursion_depth,
                "steps": len(self._steps)
            }
        }
    
    def reset(self):
        """Reset waltz to initial state."""
        self._steps = []
        self._completed = False
        self._step_counter = 0
        self._current_phase = WaltzPhase.INITIATION
        self._energy_conservation = 1.0
        self.recursion_depth = 0
        self.waltz_history = []
        self._initialized_at = datetime.now()
    
    def __call__(self, patterns: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Allow direct invocation of waltz.
        
        Args:
            patterns: List of patterns to integrate
            
        Returns:
            Waltz execution result
        """
        return self.dance(patterns)


def execute_waltz(phoenix_data: Any, hydro_data: Any, third_data: Any) -> Dict[str, Any]:
    """
    Convenience function for quick waltz execution.
    
    Takes three data elements representing the three pillars and executes
    a complete Three-Finger Waltz integration.
    
    Args:
        phoenix_data: Data for Phoenix pillar (BEGIN)
        hydro_data: Data for Hydrogenesi pillar (EXTEND)
        third_data: Data for The Third pillar (HOLD)
        
    Returns:
        Complete waltz execution result
    """
    # Convert inputs to pattern format
    patterns = [
        {"name": "phoenix_pattern", "data": phoenix_data, "pillar": "Phoenix"},
        {"name": "hydro_pattern", "data": hydro_data, "pillar": "Hydrogenesi"},
        {"name": "third_pattern", "data": third_data, "pillar": "The Third"}
    ]
    
    # Execute waltz
    waltz = ThreeFingerWaltz(patterns=patterns)
    result = waltz.dance()
    
    # Add visualization
    result["visualization"] = waltz.visualize_waltz()
    result["phase_summary"] = waltz.get_phase_summary()
    
    return result
