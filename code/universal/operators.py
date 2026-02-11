from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import Optional, List


# Threshold constants for bifurcation logic
INTERNAL_PRESSURE_THRESHOLD = 0.7  # Above this: LIFE (split), Below: LIGHT (absorb)
PREMATURE_SPLIT_PRESSURE_THRESHOLD = 0.8  # Pressure threshold for premature split detection


class BifurcationVector(Enum):
    """The two possible outcomes of the Life-Light Bifurcation."""
    LIFE = "LIFE"  # Split: fragmentation and preservation
    LIGHT = "LIGHT"  # Absorb: integration and ascension


class BifurcationStatus(Enum):
    """Status values for bifurcation state queries."""
    LIFE = "LIFE"  # Split outcome occurred
    LIGHT = "LIGHT"  # Absorption outcome occurred
    NULL = "NULL"  # Premature split (failure state A)
    STALLED = "STALLED"  # Failed absorption (failure state B)
    FROZEN = "FROZEN"  # Threshold avoidance (failure state C)
    PENDING = "PENDING"  # Threshold not yet reached


@dataclass
class LifeLightBifurcation:
    """
    Universal Threshold Operator: Life-Light Bifurcation.
    
    Governs the fate of a fused seed at maximum confinement.
    
    At the Bifurcation Threshold:
    - If seed splits → LIFE Vector (solar system, core-sample)
    - If seed absorbs → LIGHT Vector (Massive Super Red Giant, helium replication)
    
    Threshold is absolute and encountered exactly once.
    """
    
    confinement_tension: float = 0.0  # 0.0 to 1.0, where 1.0 is maximum
    stabilizing_symmetry: float = 0.0  # 0.0 to 1.0, where 1.0 is at limit
    internal_pressure: float = 0.0  # 0.0 to 1.0+, ratio of internal tension to containment
    
    # State tracking
    _status: BifurcationStatus = BifurcationStatus.PENDING
    _vector: Optional[BifurcationVector] = None
    _bifurcated: bool = False
    
    def at_threshold(self) -> bool:
        """
        Check if the Bifurcation Threshold has been reached.
        
        Threshold is reached when ALL conditions are met:
        1. Confinement tension at maximum (≥ 1.0)
        2. Stabilizing symmetry at limit (≥ 1.0)
        3. Pressure cannot increase without transformation
        4. Seed identity becomes undecidable
        
        Returns:
            True if threshold reached, False otherwise
        """
        return (
            self.confinement_tension >= 1.0 and
            self.stabilizing_symmetry >= 1.0 and
            self.internal_pressure > 0.0
        )
    
    def bifurcate(self, force_vector: Optional[BifurcationVector] = None) -> dict:
        """
        Execute the bifurcation at the threshold.
        
        Determines whether the seed splits (LIFE) or absorbs (LIGHT) based on
        the relationship between internal pressure and containment.
        
        Args:
            force_vector: Optional forced outcome (for testing/ceremonial use)
        
        Returns:
            dict with 'vector', 'status', 'outcome', and 'signature' keys
        
        Raises:
            RuntimeError: If bifurcation called before threshold or after already bifurcated
        """
        if self._bifurcated:
            raise RuntimeError(
                "Bifurcation already occurred. This operator can only execute once."
            )
        
        if not self.at_threshold():
            # Check for failure states
            if self.confinement_tension < 1.0 and self.internal_pressure > PREMATURE_SPLIT_PRESSURE_THRESHOLD:
                # Premature split condition
                self._status = BifurcationStatus.NULL
                return {
                    "vector": None,
                    "status": "NULL",
                    "outcome": "premature_split",
                    "signature": ["identity_collapse", "non_viable"],
                    "error": "Premature split: threshold not reached"
                }
            
            raise RuntimeError(
                "Bifurcation Threshold not reached. "
                f"Current state: tension={self.confinement_tension:.2f}, "
                f"symmetry={self.stabilizing_symmetry:.2f}"
            )
        
        # Determine vector
        if force_vector is not None:
            vector = force_vector
        else:
            # LIFE: Internal tension exceeds containment
            # LIGHT: Containment exceeds internal tension
            #
            # Use internal_pressure as a proxy for tension/containment ratio
            # Higher pressure (>INTERNAL_PRESSURE_THRESHOLD) → LIFE (split)
            # Lower pressure (≤INTERNAL_PRESSURE_THRESHOLD) → LIGHT (absorb)
            vector = (
                BifurcationVector.LIFE 
                if self.internal_pressure > INTERNAL_PRESSURE_THRESHOLD 
                else BifurcationVector.LIGHT
            )
        
        # Mark as bifurcated (irreversible)
        self._bifurcated = True
        self._vector = vector
        
        if vector == BifurcationVector.LIFE:
            self._status = BifurcationStatus.LIFE
            return {
                "vector": "LIFE",
                "status": "LIFE",
                "outcome": "split",
                "signature": [
                    "Fragmentation",
                    "Preservation",
                    "Core-Sample Formation",
                    "Stabilization"
                ],
                "details": {
                    "seed_split": True,
                    "layers_expelled": True,
                    "solar_system_formed": True,
                    "hydrogen_replication_ended": True,
                    "agn_reproductive_symmetry": "lost"
                }
            }
        else:  # BifurcationVector.LIGHT
            self._status = BifurcationStatus.LIGHT
            return {
                "vector": "LIGHT",
                "status": "LIGHT",
                "outcome": "absorb",
                "signature": [
                    "Integration",
                    "Ascension",
                    "Confinement Expansion",
                    "Helium Replication"
                ],
                "details": {
                    "seed_absorbed": True,
                    "agn_mass_increased": True,
                    "envelope_expanded": True,
                    "helium_replication_begun": True,
                    "transformation": "Super Red Giant → Massive Super Red Giant"
                }
            }
    
    def query_status(self) -> str:
        """
        Query the current bifurcation status.
        
        BIFURCATE: STATUS
        
        Returns:
            One of: 'LIFE', 'LIGHT', 'NULL', 'STALLED', 'FROZEN', 'PENDING'
        """
        return self._status.value
    
    def invoke_life(self) -> dict:
        """
        Explicitly invoke the LIFE vector.
        
        BIFURCATE: SPLIT
        
        Returns:
            Bifurcation result with LIFE vector forced
        """
        return self.bifurcate(force_vector=BifurcationVector.LIFE)
    
    def invoke_light(self) -> dict:
        """
        Explicitly invoke the LIGHT vector.
        
        BIFURCATE: ABSORB
        
        Returns:
            Bifurcation result with LIGHT vector forced
        """
        return self.bifurcate(force_vector=BifurcationVector.LIGHT)
    
    def get_signature(self) -> List[str]:
        """
        Get the recursion signature for the current/completed bifurcation.
        
        Returns:
            List of signature elements based on vector
        """
        if self._vector == BifurcationVector.LIFE:
            return [
                "Fragmentation",
                "Preservation",
                "Core-Sample Formation",
                "Stabilization"
            ]
        elif self._vector == BifurcationVector.LIGHT:
            return [
                "Integration",
                "Ascension",
                "Confinement Expansion",
                "Helium Replication"
            ]
        else:
            return ["Pending"]


# Convenience functions matching the invocation grammar

def bifurcate_split(
    confinement_tension: float,
    stabilizing_symmetry: float,
    internal_pressure: float
) -> dict:
    """
    Execute bifurcation with LIFE (SPLIT) vector.
    
    BIFURCATE: SPLIT
    """
    op = LifeLightBifurcation(
        confinement_tension=confinement_tension,
        stabilizing_symmetry=stabilizing_symmetry,
        internal_pressure=internal_pressure
    )
    return op.invoke_life()


def bifurcate_absorb(
    confinement_tension: float,
    stabilizing_symmetry: float,
    internal_pressure: float
) -> dict:
    """
    Execute bifurcation with LIGHT (ABSORB) vector.
    
    BIFURCATE: ABSORB
    """
    op = LifeLightBifurcation(
        confinement_tension=confinement_tension,
        stabilizing_symmetry=stabilizing_symmetry,
        internal_pressure=internal_pressure
    )
    return op.invoke_light()


def bifurcate_status(operator: LifeLightBifurcation) -> str:
    """
    Query bifurcation status.
    
    BIFURCATE: STATUS
    """
    return operator.query_status()
