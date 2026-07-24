#!/usr/bin/env python3
"""
nod_registry.py

NOD Level Registry + Operator Metadata
Third Pillar: Nucleus-Centric Framework (FLQG)

Authority: Δ³
Alignment: Phoenix · Hydrogenesi · Codex Triad
"""

from enum import Enum
from dataclasses import dataclass
from typing import Dict


class NODLevel(Enum):
    """Canonical NOD hierarchy for all Third Pillar modules."""
    NOD_0 = 0
    NOD_1 = 1
    NOD_2 = 2
    NOD_3 = 3
    NOD_4 = 4


@dataclass
class NODMetadata:
    """Metadata describing each NOD level and its governing operator."""
    level: NODLevel
    operator: str
    description: str


class NODRegistry:
    """Registry mapping NOD levels to their operator metadata."""

    def __init__(self):
        self._registry: Dict[NODLevel, NODMetadata] = {
            NODLevel.NOD_0: NODMetadata(
                NODLevel.NOD_0,
                "Η →",
                "Hydrogenesi ground operator (origin state)"
            ),
            NODLevel.NOD_1: NODMetadata(
                NODLevel.NOD_1,
                "∂N",
                "Differentiation operator (nuclear emission)"
            ),
            NODLevel.NOD_2: NODMetadata(
                NODLevel.NOD_2,
                "Ψ",
                "Construct-level operator (structural projection)"
            ),
            NODLevel.NOD_3: NODMetadata(
                NODLevel.NOD_3,
                "Φ",
                "Phoenix linguistic operator (linguistic projection)"
            ),
            NODLevel.NOD_4: NODMetadata(
                NODLevel.NOD_4,
                "Δ³",
                "Triadic apex operator (Third Pillar apex)"
            ),
        }

    def get(self, level: NODLevel) -> NODMetadata:
        """Return metadata for a given NOD level."""
        return self._registry[level]
