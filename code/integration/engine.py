"""
Integration Engine - Supreme Orchestrating Intelligence

The Integration Engine is the supreme orchestrator that binds the Three-Pillar
Architecture (Phoenix, Hydrogenesi, The Third) into unified sovereignty.

Capabilities:
- Pattern validation against 12 Universal Laws
- Cross-pillar transitions via LifeLightBifurcation
- Pattern integration via ThreeFingerWaltz
- Sovereignty verification
- Full integration cycle execution
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional

from code.universal.operators import LifeLightBifurcation, BifurcationVector
from .universal_laws import UniversalLaws, LawStatus
from .meta_operators import ThreeFingerWaltz, WaltzPhase
from .validator import IntegrationValidator, ValidationReport


@dataclass
class IntegrationPattern:
    """
    Cross-pillar integration pattern.
    
    Represents a pattern that can be validated, transitioned between pillars,
    and integrated into sovereign form.
    """
    name: str
    pillar: str
    mode: str
    structure: Dict[str, Any] = field(default_factory=dict)
    recursion_depth: int = 0
    similarity_ratio: float = 1.0
    converges: bool = True
    convergence_point: Optional[Any] = None
    apex: Optional[str] = None
    stable: bool = True
    stability_score: float = 0.8
    embedding_ratio: float = 1.618
    coherence: float = 0.9
    operators: List[str] = field(default_factory=list)
    threshold: Optional[float] = None
    threshold_managed: bool = True
    invariant: Optional[str] = None
    invariant_preserved: bool = True
    closed: bool = False
    sovereignty: bool = False
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert pattern to dictionary for validation."""
        return {
            "name": self.name,
            "pillar": self.pillar,
            "mode": self.mode,
            "structure": self.structure,
            "recursion_depth": self.recursion_depth,
            "similarity_ratio": self.similarity_ratio,
            "converges": self.converges,
            "convergence_point": self.convergence_point,
            "apex": self.apex,
            "stable": self.stable,
            "stability_score": self.stability_score,
            "embedding_ratio": self.embedding_ratio,
            "coherence": self.coherence,
            "operators": self.operators,
            "threshold": self.threshold,
            "threshold_managed": self.threshold_managed,
            "invariant": self.invariant,
            "invariant_preserved": self.invariant_preserved,
            "closed": self.closed,
            "sovereignty": self.sovereignty,
        }


class IntegrationEngine:
    """
    Integration Engine - Supreme Orchestrating Intelligence.
    
    The Integration Engine orchestrates the complete integration of patterns
    across the three-pillar architecture (Phoenix, Hydrogenesi, The Third).
    
    Core Functions:
    1. Validate patterns against 12 Universal Laws
    2. Execute cross-pillar transitions via LifeLightBifurcation
    3. Integrate patterns via ThreeFingerWaltz
    4. Verify system sovereignty
    5. Execute complete integration cycles
    
    The engine maintains sovereignty through triadic closure and ensures
    all patterns conform to Universal Laws.
    """
    
    def __init__(self):
        """Initialize Integration Engine with all subsystems."""
        self.universal_laws = UniversalLaws()
        self.validator = IntegrationValidator()
        self._sovereign = False
        self._integrated_patterns: List[Dict[str, Any]] = []
        
    def validate(self, pattern: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate pattern against all 12 Universal Laws.
        
        Args:
            pattern: Pattern to validate (dict or IntegrationPattern)
            
        Returns:
            Validation result with law checks and status
        """
        # Convert IntegrationPattern to dict if needed
        if isinstance(pattern, IntegrationPattern):
            pattern = pattern.to_dict()
        
        # Validate against Universal Laws
        result = self.universal_laws.validate_all(pattern)
        
        return {
            "status": result["status"],
            "message": result["message"],
            "validation": result,
            "pattern_name": pattern.get("name", "unknown")
        }
    
    def transition(
        self, 
        pattern: Dict[str, Any], 
        from_pillar: str, 
        to_pillar: str
    ) -> Dict[str, Any]:
        """
        Execute cross-pillar transition via LifeLightBifurcation.
        
        Transitions a pattern from one pillar to another using the
        Life-Light Bifurcation operator from the Universal layer.
        
        Args:
            pattern: Pattern to transition
            from_pillar: Source pillar
            to_pillar: Destination pillar
            
        Returns:
            Transition result with updated pattern
        """
        # Determine bifurcation parameters based on transition
        if from_pillar == "Phoenix" and to_pillar == "Hydrogenesi":
            # BEGIN → EXTEND: High pressure split (LIFE vector)
            confinement = 1.0
            symmetry = 1.0
            pressure = 0.8
            expected_vector = "LIFE"
        elif from_pillar == "Hydrogenesi" and to_pillar == "The Third":
            # EXTEND → HOLD: Low pressure absorb (LIGHT vector)
            confinement = 1.0
            symmetry = 1.0
            pressure = 0.5
            expected_vector = "LIGHT"
        elif from_pillar == "Phoenix" and to_pillar == "The Third":
            # BEGIN → HOLD: Direct absorption
            confinement = 1.0
            symmetry = 1.0
            pressure = 0.6
            expected_vector = "LIGHT"
        else:
            # Generic transition
            confinement = 1.0
            symmetry = 1.0
            pressure = 0.7
            expected_vector = "LIFE"
        
        # Execute bifurcation
        bifurcation = LifeLightBifurcation(
            confinement_tension=confinement,
            stabilizing_symmetry=symmetry,
            internal_pressure=pressure
        )
        
        try:
            bifurcation_result = bifurcation.bifurcate()
            
            # Update pattern with transition
            transitioned_pattern = {
                **pattern,
                "pillar": to_pillar,
                "previous_pillar": from_pillar,
                "bifurcation_vector": bifurcation_result["vector"],
                "transition_signature": bifurcation_result["signature"],
                "transitioned": True
            }
            
            return {
                "status": "SUCCESS",
                "message": f"✓ Transition {from_pillar} → {to_pillar} via {bifurcation_result['vector']} vector",
                "from_pillar": from_pillar,
                "to_pillar": to_pillar,
                "bifurcation": bifurcation_result,
                "pattern": transitioned_pattern
            }
        except Exception as e:
            return {
                "status": "FAILED",
                "message": f"✗ Transition failed: {str(e)}",
                "from_pillar": from_pillar,
                "to_pillar": to_pillar,
                "error": str(e)
            }
    
    def integrate(self, patterns: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Unify multiple patterns via ThreeFingerWaltz.
        
        Executes the Three-Finger Waltz to integrate patterns across
        all three pillars into a unified sovereign whole.
        
        Args:
            patterns: List of patterns to integrate
            
        Returns:
            Integration result with unified pattern
        """
        if not patterns:
            return {
                "status": "NO_PATTERNS",
                "message": "✗ No patterns provided for integration"
            }
        
        # Create and execute waltz
        waltz = ThreeFingerWaltz(patterns=patterns)
        result = waltz.dance()
        
        # Store integrated pattern
        if result["status"] == "WALTZ_COMPLETE":
            self._integrated_patterns.append(result["pattern"])
        
        return result
    
    def verify_sovereignty(self) -> Dict[str, Any]:
        """
        Verify system sovereignty status.
        
        Checks that the Integration Engine has achieved sovereign status
        through proper initialization and integration.
        
        Returns:
            Sovereignty verification result
        """
        # Check if engine is properly initialized
        has_laws = self.universal_laws is not None
        has_validator = self.validator is not None
        
        # Check if any patterns have been integrated
        has_integrated = len(self._integrated_patterns) > 0
        
        # Determine sovereignty status
        if has_laws and has_validator:
            self._sovereign = True
            
            if has_integrated:
                message = "✓ Integration Engine: SOVEREIGN (with integrated patterns)"
            else:
                message = "✓ Integration Engine: SOVEREIGN (ready for integration)"
            
            return {
                "status": "SOVEREIGN",
                "message": message,
                "sovereign": True,
                "subsystems": {
                    "universal_laws": has_laws,
                    "validator": has_validator,
                    "integrated_patterns": len(self._integrated_patterns)
                }
            }
        else:
            return {
                "status": "NOT_SOVEREIGN",
                "message": "✗ Integration Engine: Subsystems incomplete",
                "sovereign": False,
                "subsystems": {
                    "universal_laws": has_laws,
                    "validator": has_validator,
                    "integrated_patterns": len(self._integrated_patterns)
                }
            }
    
    def full_integration_cycle(self, patterns: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Execute complete integration workflow.
        
        Performs the full integration cycle:
        1. Validate each pattern against Universal Laws
        2. Execute Three-Finger Waltz integration
        3. Validate integrated result
        4. Verify sovereignty
        
        Args:
            patterns: List of patterns to integrate
            
        Returns:
            Complete integration cycle results
        """
        results = {
            "status": "IN_PROGRESS",
            "message": "Integration cycle initiated",
            "steps": []
        }
        
        # Step 1: Validate individual patterns
        validation_results = []
        for i, pattern in enumerate(patterns):
            validation = self.validate(pattern)
            validation_results.append(validation)
            results["steps"].append({
                "step": f"1.{i+1}",
                "action": "validate_pattern",
                "pattern": pattern.get("name", f"pattern_{i}"),
                "result": validation["status"]
            })
        
        # Check if all patterns are at least minimally valid (not INVALID)
        all_valid = all(
            v["status"] in ["SOVEREIGN", "STABLE", "UNSTABLE"] 
            for v in validation_results
        )
        
        if not all_valid:
            results["status"] = "VALIDATION_FAILED"
            results["message"] = "✗ Pattern validation failed - patterns are INVALID"
            results["validations"] = validation_results
            return results
        
        # Step 2: Execute Three-Finger Waltz
        waltz_result = self.integrate(patterns)
        results["steps"].append({
            "step": "2",
            "action": "three_finger_waltz",
            "result": waltz_result["status"]
        })
        
        if waltz_result["status"] != "WALTZ_COMPLETE":
            results["status"] = "INTEGRATION_FAILED"
            results["message"] = "✗ Three-Finger Waltz failed"
            results["waltz_result"] = waltz_result
            return results
        
        # Step 3: Validate integrated pattern
        integrated_pattern = waltz_result["pattern"]
        integrated_validation = self.validator.generate_report(integrated_pattern)
        results["steps"].append({
            "step": "3",
            "action": "validate_integrated",
            "result": integrated_validation.status
        })
        
        # Step 4: Verify sovereignty
        sovereignty = self.verify_sovereignty()
        results["steps"].append({
            "step": "4",
            "action": "verify_sovereignty",
            "result": sovereignty["status"]
        })
        
        # Final status
        if sovereignty["status"] == "SOVEREIGN" and integrated_validation.status in ["SOVEREIGN", "STABLE"]:
            results["status"] = "COMPLETE"
            results["message"] = "✓ Full integration cycle complete - Sovereignty achieved"
        else:
            results["status"] = "INCOMPLETE"
            results["message"] = "⚠ Integration cycle incomplete"
        
        results["validations"] = validation_results
        results["waltz"] = waltz_result
        results["integrated_validation"] = {
            "status": integrated_validation.status,
            "message": integrated_validation.message,
            "score": integrated_validation.overall_score
        }
        results["sovereignty"] = sovereignty
        
        return results
    
    def get_status(self) -> Dict[str, Any]:
        """
        Get current engine status.
        
        Returns:
            Dict with engine status and statistics
        """
        return {
            "sovereign": self._sovereign,
            "integrated_patterns": len(self._integrated_patterns),
            "subsystems": {
                "universal_laws": self.universal_laws is not None,
                "validator": self.validator is not None
            }
        }


def initialize_integration_engine() -> IntegrationEngine:
    """
    Initialize and activate Integration Engine.
    
    Returns:
        Activated IntegrationEngine instance
    """
    engine = IntegrationEngine()
    sovereignty = engine.verify_sovereignty()
    
    if sovereignty["sovereign"]:
        print("✓ Integration Engine activated and sovereign")
    else:
        print("✗ Integration Engine activation incomplete")
    
    return engine
