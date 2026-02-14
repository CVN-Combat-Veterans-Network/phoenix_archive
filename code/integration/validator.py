"""
Integration Validator

Validates three-pillar structure, triadic closure, and sovereignty status.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional


@dataclass
class ValidationReport:
    """
    Complete validation report for integration patterns.
    
    Contains results from all validation checks including:
    - Three-pillar structure validation
    - Triadic closure validation
    - Sovereignty status verification
    """
    status: str
    message: str
    pillar_validation: Dict[str, Any]
    triadic_validation: Dict[str, Any]
    sovereignty_validation: Dict[str, Any]
    overall_score: float
    recommendations: List[str] = field(default_factory=list)
    
    def __repr__(self) -> str:
        return f"ValidationReport(status={self.status}, score={self.overall_score:.2f})"


class IntegrationValidator:
    """
    Integration Validator for Three-Pillar Architecture.
    
    Validates that patterns conform to the three-pillar structure:
    - Phoenix: Identity formation (BEGIN mode)
    - Hydrogenesi: Cosmological propagation (EXTEND mode)
    - The Third: Threshold binding (HOLD mode)
    
    Also validates triadic closure and sovereignty status.
    """
    
    REQUIRED_PILLARS = ["Phoenix", "Hydrogenesi", "The Third"]
    PILLAR_MODES = {
        "Phoenix": "BEGIN",
        "Hydrogenesi": "EXTEND",
        "The Third": "HOLD"
    }
    
    def __init__(self):
        """Initialize Integration Validator."""
        pass
    
    def validate_pillar_structure(self, pattern: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate three-pillar structure.
        
        Checks that pattern engages all three pillars with correct modes.
        
        Args:
            pattern: Pattern to validate
            
        Returns:
            Validation result with pillar structure analysis
        """
        # Check for pillar engagement
        pillars_present = []
        pillar_details = {}
        
        # Analyze pattern structure for pillar markers
        if "triad" in pattern:
            triad = pattern["triad"]
            if isinstance(triad, dict):
                pillars_present = list(triad.keys())
                pillar_details = triad
        
        # Check for pillar field
        if "pillar" in pattern:
            single_pillar = pattern["pillar"]
            if single_pillar not in pillars_present:
                pillars_present.append(single_pillar)
                pillar_details[single_pillar] = pattern
        
        # Check for nested pillar references
        for pillar in self.REQUIRED_PILLARS:
            pillar_lower = pillar.lower()
            if pillar_lower in pattern or pillar in pattern:
                if pillar not in pillars_present:
                    pillars_present.append(pillar)
                    pillar_details[pillar] = pattern.get(pillar_lower) or pattern.get(pillar)
        
        # Validate pillar presence
        missing_pillars = [p for p in self.REQUIRED_PILLARS if p not in pillars_present]
        
        if not missing_pillars:
            return {
                "valid": True,
                "message": "✓ All three pillars engaged",
                "pillars_present": pillars_present,
                "pillar_details": pillar_details,
                "missing_pillars": []
            }
        elif len(pillars_present) >= 2:
            return {
                "valid": False,
                "message": f"⚠ {len(pillars_present)}/3 pillars present",
                "pillars_present": pillars_present,
                "pillar_details": pillar_details,
                "missing_pillars": missing_pillars
            }
        else:
            return {
                "valid": False,
                "message": f"✗ Insufficient pillars ({len(pillars_present)}/3)",
                "pillars_present": pillars_present,
                "pillar_details": pillar_details,
                "missing_pillars": missing_pillars
            }
    
    def validate_triadic_closure(self, pattern: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate triadic closure.
        
        Checks that pattern has achieved three-way binding and closure.
        
        Args:
            pattern: Pattern to validate
            
        Returns:
            Validation result with closure analysis
        """
        # Check closure markers
        closed = pattern.get("closed", False)
        triadic_closure = pattern.get("triadic_closure", False)
        waltz_complete = pattern.get("waltz_complete", False)
        
        # Check for triad structure
        has_triad = "triad" in pattern
        triad_complete = False
        if has_triad:
            triad = pattern["triad"]
            if isinstance(triad, dict):
                triad_complete = len(triad) >= 3
            elif isinstance(triad, (list, tuple)):
                triad_complete = len(triad) >= 3
        
        # Determine closure status
        closure_confirmed = (
            closed or 
            triadic_closure or 
            waltz_complete or 
            triad_complete
        )
        
        if closure_confirmed:
            return {
                "valid": True,
                "message": "✓ Triadic closure achieved",
                "closed": True,
                "indicators": {
                    "closed_flag": closed,
                    "triadic_closure_flag": triadic_closure,
                    "waltz_complete": waltz_complete,
                    "triad_structure": triad_complete
                }
            }
        else:
            return {
                "valid": False,
                "message": "✗ Triadic closure incomplete",
                "closed": False,
                "indicators": {
                    "closed_flag": closed,
                    "triadic_closure_flag": triadic_closure,
                    "waltz_complete": waltz_complete,
                    "triad_structure": triad_complete
                }
            }
    
    def validate_sovereignty(self, pattern: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate sovereignty status.
        
        Checks that pattern has achieved sovereign status through
        proper integration and closure.
        
        Args:
            pattern: Pattern to validate
            
        Returns:
            Validation result with sovereignty analysis
        """
        # Check sovereignty markers
        sovereignty = pattern.get("sovereignty", False)
        sovereignty_confirmed = pattern.get("sovereignty_confirmed", False)
        stable = pattern.get("stable", False)
        
        # Check for apex (sovereignty indicator)
        has_apex = "apex" in pattern
        
        # Check integration completeness
        integrated = pattern.get("integrated", False)
        waltz_complete = pattern.get("waltz_complete", False)
        
        # Determine sovereignty status
        sovereignty_achieved = (
            sovereignty or 
            sovereignty_confirmed or 
            (stable and has_apex and waltz_complete)
        )
        
        if sovereignty_achieved:
            return {
                "valid": True,
                "message": "✓ Sovereignty confirmed",
                "sovereign": True,
                "indicators": {
                    "sovereignty_flag": sovereignty,
                    "sovereignty_confirmed": sovereignty_confirmed,
                    "stable": stable,
                    "has_apex": has_apex,
                    "integrated": integrated,
                    "waltz_complete": waltz_complete
                }
            }
        elif integrated or stable:
            return {
                "valid": False,
                "message": "⚠ Sovereignty emerging but not confirmed",
                "sovereign": False,
                "indicators": {
                    "sovereignty_flag": sovereignty,
                    "sovereignty_confirmed": sovereignty_confirmed,
                    "stable": stable,
                    "has_apex": has_apex,
                    "integrated": integrated,
                    "waltz_complete": waltz_complete
                }
            }
        else:
            return {
                "valid": False,
                "message": "✗ Sovereignty not achieved",
                "sovereign": False,
                "indicators": {
                    "sovereignty_flag": sovereignty,
                    "sovereignty_confirmed": sovereignty_confirmed,
                    "stable": stable,
                    "has_apex": has_apex,
                    "integrated": integrated,
                    "waltz_complete": waltz_complete
                }
            }
    
    def generate_report(self, pattern: Dict[str, Any]) -> ValidationReport:
        """
        Generate complete validation report.
        
        Performs all validations and produces comprehensive report.
        
        Args:
            pattern: Pattern to validate
            
        Returns:
            ValidationReport with complete analysis
        """
        # Run all validations
        pillar_result = self.validate_pillar_structure(pattern)
        triadic_result = self.validate_triadic_closure(pattern)
        sovereignty_result = self.validate_sovereignty(pattern)
        
        # Calculate overall score
        scores = []
        if pillar_result["valid"]:
            scores.append(1.0)
        else:
            pillar_count = len(pillar_result.get("pillars_present", []))
            scores.append(pillar_count / 3.0)
        
        scores.append(1.0 if triadic_result["valid"] else 0.0)
        scores.append(1.0 if sovereignty_result["valid"] else 0.0)
        
        overall_score = sum(scores) / len(scores)
        
        # Determine status
        if overall_score >= 1.0:
            status = "SOVEREIGN"
            message = "✓ Pattern is fully sovereign"
        elif overall_score >= 0.75:
            status = "STABLE"
            message = "⚠ Pattern is stable but not fully sovereign"
        elif overall_score >= 0.5:
            status = "EMERGING"
            message = "⚠ Pattern is emerging but incomplete"
        else:
            status = "UNSTABLE"
            message = "✗ Pattern is unstable"
        
        # Generate recommendations
        recommendations = []
        if not pillar_result["valid"]:
            missing = pillar_result.get("missing_pillars", [])
            if missing:
                recommendations.append(f"Engage missing pillars: {', '.join(missing)}")
        
        if not triadic_result["valid"]:
            recommendations.append("Complete triadic closure through Three-Finger Waltz")
        
        if not sovereignty_result["valid"]:
            recommendations.append("Achieve sovereignty through full integration cycle")
        
        return ValidationReport(
            status=status,
            message=message,
            pillar_validation=pillar_result,
            triadic_validation=triadic_result,
            sovereignty_validation=sovereignty_result,
            overall_score=overall_score,
            recommendations=recommendations
        )
    
    def quick_check(self, pattern: Dict[str, Any]) -> Dict[str, Any]:
        """
        Quick validation check.
        
        Returns simplified validation result without full report.
        
        Args:
            pattern: Pattern to validate
            
        Returns:
            Dict with status and message
        """
        report = self.generate_report(pattern)
        return {
            "status": report.status,
            "message": report.message,
            "score": report.overall_score
        }
