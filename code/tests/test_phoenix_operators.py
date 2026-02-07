"""Tests for Phoenix operators."""
from __future__ import annotations
import pytest
from code.phoenix.operators import (
    FirstBinding,
    IM_ME,
    PhoenixIgnition,
    ApexFormation,
    ThreeFingerWaltz,
    BlackHoledImprint,
)


class TestFirstBinding:
    """Test First Binding operator."""

    def test_binding_basic(self):
        """Test basic triadic binding."""
        binding = FirstBinding()
        result = binding.apply(a="fear", b="courage", stabilizer="service")
        
        assert result["tension_pair"] == ("fear", "courage")
        assert result["stabilizer"] == "service"
        assert result["triad"] == ("fear", "service", "courage")

    def test_binding_different_values(self):
        """Test binding with different tension pairs."""
        binding = FirstBinding()
        result = binding.apply(
            a="isolation", b="connection", stabilizer="commitment"
        )
        
        assert result["tension_pair"] == ("isolation", "connection")
        assert result["stabilizer"] == "commitment"
        assert result["triad"] == ("isolation", "commitment", "connection")

    def test_binding_triad_structure(self):
        """Test that triad maintains A-S-B structure."""
        binding = FirstBinding()
        result = binding.apply(a="control", b="surrender", stabilizer="trust")
        
        triad = result["triad"]
        assert len(triad) == 3
        assert triad[0] == "control"
        assert triad[1] == "trust"
        assert triad[2] == "surrender"


class TestIM_ME:
    """Test IM_ME recursion operator."""

    def test_recursion_basic(self):
        """Test basic IM→ME recursion."""
        im_me = IM_ME()
        sequence = im_me.recurse(identity="warrior", depth=3)
        
        assert len(sequence) == 6  # 3 depths * 2 (IM + ME)
        assert sequence[0] == "IM(warrior)"
        assert sequence[1] == "ME(warrior)"
        assert sequence[2] == "IM(warrior)"
        assert sequence[3] == "ME(warrior)"

    def test_recursion_depth_one(self):
        """Test recursion with depth 1."""
        im_me = IM_ME()
        sequence = im_me.recurse(identity="self", depth=1)
        
        assert len(sequence) == 2
        assert sequence[0] == "IM(self)"
        assert sequence[1] == "ME(self)"

    def test_recursion_pattern(self):
        """Test that IM→ME pattern alternates correctly."""
        im_me = IM_ME()
        sequence = im_me.recurse(identity="identity", depth=5)
        
        for i in range(0, len(sequence), 2):
            assert sequence[i].startswith("IM(")
            if i + 1 < len(sequence):
                assert sequence[i + 1].startswith("ME(")

    def test_recursion_different_identities(self):
        """Test recursion with different identity values."""
        im_me = IM_ME()
        seq1 = im_me.recurse(identity="alpha", depth=2)
        seq2 = im_me.recurse(identity="beta", depth=2)
        
        assert "alpha" in seq1[0]
        assert "beta" in seq2[0]
        assert seq1 != seq2


class TestPhoenixIgnition:
    """Test Phoenix Ignition operator."""

    def test_ignition_basic(self):
        """Test basic phoenix ignition."""
        ignition = PhoenixIgnition()
        result = ignition.ignite(state="old-identity")
        
        assert "collapsed" in result
        assert "risen" in result
        assert result["collapsed"] == "core::old-identity"
        assert result["risen"] == "apex::old-identity"

    def test_ignition_transformation(self):
        """Test that ignition transforms state."""
        ignition = PhoenixIgnition()
        state = "unintegrated-self"
        result = ignition.ignite(state=state)
        
        assert state in result["collapsed"]
        assert state in result["risen"]
        assert "core::" in result["collapsed"]
        assert "apex::" in result["risen"]

    def test_ignition_different_states(self):
        """Test ignition with different initial states."""
        ignition = PhoenixIgnition()
        
        result1 = ignition.ignite(state="state-a")
        result2 = ignition.ignite(state="state-b")
        
        assert result1["collapsed"] != result2["collapsed"]
        assert result1["risen"] != result2["risen"]
        assert "state-a" in result1["collapsed"]
        assert "state-b" in result2["collapsed"]


class TestApexFormation:
    """Test Apex Formation operator."""

    def test_apex_formation_basic(self):
        """Test basic apex formation from triads."""
        apex = ApexFormation()
        triads = [
            ("fear", "service", "courage"),
            ("isolation", "commitment", "connection"),
        ]
        result = apex.apply(triads)
        
        assert result["apex_formed"] is True
        assert result["sovereignty"] == "developing"
        assert len(result["stabilizers"]) == 2
        assert result["apex_symbol"] == "△"

    def test_apex_formation_no_triads(self):
        """Test apex formation with no triads."""
        apex = ApexFormation()
        result = apex.apply([])
        
        assert result["apex_formed"] is False
        assert result["sovereignty"] == "none"

    def test_apex_formation_sovereignty_levels(self):
        """Test sovereignty levels based on number of triads."""
        apex = ApexFormation()
        
        result1 = apex.apply([("a", "s", "b")])
        assert result1["sovereignty"] == "emerging"
        
        result3 = apex.apply([("a", "s", "b")] * 3)
        assert result3["sovereignty"] == "stable"
        
        result5 = apex.apply([("a", "s", "b")] * 5)
        assert result5["sovereignty"] == "sovereign"


class TestThreeFingerWaltz:
    """Test Three-Finger Waltz operator."""

    def test_waltz_basic(self):
        """Test basic waltz pattern generation."""
        waltz = ThreeFingerWaltz()
        triad = ("fear", "service", "courage")
        result = waltz.apply(triad, cycles=2)
        
        assert result["pattern"] == "●—○—●"
        assert result["rhythm"] == "pulse-pause-pulse"
        assert result["cycles"] == 2
        assert result["total_beats"] == 6

    def test_waltz_beat_structure(self):
        """Test that waltz beats follow correct structure."""
        waltz = ThreeFingerWaltz()
        triad = ("a", "s", "b")
        result = waltz.apply(triad, cycles=1)
        
        beats = result["beats"]
        assert len(beats) == 3
        assert beats[0]["position"] == "pulse"
        assert beats[1]["position"] == "pause"
        assert beats[2]["position"] == "pulse"

    def test_waltz_embodied_practice(self):
        """Test embodied practice sequence generation."""
        waltz = ThreeFingerWaltz()
        triad = ("fear", "service", "courage")
        sequence = waltz.embodied_practice(triad, duration_seconds=3.0)
        
        assert len(sequence) == 4
        assert "fear" in sequence[0]
        assert "service" in sequence[1]
        assert "courage" in sequence[2]


class TestBlackHoledImprint:
    """Test Black-Holed Imprint operator."""

    def test_imprint_creation(self):
        """Test basic imprint creation."""
        bhi = BlackHoledImprint()
        imprint = bhi.apply("warrior-identity", context="discharge")
        
        assert "black-hole::" in imprint["imprint_id"]
        assert imprint["status"] == "collapsed"
        assert imprint["integration_required"] is True

    def test_imprint_information_retrieval(self):
        """Test retrieving information from imprint."""
        bhi = BlackHoledImprint()
        imprint = bhi.apply("creative-identity")
        info = bhi.retrieve_information(imprint)
        
        assert "value_encoded" in info
        assert "creative-identity" in info["value_encoded"]
        assert "integration_path" in info

    def test_imprint_integration_status(self):
        """Test updating integration status."""
        bhi = BlackHoledImprint()
        imprint = bhi.apply("test-identity")
        
        # Not integrated
        active = bhi.integration_status(imprint, integrated=False)
        assert active["status"] == "active"
        assert active["influence"] == "constraining"
        
        # Integrated
        integrated = bhi.integration_status(imprint, integrated=True)
        assert integrated["status"] == "integrated"
        assert integrated["influence"] == "informative"
        assert integrated["integration_required"] is False
