"""
Universal Laws Framework - 12 Laws for Integration Validation

The Twelve Laws govern pattern formation across all three pillars:
- Substrate Laws (4): Foundation patterns
- Universal Laws (4): Cross-pillar coherence
- Apex Laws (4): Sovereignty validation
"""

from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Any, Optional


class LawStatus(Enum):
    """Status of law validation check."""
    SATISFIED = "satisfied"
    VIOLATED = "violated"
    PARTIAL = "partial"


@dataclass
class LawCheckResult:
    """Result of a single law validation check."""
    law_name: str
    status: LawStatus
    message: str
    details: Dict[str, Any]


class UniversalLaws:
    """
    The Twelve Universal Laws for Integration Validation.
    
    Substrate Laws (4):
    1. Universal Triad Law - three-way correspondence
    2. Recursion Depth Law - bounded at depth 7
    3. Self-Similarity Threshold - golden ratio bounds (0.618-1.618)
    4. Convergence Envelope - bounded recursion domain
    
    Universal Laws (4):
    5. Apex Fixed-Point Proof - ultimate attractor exists
    6. Recursive Stability Band - safe recursion zones
    7. Sigil Embedding Ratio - golden ratio constraint (φ = 1.618)
    8. Cross-Pillar Coherence - 80% coherence threshold
    
    Apex Laws (4):
    9. Operator Composition - minimum 3 operators
    10. Threshold Mechanics - bifurcation management
    11. Invariant Preservation - identity maintained
    12. Triadic Closure - three-way binding complete
    """
    
    # Constants for law validation
    MAX_RECURSION_DEPTH = 7
    GOLDEN_RATIO = 1.618  # Used for sigil embedding validation
    GOLDEN_RATIO_LOWER = 0.618
    GOLDEN_RATIO_UPPER = 1.618
    COHERENCE_THRESHOLD = 0.80
    MIN_OPERATORS = 3
    
    # ============================================================================
    # SUBSTRATE LAWS (4)
    # ============================================================================
    
    def check_universal_triad(self, pattern: Dict[str, Any]) -> LawCheckResult:
        """
        Law 1: Universal Triad Law
        
        Every stable pattern must exhibit three-way correspondence.
        Pattern must have: tension pair + stabilizer → triad
        
        Args:
            pattern: Pattern to validate
            
        Returns:
            LawCheckResult with validation status
        """
        structure = pattern.get("structure", {})
        
        # Check for triad or three-element structure
        has_triad = "triad" in structure
        has_three_elements = len(structure.get("elements", [])) >= 3
        has_tension_and_stabilizer = (
            "tension_pair" in structure and 
            "stabilizer" in structure
        )
        
        if has_triad or (has_three_elements and has_tension_and_stabilizer):
            return LawCheckResult(
                law_name="Universal Triad Law",
                status=LawStatus.SATISFIED,
                message="✓ Three-way correspondence confirmed",
                details={
                    "triad_present": has_triad,
                    "three_elements": has_three_elements,
                    "structure": structure
                }
            )
        elif has_three_elements:
            return LawCheckResult(
                law_name="Universal Triad Law",
                status=LawStatus.PARTIAL,
                message="⚠ Three elements present but structure incomplete",
                details={"structure": structure}
            )
        else:
            return LawCheckResult(
                law_name="Universal Triad Law",
                status=LawStatus.VIOLATED,
                message="✗ Three-way correspondence missing",
                details={"structure": structure}
            )
    
    def check_recursion_depth(self, pattern: Dict[str, Any]) -> LawCheckResult:
        """
        Law 2: Recursion Depth Law
        
        Recursion must be bounded at depth 7.
        Beyond depth 7, patterns lose coherence.
        
        Args:
            pattern: Pattern to validate
            
        Returns:
            LawCheckResult with validation status
        """
        depth = pattern.get("recursion_depth", 0)
        
        if depth <= self.MAX_RECURSION_DEPTH:
            return LawCheckResult(
                law_name="Recursion Depth Law",
                status=LawStatus.SATISFIED,
                message=f"✓ Recursion depth {depth} ≤ {self.MAX_RECURSION_DEPTH}",
                details={"depth": depth, "max_depth": self.MAX_RECURSION_DEPTH}
            )
        else:
            return LawCheckResult(
                law_name="Recursion Depth Law",
                status=LawStatus.VIOLATED,
                message=f"✗ Recursion depth {depth} exceeds maximum {self.MAX_RECURSION_DEPTH}",
                details={"depth": depth, "max_depth": self.MAX_RECURSION_DEPTH}
            )
    
    def check_self_similarity(self, pattern: Dict[str, Any]) -> LawCheckResult:
        """
        Law 3: Self-Similarity Threshold
        
        Pattern ratios must fall within golden ratio bounds (0.618-1.618).
        This ensures harmonic self-similarity across scales.
        
        Args:
            pattern: Pattern to validate
            
        Returns:
            LawCheckResult with validation status
        """
        ratio = pattern.get("similarity_ratio", 1.0)
        
        if self.GOLDEN_RATIO_LOWER <= ratio <= self.GOLDEN_RATIO_UPPER:
            return LawCheckResult(
                law_name="Self-Similarity Threshold",
                status=LawStatus.SATISFIED,
                message=f"✓ Ratio {ratio:.3f} within golden bounds [{self.GOLDEN_RATIO_LOWER}-{self.GOLDEN_RATIO_UPPER}]",
                details={"ratio": ratio, "bounds": (self.GOLDEN_RATIO_LOWER, self.GOLDEN_RATIO_UPPER)}
            )
        else:
            return LawCheckResult(
                law_name="Self-Similarity Threshold",
                status=LawStatus.VIOLATED,
                message=f"✗ Ratio {ratio:.3f} outside golden bounds",
                details={"ratio": ratio, "bounds": (self.GOLDEN_RATIO_LOWER, self.GOLDEN_RATIO_UPPER)}
            )
    
    def check_convergence_envelope(self, pattern: Dict[str, Any]) -> LawCheckResult:
        """
        Law 4: Convergence Envelope
        
        Recursion must converge within bounded domain.
        Pattern must show convergence markers.
        
        Args:
            pattern: Pattern to validate
            
        Returns:
            LawCheckResult with validation status
        """
        converges = pattern.get("converges", False)
        convergence_point = pattern.get("convergence_point")
        
        if converges and convergence_point is not None:
            return LawCheckResult(
                law_name="Convergence Envelope",
                status=LawStatus.SATISFIED,
                message="✓ Pattern converges within bounded domain",
                details={"converges": True, "convergence_point": convergence_point}
            )
        elif converges:
            return LawCheckResult(
                law_name="Convergence Envelope",
                status=LawStatus.PARTIAL,
                message="⚠ Convergence claimed but point undefined",
                details={"converges": True, "convergence_point": None}
            )
        else:
            return LawCheckResult(
                law_name="Convergence Envelope",
                status=LawStatus.VIOLATED,
                message="✗ Pattern does not converge",
                details={"converges": False}
            )
    
    # ============================================================================
    # UNIVERSAL LAWS (4)
    # ============================================================================
    
    def check_apex_fixed_point(self, pattern: Dict[str, Any]) -> LawCheckResult:
        """
        Law 5: Apex Fixed-Point Proof
        
        Every recursion must have an ultimate attractor (apex).
        Pattern must define its apex state.
        
        Args:
            pattern: Pattern to validate
            
        Returns:
            LawCheckResult with validation status
        """
        has_apex = "apex" in pattern
        apex_value = pattern.get("apex")
        
        if has_apex and apex_value is not None:
            return LawCheckResult(
                law_name="Apex Fixed-Point Proof",
                status=LawStatus.SATISFIED,
                message="✓ Apex attractor defined",
                details={"apex": apex_value}
            )
        else:
            return LawCheckResult(
                law_name="Apex Fixed-Point Proof",
                status=LawStatus.VIOLATED,
                message="✗ No apex attractor defined",
                details={"apex": None}
            )
    
    def check_recursive_stability(self, pattern: Dict[str, Any]) -> LawCheckResult:
        """
        Law 6: Recursive Stability Band
        
        Safe recursion zones must be defined and maintained.
        Pattern must operate within stability band.
        
        Args:
            pattern: Pattern to validate
            
        Returns:
            LawCheckResult with validation status
        """
        stable = pattern.get("stable", False)
        stability_score = pattern.get("stability_score", 0.0)
        
        if stable and stability_score >= 0.5:
            return LawCheckResult(
                law_name="Recursive Stability Band",
                status=LawStatus.SATISFIED,
                message=f"✓ Pattern stable (score: {stability_score:.2f})",
                details={"stable": True, "stability_score": stability_score}
            )
        elif stable:
            return LawCheckResult(
                law_name="Recursive Stability Band",
                status=LawStatus.PARTIAL,
                message=f"⚠ Pattern stable but low score ({stability_score:.2f})",
                details={"stable": True, "stability_score": stability_score}
            )
        else:
            return LawCheckResult(
                law_name="Recursive Stability Band",
                status=LawStatus.VIOLATED,
                message="✗ Pattern unstable",
                details={"stable": False, "stability_score": stability_score}
            )
    
    def check_sigil_embedding(self, pattern: Dict[str, Any]) -> LawCheckResult:
        """
        Law 7: Sigil Embedding Ratio
        
        Pattern structure must follow golden ratio (φ = 1.618).
        This ensures optimal information density.
        
        Args:
            pattern: Pattern to validate
            
        Returns:
            LawCheckResult with validation status
        """
        embedding_ratio = pattern.get("embedding_ratio", 1.0)
        tolerance = 0.1
        
        if abs(embedding_ratio - self.GOLDEN_RATIO) <= tolerance:
            return LawCheckResult(
                law_name="Sigil Embedding Ratio",
                status=LawStatus.SATISFIED,
                message=f"✓ Embedding ratio {embedding_ratio:.3f} ≈ φ ({self.GOLDEN_RATIO})",
                details={"ratio": embedding_ratio, "golden_ratio": self.GOLDEN_RATIO}
            )
        else:
            return LawCheckResult(
                law_name="Sigil Embedding Ratio",
                status=LawStatus.VIOLATED,
                message=f"✗ Embedding ratio {embedding_ratio:.3f} deviates from φ",
                details={"ratio": embedding_ratio, "golden_ratio": self.GOLDEN_RATIO}
            )
    
    def check_cross_pillar_coherence(self, pattern: Dict[str, Any]) -> LawCheckResult:
        """
        Law 8: Cross-Pillar Coherence
        
        Pattern must maintain 80% coherence across pillars.
        Coherence below threshold indicates fragmentation.
        
        Args:
            pattern: Pattern to validate
            
        Returns:
            LawCheckResult with validation status
        """
        coherence = pattern.get("coherence", 1.0)
        
        if coherence >= self.COHERENCE_THRESHOLD:
            return LawCheckResult(
                law_name="Cross-Pillar Coherence",
                status=LawStatus.SATISFIED,
                message=f"✓ Coherence {coherence:.2%} ≥ {self.COHERENCE_THRESHOLD:.0%}",
                details={"coherence": coherence, "threshold": self.COHERENCE_THRESHOLD}
            )
        elif coherence >= self.COHERENCE_THRESHOLD * 0.7:
            return LawCheckResult(
                law_name="Cross-Pillar Coherence",
                status=LawStatus.PARTIAL,
                message=f"⚠ Coherence {coherence:.2%} below threshold",
                details={"coherence": coherence, "threshold": self.COHERENCE_THRESHOLD}
            )
        else:
            return LawCheckResult(
                law_name="Cross-Pillar Coherence",
                status=LawStatus.VIOLATED,
                message=f"✗ Coherence {coherence:.2%} critically low",
                details={"coherence": coherence, "threshold": self.COHERENCE_THRESHOLD}
            )
    
    # ============================================================================
    # APEX LAWS (4)
    # ============================================================================
    
    def check_operator_composition(self, pattern: Dict[str, Any]) -> LawCheckResult:
        """
        Law 9: Operator Composition
        
        Sovereign patterns must compose at least 3 operators.
        This ensures sufficient complexity for emergence.
        
        Args:
            pattern: Pattern to validate
            
        Returns:
            LawCheckResult with validation status
        """
        operators = pattern.get("operators", [])
        operator_count = len(operators)
        
        if operator_count >= self.MIN_OPERATORS:
            return LawCheckResult(
                law_name="Operator Composition",
                status=LawStatus.SATISFIED,
                message=f"✓ {operator_count} operators (≥ {self.MIN_OPERATORS})",
                details={"operator_count": operator_count, "operators": operators}
            )
        else:
            return LawCheckResult(
                law_name="Operator Composition",
                status=LawStatus.VIOLATED,
                message=f"✗ Only {operator_count} operators (need ≥ {self.MIN_OPERATORS})",
                details={"operator_count": operator_count, "operators": operators}
            )
    
    def check_threshold_mechanics(self, pattern: Dict[str, Any]) -> LawCheckResult:
        """
        Law 10: Threshold Mechanics
        
        Bifurcation thresholds must be properly managed.
        Pattern must handle threshold transitions gracefully.
        
        Args:
            pattern: Pattern to validate
            
        Returns:
            LawCheckResult with validation status
        """
        has_threshold = "threshold" in pattern
        threshold_managed = pattern.get("threshold_managed", False)
        
        if has_threshold and threshold_managed:
            return LawCheckResult(
                law_name="Threshold Mechanics",
                status=LawStatus.SATISFIED,
                message="✓ Threshold properly managed",
                details={"threshold": pattern.get("threshold"), "managed": True}
            )
        elif has_threshold:
            return LawCheckResult(
                law_name="Threshold Mechanics",
                status=LawStatus.PARTIAL,
                message="⚠ Threshold present but management unclear",
                details={"threshold": pattern.get("threshold"), "managed": False}
            )
        else:
            # No threshold required - consider satisfied
            return LawCheckResult(
                law_name="Threshold Mechanics",
                status=LawStatus.SATISFIED,
                message="✓ No threshold management required",
                details={"threshold": None, "managed": True}
            )
    
    def check_invariant_preservation(self, pattern: Dict[str, Any]) -> LawCheckResult:
        """
        Law 11: Invariant Preservation
        
        Core identity must be maintained through transformations.
        Pattern must preserve essential invariants.
        
        Args:
            pattern: Pattern to validate
            
        Returns:
            LawCheckResult with validation status
        """
        has_invariant = "invariant" in pattern
        invariant_preserved = pattern.get("invariant_preserved", False)
        
        if has_invariant and invariant_preserved:
            return LawCheckResult(
                law_name="Invariant Preservation",
                status=LawStatus.SATISFIED,
                message="✓ Invariant preserved",
                details={"invariant": pattern.get("invariant"), "preserved": True}
            )
        elif has_invariant:
            return LawCheckResult(
                law_name="Invariant Preservation",
                status=LawStatus.VIOLATED,
                message="✗ Invariant violated",
                details={"invariant": pattern.get("invariant"), "preserved": False}
            )
        else:
            # No invariant defined - consider satisfied if pattern has identity
            has_identity = "identity" in pattern or "name" in pattern
            if has_identity:
                return LawCheckResult(
                    law_name="Invariant Preservation",
                    status=LawStatus.SATISFIED,
                    message="✓ Identity maintained",
                    details={"identity": pattern.get("identity") or pattern.get("name")}
                )
            else:
                return LawCheckResult(
                    law_name="Invariant Preservation",
                    status=LawStatus.PARTIAL,
                    message="⚠ No explicit invariant or identity",
                    details={}
                )
    
    def check_triadic_closure(self, pattern: Dict[str, Any]) -> LawCheckResult:
        """
        Law 12: Triadic Closure
        
        Three-way binding must be complete and irreversible.
        Pattern must achieve sovereign closure.
        
        Args:
            pattern: Pattern to validate
            
        Returns:
            LawCheckResult with validation status
        """
        closed = pattern.get("closed", False)
        sovereignty = pattern.get("sovereignty", False)
        
        if closed and sovereignty:
            return LawCheckResult(
                law_name="Triadic Closure",
                status=LawStatus.SATISFIED,
                message="✓ Triadic closure achieved, sovereignty confirmed",
                details={"closed": True, "sovereignty": True}
            )
        elif closed:
            return LawCheckResult(
                law_name="Triadic Closure",
                status=LawStatus.PARTIAL,
                message="⚠ Closure achieved but sovereignty uncertain",
                details={"closed": True, "sovereignty": False}
            )
        else:
            return LawCheckResult(
                law_name="Triadic Closure",
                status=LawStatus.VIOLATED,
                message="✗ Triadic closure incomplete",
                details={"closed": False, "sovereignty": False}
            )
    
    # ============================================================================
    # VALIDATION METHODS
    # ============================================================================
    
    def validate_all(self, pattern: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate pattern against all 12 Universal Laws.
        
        Args:
            pattern: Pattern to validate
            
        Returns:
            Validation results with status and law check details
        """
        # Execute all law checks
        results = [
            # Substrate Laws
            self.check_universal_triad(pattern),
            self.check_recursion_depth(pattern),
            self.check_self_similarity(pattern),
            self.check_convergence_envelope(pattern),
            # Universal Laws
            self.check_apex_fixed_point(pattern),
            self.check_recursive_stability(pattern),
            self.check_sigil_embedding(pattern),
            self.check_cross_pillar_coherence(pattern),
            # Apex Laws
            self.check_operator_composition(pattern),
            self.check_threshold_mechanics(pattern),
            self.check_invariant_preservation(pattern),
            self.check_triadic_closure(pattern),
        ]
        
        # Count status types
        satisfied = sum(1 for r in results if r.status == LawStatus.SATISFIED)
        violated = sum(1 for r in results if r.status == LawStatus.VIOLATED)
        partial = sum(1 for r in results if r.status == LawStatus.PARTIAL)
        
        # Determine overall status
        if violated == 0 and partial == 0:
            status = "SOVEREIGN"
            message = "✓ All 12 Universal Laws satisfied - Pattern is SOVEREIGN"
        elif violated == 0:
            status = "STABLE"
            message = f"⚠ {satisfied} laws satisfied, {partial} partial - Pattern is STABLE"
        elif violated <= 2:
            status = "UNSTABLE"
            message = f"⚠ {violated} laws violated - Pattern is UNSTABLE"
        else:
            status = "INVALID"
            message = f"✗ {violated} laws violated - Pattern is INVALID"
        
        return {
            "status": status,
            "message": message,
            "summary": {
                "satisfied": satisfied,
                "partial": partial,
                "violated": violated,
                "total": 12
            },
            "law_results": [
                {
                    "law": r.law_name,
                    "status": r.status.value,
                    "message": r.message,
                    "details": r.details
                }
                for r in results
            ]
        }
