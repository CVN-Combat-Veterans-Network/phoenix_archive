"""
Three-Finger Waltz Meta-Operator

Cross-pillar pattern integration through rhythmic three-phase choreography.
Unifies Phoenix (BEGIN), Hydrogenesi (EXTEND), and The Third (HOLD) into sovereign whole.
"""

from __future__ import annotations
from dataclasses import dataclass, field
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
    timestamp: Optional[float] = None
    
    def __repr__(self) -> str:
        return (
            f"WaltzStep(phase={self.phase.value}, pillar={self.pillar}, "
            f"mode={self.mode}, transformation={self.transformation_applied})"
        )


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
    
    def __post_init__(self):
        """Initialize waltz state."""
        if not self.patterns:
            self.patterns = []
    
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
        
        # Record step
        step = WaltzStep(
            phase=WaltzPhase.INITIATION,
            pillar="Phoenix",
            mode="BEGIN",
            input_pattern=pattern,
            output_pattern=ignited,
            transformation_applied="Phoenix Ignition"
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
        
        # Record step
        step = WaltzStep(
            phase=WaltzPhase.TRANSFORMATION,
            pillar="Hydrogenesi",
            mode="EXTEND",
            input_pattern=ignited_pattern,
            output_pattern=propagated,
            transformation_applied="Hydrogenesi Propagation"
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
        
        # Record step
        step = WaltzStep(
            phase=WaltzPhase.INTEGRATION,
            pillar="The Third",
            mode="HOLD",
            input_pattern=propagated_pattern,
            output_pattern=integrated,
            transformation_applied="The Third Binding"
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
            ]
        }
        
        # Record step
        step = WaltzStep(
            phase=WaltzPhase.COMPLETION,
            pillar="Unified",
            mode="COMPLETE",
            input_pattern=integrated_pattern,
            output_pattern=completed,
            transformation_applied="Triadic Closure"
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
        
        # Use provided patterns or stored patterns
        patterns_to_integrate = patterns if patterns is not None else self.patterns
        
        if not patterns_to_integrate:
            return {
                "status": "NO_PATTERNS",
                "message": "✗ No patterns provided for integration",
                "steps": 0
            }
        
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
        
        return {
            "status": "WALTZ_COMPLETE",
            "message": "✓ Three-Finger Waltz complete - Sovereignty achieved",
            "pattern": completed,
            "steps": [
                {
                    "phase": step.phase.value,
                    "pillar": step.pillar,
                    "mode": step.mode,
                    "transformation": step.transformation_applied
                }
                for step in self._steps
            ],
            "phase_count": len(self._steps),
            "sovereignty": True
        }
    
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
