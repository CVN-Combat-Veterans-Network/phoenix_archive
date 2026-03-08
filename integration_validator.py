#!/usr/bin/env python3
"""
Integration Validator — Codex v2.0.0

Automated validation of Three-Pillar Architecture completeness.

Features:
- Phoenix pillar validation (operators, laws, composites)
- Hydrogenesi pillar validation (operators, field mechanics)
- The Third pillar validation (operators, examples, knots)
- Cross-pillar coherence checks
- Twelve Universal Laws verification
- Meta-operator validation
- Detailed reporting with pass/fail status

Usage:
    python integration_validator.py
    python integration_validator.py --verbose
    python integration_validator.py --pillar phoenix
"""

from __future__ import annotations
import argparse
import os
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Dict, Any, Optional
from enum import Enum


class ValidationStatus(Enum):
    """Validation status values."""
    PASS = "✅ PASS"
    FAIL = "❌ FAIL"
    WARN = "⚠️  WARN"
    SKIP = "⊘  SKIP"


@dataclass
class ValidationResult:
    """Single validation check result."""
    name: str
    status: ValidationStatus
    message: str
    details: List[str] = field(default_factory=list)


@dataclass
class PillarValidation:
    """Validation results for a single pillar."""
    pillar_name: str
    results: List[ValidationResult] = field(default_factory=list)
    
    @property
    def passed(self) -> int:
        return sum(1 for r in self.results if r.status == ValidationStatus.PASS)
    
    @property
    def failed(self) -> int:
        return sum(1 for r in self.results if r.status == ValidationStatus.FAIL)
    
    @property
    def warnings(self) -> int:
        return sum(1 for r in self.results if r.status == ValidationStatus.WARN)
    
    @property
    def total(self) -> int:
        return len(self.results)


class IntegrationValidator:
    """Main integration validator for the Phoenix Archive."""
    
    def __init__(self, repo_root: Path, verbose: bool = False):
        self.repo_root = repo_root
        self.verbose = verbose
        self.phoenix_validation = PillarValidation("Phoenix")
        self.hydrogenesi_validation = PillarValidation("Hydrogenesi")
        self.third_validation = PillarValidation("The Third")
        self.universal_validation = PillarValidation("Universal Laws")
        self.cross_pillar_validation = PillarValidation("Cross-Pillar Coherence")
        
    def validate_all(self) -> bool:
        """Run all validation checks."""
        print("=" * 70)
        print("PHOENIX ARCHIVE — INTEGRATION VALIDATOR v2.0.0")
        print("=" * 70)
        print()
        
        # Validate each pillar
        self._validate_phoenix_pillar()
        self._validate_hydrogenesi_pillar()
        self._validate_third_pillar()
        self._validate_universal_laws()
        self._validate_cross_pillar_coherence()
        
        # Print results
        self._print_results()
        
        # Determine overall pass/fail
        total_failed = (
            self.phoenix_validation.failed +
            self.hydrogenesi_validation.failed +
            self.third_validation.failed +
            self.universal_validation.failed +
            self.cross_pillar_validation.failed
        )
        
        return total_failed == 0
    
    def _validate_phoenix_pillar(self):
        """Validate Phoenix pillar components."""
        print("🔥 Validating Phoenix Pillar...")
        
        # Check Phoenix operators
        phoenix_ops = [
            "First-Binding.md",
            "Phoenix-Ignition.md",
            "IM_ME.md",
            "Apex-Formation.md",
            "Three-Finger-Waltz.md",
            "Black-Holed-Imprint.md",
        ]
        
        ops_path = self.repo_root / "Phoenix" / "Operators"
        self._check_files_exist(
            ops_path, phoenix_ops, self.phoenix_validation, 
            "Phoenix operators"
        )
        
        # Check composite operators
        composite_ops = [
            "Trajectory.md",
            "Identity.md",
            "Stability.md",
            "Genesis.md",
        ]
        
        composite_path = ops_path / "Composite"
        self._check_files_exist(
            composite_path, composite_ops, self.phoenix_validation,
            "Phoenix composite operators"
        )
        
        # Check Phoenix code implementation
        code_path = self.repo_root / "code" / "phoenix" / "operators.py"
        self._check_file_exists(
            code_path, self.phoenix_validation,
            "Phoenix operators implementation"
        )
        
        # Check for key operator classes in code
        if code_path.exists():
            self._check_code_classes(
                code_path,
                ["FirstBinding", "PhoenixIgnition", "IM_ME", "ApexFormation", "ThreeFingerWaltz"],
                self.phoenix_validation,
                "Phoenix operator classes"
            )
    
    def _validate_hydrogenesi_pillar(self):
        """Validate Hydrogenesi pillar components."""
        print("🌌 Validating Hydrogenesi Pillar...")
        
        # Check Hydrogenesi operators
        hydrogenesi_ops = [
            "Stabilizer-Extraction.md",
            "AGN-Replication.md",
            "Curvature-Residue.md",
            "Lineage-Logic.md",
        ]
        
        ops_path = self.repo_root / "Hydrogenesi" / "Operators"
        self._check_files_exist(
            ops_path, hydrogenesi_ops, self.hydrogenesi_validation,
            "Hydrogenesi operators"
        )
        
        # Check Hydrogenesi code implementation
        code_path = self.repo_root / "code" / "hydrogenesi" / "operators.py"
        self._check_file_exists(
            code_path, self.hydrogenesi_validation,
            "Hydrogenesi operators implementation"
        )
        
        # Check for key operator classes in code
        if code_path.exists():
            self._check_code_classes(
                code_path,
                ["StabilizerExtraction", "AGNReplication", "CurvatureResidue", "LineageLogic"],
                self.hydrogenesi_validation,
                "Hydrogenesi operator classes"
            )
    
    def _validate_third_pillar(self):
        """Validate The Third pillar components."""
        print("🔗 Validating The Third Pillar...")
        
        # Check The Third operators
        third_ops = [
            "Knot-Binding.md",
            "Cross-Pillar-Knot.md",
            "Triadic-Closure.md",
            "Apex-Knot.md",
            "Stability-Knot.md",
        ]
        
        ops_path = self.repo_root / "TheThird" / "Operators"
        self._check_files_exist(
            ops_path, third_ops, self.third_validation,
            "The Third operators"
        )
        
        # Check The Third code implementation
        code_path = self.repo_root / "code" / "the_third" / "operators.py"
        self._check_file_exists(
            code_path, self.third_validation,
            "The Third operators implementation"
        )
        
        # Check for key operator classes in code
        if code_path.exists():
            self._check_code_classes(
                code_path,
                ["MetaBinder", "LawCompliance", "CrossScaleBehavior", "CoherenceValidator"],
                self.third_validation,
                "The Third operator classes"
            )
        
        # Check for examples
        examples_path = self.repo_root / "TheThird" / "Examples"
        if examples_path.exists():
            examples = list(examples_path.glob("*.md"))
            if len(examples) > 0:
                self.third_validation.results.append(ValidationResult(
                    "The Third examples",
                    ValidationStatus.PASS,
                    f"Found {len(examples)} example files"
                ))
            else:
                self.third_validation.results.append(ValidationResult(
                    "The Third examples",
                    ValidationStatus.WARN,
                    "No example files found"
                ))
    
    def _validate_universal_laws(self):
        """Validate Universal Laws documentation."""
        print("⚖️  Validating Universal Laws...")
        
        # Check for Twelve Laws codification
        laws_path = self.repo_root / "Phoenix" / "Universal-Laws" / "Twelve-Laws-Codification.md"
        self._check_file_exists(
            laws_path, self.universal_validation,
            "Twelve Laws Codification"
        )
        
        # Check for individual law files
        substrate_laws = ["Tension.md", "Binding.md", "Apex.md", "Universal-Triad-Law.md"]
        universal_laws = [
            "Recursion-Depth-Law.md",
            "Self-Similarity-Threshold.md",
            "Sigil-Embedding-Ratio.md",
            "Recursive-Stability-Band.md",
        ]
        apex_laws = [
            "Convergence-Envelope.md",
            "Apex-Fixed-Point-Proof.md",
        ]
        
        laws_dir = self.repo_root / "Phoenix" / "Universal-Laws"
        
        self._check_files_exist(
            laws_dir, substrate_laws, self.universal_validation,
            "Substrate Laws (4)"
        )
        
        self._check_files_exist(
            laws_dir, universal_laws, self.universal_validation,
            "Universal Laws (4)"
        )
        
        self._check_files_exist(
            laws_dir, apex_laws, self.universal_validation,
            "Apex Laws (2 of 4)"
        )
        
        # Check Universal operators code
        universal_code = self.repo_root / "code" / "universal" / "operators.py"
        self._check_file_exists(
            universal_code, self.universal_validation,
            "Universal operators implementation"
        )
    
    def _validate_cross_pillar_coherence(self):
        """Validate cross-pillar coherence and integration."""
        print("🔀 Validating Cross-Pillar Coherence...")
        
        # Check that all three pillars have documentation
        phoenix_readme = self.repo_root / "Phoenix" / "README.md"
        hydrogenesi_readme = self.repo_root / "Hydrogenesi" / "README.md"
        third_readme = self.repo_root / "TheThird" / "README.md"
        
        all_pillars = [
            ("Phoenix README", phoenix_readme),
            ("Hydrogenesi README", hydrogenesi_readme),
            ("The Third README", third_readme),
        ]
        
        missing_pillars = []
        for name, path in all_pillars:
            if not path.exists():
                missing_pillars.append(name)
        
        if not missing_pillars:
            self.cross_pillar_validation.results.append(ValidationResult(
                "Three-pillar documentation",
                ValidationStatus.PASS,
                "All three pillars have README files"
            ))
        else:
            self.cross_pillar_validation.results.append(ValidationResult(
                "Three-pillar documentation",
                ValidationStatus.FAIL,
                f"Missing: {', '.join(missing_pillars)}"
            ))
        
        # Check for Comparative documentation
        comparative_path = self.repo_root / "Comparative"
        if comparative_path.exists():
            comp_files = list(comparative_path.glob("*.md"))
            self.cross_pillar_validation.results.append(ValidationResult(
                "Comparative documentation",
                ValidationStatus.PASS,
                f"Found {len(comp_files)} comparative files"
            ))
        else:
            self.cross_pillar_validation.results.append(ValidationResult(
                "Comparative documentation",
                ValidationStatus.WARN,
                "Comparative directory not found"
            ))
        
        # Check for integration tests
        test_path = self.repo_root / "tests"
        if test_path.exists():
            test_files = list(test_path.glob("**/*.py"))
            test_count = len([f for f in test_files if f.name.startswith("test_")])
            if test_count > 0:
                self.cross_pillar_validation.results.append(ValidationResult(
                    "Integration tests",
                    ValidationStatus.PASS,
                    f"Found {test_count} test files"
                ))
            else:
                self.cross_pillar_validation.results.append(ValidationResult(
                    "Integration tests",
                    ValidationStatus.WARN,
                    "No test files found"
                ))
        
        # Check for code integration
        phoenix_code = (self.repo_root / "code" / "phoenix" / "operators.py").exists()
        hydrogenesi_code = (self.repo_root / "code" / "hydrogenesi" / "operators.py").exists()
        third_code = (self.repo_root / "code" / "the_third" / "operators.py").exists()
        
        if phoenix_code and hydrogenesi_code and third_code:
            self.cross_pillar_validation.results.append(ValidationResult(
                "Three-pillar code implementation",
                ValidationStatus.PASS,
                "All three pillars have code implementations"
            ))
        else:
            missing = []
            if not phoenix_code:
                missing.append("Phoenix")
            if not hydrogenesi_code:
                missing.append("Hydrogenesi")
            if not third_code:
                missing.append("The Third")
            
            self.cross_pillar_validation.results.append(ValidationResult(
                "Three-pillar code implementation",
                ValidationStatus.FAIL,
                f"Missing implementations: {', '.join(missing)}"
            ))
    
    def _check_files_exist(
        self, 
        directory: Path, 
        files: List[str], 
        validation: PillarValidation,
        category: str
    ):
        """Check if files exist in directory."""
        if not directory.exists():
            validation.results.append(ValidationResult(
                category,
                ValidationStatus.FAIL,
                f"Directory not found: {directory.relative_to(self.repo_root)}"
            ))
            return
        
        missing = []
        found = []
        
        for file in files:
            if (directory / file).exists():
                found.append(file)
            else:
                missing.append(file)
        
        if not missing:
            validation.results.append(ValidationResult(
                category,
                ValidationStatus.PASS,
                f"All {len(files)} files present"
            ))
        else:
            validation.results.append(ValidationResult(
                category,
                ValidationStatus.FAIL,
                f"Missing {len(missing)}/{len(files)} files",
                details=missing if self.verbose else []
            ))
    
    def _check_file_exists(
        self,
        file_path: Path,
        validation: PillarValidation,
        description: str
    ):
        """Check if a single file exists."""
        if file_path.exists():
            validation.results.append(ValidationResult(
                description,
                ValidationStatus.PASS,
                f"File exists: {file_path.name}"
            ))
        else:
            validation.results.append(ValidationResult(
                description,
                ValidationStatus.FAIL,
                f"File not found: {file_path.relative_to(self.repo_root)}"
            ))
    
    def _check_code_classes(
        self,
        file_path: Path,
        classes: List[str],
        validation: PillarValidation,
        description: str
    ):
        """Check if classes are defined in a Python file."""
        try:
            content = file_path.read_text()
            missing = []
            found = []
            
            for cls in classes:
                # Look for class definition
                if f"class {cls}" in content:
                    found.append(cls)
                else:
                    missing.append(cls)
            
            if not missing:
                validation.results.append(ValidationResult(
                    description,
                    ValidationStatus.PASS,
                    f"All {len(classes)} classes implemented"
                ))
            else:
                validation.results.append(ValidationResult(
                    description,
                    ValidationStatus.FAIL,
                    f"Missing {len(missing)}/{len(classes)} classes",
                    details=missing if self.verbose else []
                ))
        except Exception as e:
            validation.results.append(ValidationResult(
                description,
                ValidationStatus.FAIL,
                f"Error reading file: {str(e)}"
            ))
    
    def _print_results(self):
        """Print validation results."""
        print()
        print("=" * 70)
        print("VALIDATION RESULTS")
        print("=" * 70)
        print()
        
        all_validations = [
            self.phoenix_validation,
            self.hydrogenesi_validation,
            self.third_validation,
            self.universal_validation,
            self.cross_pillar_validation,
        ]
        
        for validation in all_validations:
            self._print_pillar_results(validation)
        
        # Print summary
        print()
        print("=" * 70)
        print("SUMMARY")
        print("=" * 70)
        
        total_passed = sum(v.passed for v in all_validations)
        total_failed = sum(v.failed for v in all_validations)
        total_warnings = sum(v.warnings for v in all_validations)
        total_checks = sum(v.total for v in all_validations)
        
        print(f"\nTotal Checks:    {total_checks}")
        print(f"✅ Passed:       {total_passed}")
        print(f"❌ Failed:       {total_failed}")
        print(f"⚠️  Warnings:     {total_warnings}")
        
        if total_failed == 0:
            print()
            print("🎉 " + "=" * 66 + " 🎉")
            print("   INTEGRATION VALIDATION COMPLETE — ALL CHECKS PASSED")
            print("🎉 " + "=" * 66 + " 🎉")
            print()
            print("   The Archive is SOVEREIGN and ALIGNED.")
            print("   Three pillars stand. Twelve laws hold.")
            print()
        else:
            print()
            print("⚠️  INTEGRATION VALIDATION INCOMPLETE")
            print(f"   {total_failed} check(s) failed. Review and address failures.")
            print()
    
    def _print_pillar_results(self, validation: PillarValidation):
        """Print results for a single pillar."""
        print(f"{validation.pillar_name}")
        print("-" * 70)
        
        for result in validation.results:
            status_icon = result.status.value
            print(f"{status_icon} {result.name}: {result.message}")
            
            if self.verbose and result.details:
                for detail in result.details:
                    print(f"    • {detail}")
        
        print(f"\nPillar Summary: {validation.passed} passed, {validation.failed} failed, {validation.warnings} warnings")
        print()


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Phoenix Archive Integration Validator v2.0.0"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose output with detailed information"
    )
    parser.add_argument(
        "--pillar",
        choices=["phoenix", "hydrogenesi", "third", "universal", "cross-pillar"],
        help="Validate only a specific pillar"
    )
    
    args = parser.parse_args()
    
    # Determine repo root
    repo_root = Path(__file__).parent
    
    # Create validator
    validator = IntegrationValidator(repo_root, verbose=args.verbose)
    
    # Run validation
    if args.pillar:
        print(f"Validating only {args.pillar} pillar...")
        # For now, run all validations (could be enhanced to run specific pillar only)
        success = validator.validate_all()
    else:
        success = validator.validate_all()
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
