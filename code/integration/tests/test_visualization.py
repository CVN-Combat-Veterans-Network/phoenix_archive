"""
Unit Tests for Visualization Module
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

from code.integration.meta_operators import ThreeFingerWaltz
from code.integration.visualization import (
    MermaidWaltzExporter,
    GraphVizWaltzExporter,
    JSONWaltzExporter,
    WaltzVisualizer
)
import json


class TestMermaidWaltzExporter:
    """Test Mermaid export functionality."""
    
    def test_mermaid_empty_waltz(self):
        """Test mermaid export with no steps."""
        waltz = ThreeFingerWaltz()
        exporter = MermaidWaltzExporter()
        
        result = exporter.export(waltz)
        
        assert "```mermaid" in result
        assert "No waltz steps recorded" in result
    
    def test_mermaid_complete_waltz(self):
        """Test mermaid export with complete waltz."""
        waltz = ThreeFingerWaltz()
        waltz.dance([{"name": "test"}])
        
        exporter = MermaidWaltzExporter()
        result = exporter.export(waltz)
        
        assert "```mermaid" in result
        assert "graph TD" in result
        assert "Phoenix" in result
        assert "Hydro" in result
        assert "Third" in result
        assert "Complete" in result
        assert "style Phoenix" in result


class TestGraphVizWaltzExporter:
    """Test GraphViz export functionality."""
    
    def test_graphviz_empty_waltz(self):
        """Test graphviz export with no steps."""
        waltz = ThreeFingerWaltz()
        exporter = GraphVizWaltzExporter()
        
        result = exporter.export(waltz)
        
        assert "digraph waltz" in result
        assert "No waltz steps recorded" in result
    
    def test_graphviz_complete_waltz(self):
        """Test graphviz export with complete waltz."""
        waltz = ThreeFingerWaltz()
        waltz.dance([{"name": "test"}])
        
        exporter = GraphVizWaltzExporter()
        result = exporter.export(waltz)
        
        assert "digraph waltz" in result
        assert "Phoenix" in result
        assert "Hydrogenesi" in result
        assert "TheThird" in result
        assert "Unified" in result
        assert "fillcolor" in result
    
    def test_graphviz_export_to_file(self):
        """Test graphviz export to file."""
        waltz = ThreeFingerWaltz()
        waltz.dance([{"name": "test"}])
        
        exporter = GraphVizWaltzExporter()
        
        import tempfile
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.dot') as f:
            filepath = f.name
        
        try:
            exporter.export_to_file(waltz, filepath)
            
            with open(filepath, 'r') as f:
                content = f.read()
            
            assert "digraph waltz" in content
            assert "Phoenix" in content
        finally:
            os.unlink(filepath)


class TestJSONWaltzExporter:
    """Test JSON export functionality."""
    
    def test_json_export_structure(self):
        """Test JSON export structure."""
        waltz = ThreeFingerWaltz()
        waltz.dance([{"name": "test"}])
        
        exporter = JSONWaltzExporter()
        result = exporter.export(waltz)
        
        # Parse JSON
        data = json.loads(result)
        
        assert "waltz_metadata" in data
        assert "steps" in data
        assert "phase_summary" in data
        
        assert data["waltz_metadata"]["completed"] == True
        assert len(data["steps"]) == 4
    
    def test_json_export_pretty(self):
        """Test pretty JSON formatting."""
        waltz = ThreeFingerWaltz()
        waltz.dance([{"name": "test"}])
        
        exporter = JSONWaltzExporter()
        result = exporter.export(waltz, pretty=True)
        
        # Pretty JSON should have newlines
        assert "\n" in result
        assert "  " in result  # Indentation


class TestWaltzVisualizer:
    """Test unified visualizer interface."""
    
    def test_visualizer_initialization(self):
        """Test visualizer initializes with all exporters."""
        viz = WaltzVisualizer()
        
        assert viz.mermaid_exporter is not None
        assert viz.graphviz_exporter is not None
        assert viz.json_exporter is not None
    
    def test_visualizer_mermaid_export(self):
        """Test mermaid export via visualizer."""
        waltz = ThreeFingerWaltz()
        waltz.dance([{"name": "test"}])
        
        viz = WaltzVisualizer()
        result = viz.export(waltz, format="mermaid")
        
        assert "```mermaid" in result
        assert "Phoenix" in result
    
    def test_visualizer_graphviz_export(self):
        """Test graphviz export via visualizer."""
        waltz = ThreeFingerWaltz()
        waltz.dance([{"name": "test"}])
        
        viz = WaltzVisualizer()
        result = viz.export(waltz, format="graphviz")
        
        assert "digraph waltz" in result
    
    def test_visualizer_ascii_export(self):
        """Test ASCII export via visualizer."""
        waltz = ThreeFingerWaltz()
        waltz.dance([{"name": "test"}])
        
        viz = WaltzVisualizer()
        result = viz.export(waltz, format="ascii")
        
        assert "THREE-FINGER WALTZ CHOREOGRAPHY" in result
    
    def test_visualizer_json_export(self):
        """Test JSON export via visualizer."""
        waltz = ThreeFingerWaltz()
        waltz.dance([{"name": "test"}])
        
        viz = WaltzVisualizer()
        result = viz.export(waltz, format="json")
        
        data = json.loads(result)
        assert "waltz_metadata" in data
    
    def test_visualizer_invalid_format(self):
        """Test error handling for invalid format."""
        waltz = ThreeFingerWaltz()
        viz = WaltzVisualizer()
        
        try:
            viz.export(waltz, format="invalid")
            assert False, "Should raise ValueError"
        except ValueError as e:
            assert "Unknown format" in str(e)
    
    def test_visualizer_supported_formats(self):
        """Test get_supported_formats method."""
        viz = WaltzVisualizer()
        formats = viz.get_supported_formats()
        
        assert "mermaid" in formats
        assert "graphviz" in formats
        assert "ascii" in formats
        assert "json" in formats


if __name__ == "__main__":
    print("Running visualization tests...")
    
    # Mermaid tests
    test_mermaid = TestMermaidWaltzExporter()
    test_mermaid.test_mermaid_empty_waltz()
    print("✓ test_mermaid_empty_waltz passed")
    
    test_mermaid.test_mermaid_complete_waltz()
    print("✓ test_mermaid_complete_waltz passed")
    
    # GraphViz tests
    test_graphviz = TestGraphVizWaltzExporter()
    test_graphviz.test_graphviz_empty_waltz()
    print("✓ test_graphviz_empty_waltz passed")
    
    test_graphviz.test_graphviz_complete_waltz()
    print("✓ test_graphviz_complete_waltz passed")
    
    test_graphviz.test_graphviz_export_to_file()
    print("✓ test_graphviz_export_to_file passed")
    
    # JSON tests
    test_json = TestJSONWaltzExporter()
    test_json.test_json_export_structure()
    print("✓ test_json_export_structure passed")
    
    test_json.test_json_export_pretty()
    print("✓ test_json_export_pretty passed")
    
    # Visualizer tests
    test_viz = TestWaltzVisualizer()
    test_viz.test_visualizer_initialization()
    print("✓ test_visualizer_initialization passed")
    
    test_viz.test_visualizer_mermaid_export()
    print("✓ test_visualizer_mermaid_export passed")
    
    test_viz.test_visualizer_graphviz_export()
    print("✓ test_visualizer_graphviz_export passed")
    
    test_viz.test_visualizer_ascii_export()
    print("✓ test_visualizer_ascii_export passed")
    
    test_viz.test_visualizer_json_export()
    print("✓ test_visualizer_json_export passed")
    
    test_viz.test_visualizer_invalid_format()
    print("✓ test_visualizer_invalid_format passed")
    
    test_viz.test_visualizer_supported_formats()
    print("✓ test_visualizer_supported_formats passed")
    
    print("\n✓ All visualization tests passed!")
