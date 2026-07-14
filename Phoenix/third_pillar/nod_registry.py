from enum import Enum
from dataclasses import dataclass
from typing import Dict


class NODLevel(Enum):
    NOD_0 = 0
    NOD_1 = 1
    NOD_2 = 2
    NOD_3 = 3
    NOD_4 = 4


@dataclass
class NODMetadata:
    level: NODLevel
    operator: str
    description: str


class NODRegistry:
    def __init__(self):
        self._registry: Dict[NODLevel, NODMetadata] = {
            NODLevel.NOD_0: NODMetadata(NODLevel.NOD_0, "Η →", "Hydrogenesi ground operator"),
            NODLevel.NOD_1: NODMetadata(NODLevel.NOD_1, "∂N", "Differentiation operator"),
            NODLevel.NOD_2: NODMetadata(NODLevel.NOD_2, "Ψ", "Construct-level operator"),
            NODLevel.NOD_3: NODMetadata(NODLevel.NOD_3, "Φ", "Phoenix linguistic operator"),
            NODLevel.NOD_4: NODMetadata(NODLevel.NOD_4, "Δ³", "Triadic apex operator"),
        }

    def get(self, level: NODLevel) -> NODMetadata:
        return self._registry[level]
