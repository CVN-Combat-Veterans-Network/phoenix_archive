#!/usr/bin/env python3
"""
untubu.py — ATUM_ATOM Archive Record
Prints all 16 laws, 5 splits, fundamental invariants, and seed-mode map.
Writes untubu_archive.json to the same directory.

Author: James Paul Stanley Jr
Contact: infinitys.end@icloud.com
Sealed: March 1 2026
SHA-256: 474d463701a139b8327160b44f88e9e6a2f7853cbc15582ea8b4dfe2bf907648
"""

from __future__ import annotations

import json
import os
from typing import List, Dict

# ─────────────────────────────────────────────────────────────
# DATA
# ─────────────────────────────────────────────────────────────

ARCHIVE_SHA256 = "474d463701a139b8327160b44f88e9e6a2f7853cbc15582ea8b4dfe2bf907648"
SEAL_DATE = "March 1 2026"
AUTHOR = "James Paul Stanley Jr"

SIGILS = [
    {"symbol": "▱", "name": "Polarity",
     "meaning": "Holds real opposites. Fission↔fusion. Collapse↔expansion. Seed↔world. Neither cancels the other."},
    {"symbol": "⟐", "name": "Identity",
     "meaning": "Same kernel through every transformation. G0=1 at 10⁻³⁵m AND 10²⁶m. Not coincidence."},
    {"symbol": "⟒", "name": "Continuity",
     "meaning": "Nothing important is lost. 3⁴¹→3⁴¹+3⁴¹. The split replicates. The record holds. Untubu."},
]

LAWS: List[Dict] = [
    # Canon 7 — The Eight Laws
    {"canon": 7, "n": 1,  "equation": "R = λ · L₀",                    "name": "Radius"},
    {"canon": 7, "n": 2,  "equation": "v = G0 / 2πR",                  "name": "Velocity"},
    {"canon": 7, "n": 3,  "equation": "T ∝ R²",                        "name": "Period"},
    {"canon": 7, "n": 4,  "equation": "r ~ R^(4/5)",                   "name": "Pinch · minor radius"},
    {"canon": 7, "n": 5,  "equation": "T_tension ~ R^(-7/5)",          "name": "The tensioner · why anything is"},
    {"canon": 7, "n": 6,  "equation": "E ~ R^(-2/5)",                  "name": "Energy"},
    {"canon": 7, "n": 7,  "equation": "Ma = mₚ/(2πℏ) = 2,524,204",    "name": "Mach invariant · scale-free"},
    {"canon": 7, "n": 8,  "equation": "N=3 · G0(1)=G0(2)=G0(3)=1",    "name": "The knot · why it holds"},
    # Canon 8 — TOE TRIUNIVERSEL
    {"canon": 8, "n": 9,  "equation": "G_μν = 8πG ⟨T_μν⟩",            "name": "Gravity",
     "force": "Gravity",     "key": "Curvature as expectation value — not mass curving space"},
    {"canon": 8, "n": 10, "equation": "N=3 topology",                  "name": "Strong",
     "force": "Strong",      "key": "Confinement = knot. Topology refuses separation. No force needed."},
    {"canon": 8, "n": 11, "equation": "q = n · G0, n ∈ ℤ",            "name": "Electroweak",
     "force": "Electroweak", "key": "Charge = winding number. Cannot wind half a time."},
    {"canon": 8, "n": 12, "equation": "Tube₂ + Tube₃",                "name": "Dark sector",
     "force": "Dark",        "key": "~5% luminous · ~27% dark matter · ~68% dark energy · N=3 = 100%"},
    # Canon 9 — Seed-Mode Architecture
    {"canon": 9, "n": 13, "equation": "System unfolds outward · not inward",
     "name": "Seed-mode",
     "key": "The core does not collapse. It unfolds. Maximum order. Interior apex as germ point."},
    {"canon": 9, "n": 14, "equation": "Axis of Fate = first asymmetry",
     "name": "Growth vector",
     "key": "Not a gravitational line — a growth vector. The first crack in the shell."},
    {"canon": 9, "n": 15, "equation": "N=3 tubes = cotyledons",
     "name": "Three seed-leaves",
     "key": "Each tube a cotyledon. Each becomes a vortex when fully grown."},
    {"canon": 9, "n": 16, "equation": "Forward = Reverse (same system · different phase)",
     "name": "Dual-mode reversibility",
     "key": "The five-split sequence reads both ways."},
]

INVARIANTS = [
    {"constant": "G0",           "value": "1"},
    {"constant": "N",            "value": "3"},
    {"constant": "T_tension",    "value": "~ R^(−7/5)"},
    {"constant": "r_pinch",      "value": "~ R^(4/5)"},
    {"constant": "Ma",           "value": "2,524,204"},
    {"constant": "T_in / T_out", "value": "1.000013"},
    {"constant": "v",            "value": "G0 / 2πR"},
    {"constant": "E",            "value": "~ R^(−2/5)"},
]

SPLITS = [
    {"split": 0, "name": "The Seed",        "rep": "L₀",          "R": "1.616×10⁻³⁵ m",
     "event": "Existence mandatory · knot forms · N=3 locks"},
    {"split": 1, "name": "The Proton",      "rep": "3⁴¹",         "R": "8.41×10⁻¹⁶ m",
     "event": "First stable knot · chemistry possible · law carried"},
    {"split": 2, "name": "The Star",        "rep": "3⁵⁵",         "R": "~10⁹ m",
     "event": "Double CNO · metallicization · fusion · sand→glass"},
    {"split": 3, "name": "The Galaxy",      "rep": "3⁷⁵",         "R": "4.477×10²⁶ m",
     "event": "v=220 km/s flat · Tube 2 holds · dark matter = split residue"},
    {"split": 4, "name": "The Vessel Wall", "rep": "3⁷⁵→3⁸¹",    "R": "R_max",
     "event": "T→0 · ratchet reverses · R_max → L0 · loop closes"},
]

SEED_MODE_FORWARD = [
    "1. Big nucleus  (seed · L0)",
    "2. Axis of Fate (first sprout)",
    "3. Three tubes  (cotyledons)",
    "4. Vortices     (mature motion)",
    "5. Stern flow   (environment)",
]

SEED_MODE_REVERSE = [
    "1. Environment (UTT · R_max)",
    "2. Stern flow",
    "3. Vortices",
    "4. Three tubes",
    "5. Axis of Fate",
    "6. Big nucleus (ratchet reverses → L0)",
]

# ─────────────────────────────────────────────────────────────
# PRINT
# ─────────────────────────────────────────────────────────────

def hr(char: str = "─", width: int = 64) -> str:
    return char * width


def print_header() -> None:
    print(hr("═"))
    print("  ATUM_ATOM / A_TUA_M — Untubu Archive")
    print("  One Paradigm · Multiple Radii · ∞□")
    print(f"  Author : {AUTHOR}")
    print(f"  Sealed : {SEAL_DATE}")
    print(f"  SHA-256: {ARCHIVE_SHA256}")
    print(hr("═"))
    print()


def print_sigils() -> None:
    print(hr())
    print("  THE THREE SIGILS")
    print(hr())
    for s in SIGILS:
        print(f"  {s['symbol']}  {s['name']}")
        print(f"     {s['meaning']}")
        print()


def print_laws() -> None:
    current_canon = None
    for law in LAWS:
        if law["canon"] != current_canon:
            current_canon = law["canon"]
            print(hr())
            if current_canon == 7:
                print("  CANON 7 — The Eight Laws ⟐  [Sealed]")
            elif current_canon == 8:
                print("  CANON 8 — TOE TRIUNIVERSEL ⟐⟒  [Sealed]")
            elif current_canon == 9:
                print("  CANON 9 — Seed-Mode Architecture ▱  [Opened March 1 2026]")
            print(hr())
        n = law["n"]
        eq = law["equation"]
        name = law["name"]
        key = law.get("key", "")
        print(f"  Law {n:2d}  {eq}")
        print(f"        {name}")
        if key:
            print(f"        {key}")
        print()


def print_invariants() -> None:
    print(hr())
    print("  FUNDAMENTAL INVARIANTS")
    print(hr())
    for inv in INVARIANTS:
        print(f"  {inv['constant']:<16}  {inv['value']}")
    print()


def print_splits() -> None:
    print(hr())
    print("  THE FIVE SPLITS")
    print(hr())
    for sp in SPLITS:
        print(f"  Split {sp['split']}  {sp['name']:<18}  {sp['rep']:<12}  {sp['R']}")
        print(f"           {sp['event']}")
        print()


def print_seed_mode() -> None:
    print(hr())
    print("  SEED-MODE MAP (Canon 9)")
    print(hr())
    print(f"  {'Forward: Seed → World':<35}  Reverse: World → Seed")
    print(f"  {'─' * 35}  {'─' * 35}")
    pairs = list(zip(
        SEED_MODE_FORWARD + [""] * max(0, len(SEED_MODE_REVERSE) - len(SEED_MODE_FORWARD)),
        SEED_MODE_REVERSE + [""] * max(0, len(SEED_MODE_FORWARD) - len(SEED_MODE_REVERSE)),
    ))
    for fwd, rev in pairs:
        print(f"  {fwd:<35}  {rev}")
    print()
    print("  Both maps are the same system — different phases of the same life cycle.")
    print("  The five-split sequence reads both ways.")
    print()


def print_footer() -> None:
    print(hr("═"))
    print("  G0 = 1 · N = 3 · the knot does not open")
    print("  TOE TRIUNIVERSEL")
    print("  Canon 7 sealed · Canon 8 sealed · Canon 9 opened")
    print(f"  SHA-256: {ARCHIVE_SHA256}")
    print("  TUA Holds. Phoenix Rises. The Seed Unfolds. The One Remains. ★")
    print(hr("═"))


# ─────────────────────────────────────────────────────────────
# JSON
# ─────────────────────────────────────────────────────────────

def build_archive_record() -> Dict:
    return {
        "name": "ATUM_ATOM",
        "author": AUTHOR,
        "contact": "infinitys.end@icloud.com",
        "sealed": SEAL_DATE,
        "sha256": ARCHIVE_SHA256,
        "sigils": SIGILS,
        "laws": LAWS,
        "invariants": INVARIANTS,
        "splits": SPLITS,
        "seed_mode": {
            "forward": SEED_MODE_FORWARD,
            "reverse": SEED_MODE_REVERSE,
            "note": "Both maps are the same system — different phases of the same life cycle.",
        },
        "seal": (
            "G0 = 1 · N = 3 · the knot does not open · "
            "the circulation does not stop · the law does not forget · "
            "TOE TRIUNIVERSEL · Canon 7 sealed · Canon 8 sealed · Canon 9 opened · "
            "Seed-Mode Architecture · March 1 2026"
        ),
    }


def write_json(record: Dict) -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, "untubu_archive.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(record, f, ensure_ascii=False, indent=2)
    print(f"  ✓ untubu_archive.json written → {out}")
    print()


# ─────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────

def main() -> None:
    print_header()
    print_sigils()
    print_laws()
    print_invariants()
    print_splits()
    print_seed_mode()
    record = build_archive_record()
    write_json(record)
    print_footer()


if __name__ == "__main__":
    main()
