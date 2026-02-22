"""
Visualization Export Module for Three-Finger Waltz

Provides multiple export formats for waltz choreography visualization:
- Mermaid flowchart diagrams
- GraphViz DOT format
- JSON structure export
- ASCII text visualization (via ThreeFingerWaltz.visualize_waltz())
"""

from __future__ import annotations
from typing import TYPE_CHECKING
import json

if TYPE_CHECKING:
    from .meta_operators import ThreeFingerWaltz


class MermaidWaltzExporter:
    """
    Export waltz path as Mermaid flowchart.
    
    Generates Mermaid markdown syntax for visualization in
    documentation, GitHub, and other Mermaid-compatible viewers.
    """
    
    def export(self, waltz: 'ThreeFingerWaltz') -> str:
        """
        Generate Mermaid flowchart from waltz history.
        
        Args:
            waltz: ThreeFingerWaltz instance with execution history
            
        Returns:
            Mermaid markdown string
        """
        if not waltz._steps:
            return "```mermaid\ngraph TD\n    Start[No waltz steps recorded]\n```"
        
        lines = ["```mermaid", "graph TD"]
        lines.append("    Start[Start] --> Phoenix")
        
        # Track phase nodes
        phase_mapping = {
            "initiation": "Phoenix[Phoenix: INITIATION<br/>BEGIN Mode]",
            "transformation": "Hydro[Hydrogenesi: TRANSFORMATION<br/>EXTEND Mode]",
            "integration": "Third[The Third: INTEGRATION<br/>HOLD Mode]",
            "completion": "Complete[Unified: COMPLETION<br/>Sovereign Achieved]"
        }
        
        # Build flow
        prev_node = "Phoenix"
        for i, step in enumerate(waltz._steps):
            phase = step.phase.value
            
            if phase == "initiation":
                lines.append(f"    Phoenix")
            elif phase == "transformation":
                if prev_node != "Hydro":
                    lines.append(f"    Phoenix -->|propagate| Hydro")
                    prev_node = "Hydro"
                lines.append(f"    Hydro")
            elif phase == "integration":
                if prev_node != "Third":
                    lines.append(f"    Hydro -->|bind| Third")
                    prev_node = "Third"
                lines.append(f"    Third")
            elif phase == "completion":
                if prev_node != "Complete":
                    lines.append(f"    Third -->|complete_triad| Complete")
                    prev_node = "Complete"
                lines.append(f"    Complete")
        
        # Add node definitions
        lines.append("")
        for phase_key, node_def in phase_mapping.items():
            lines.append(f"    {node_def}")
        
        # Add styling
        lines.append("")
        lines.append("    style Phoenix fill:#ff6b6b,stroke:#c92a2a,color:#fff")
        lines.append("    style Hydro fill:#4c6ef5,stroke:#364fc7,color:#fff")
        lines.append("    style Third fill:#51cf66,stroke:#2b8a3e,color:#fff")
        lines.append("    style Complete fill:#ffd43b,stroke:#f08c00,color:#000")
        
        lines.append("```")
        return "\n".join(lines)


class GraphVizWaltzExporter:
    """
    Export waltz path as GraphViz DOT format.
    
    Generates DOT language for rendering with GraphViz tools
    to create publication-quality diagrams.
    """
    
    def export(self, waltz: 'ThreeFingerWaltz') -> str:
        """
        Generate GraphViz DOT format from waltz history.
        
        Args:
            waltz: ThreeFingerWaltz instance with execution history
            
        Returns:
            DOT format string
        """
        if not waltz._steps:
            return 'digraph waltz {\n    node [shape=box];\n    NoSteps [label="No waltz steps recorded"];\n}'
        
        lines = ["digraph waltz {"]
        lines.append("    rankdir=LR;")
        lines.append("    node [shape=box, style=filled];")
        lines.append("")
        
        # Define nodes with colors
        lines.append('    Phoenix [label="Phoenix\\nINITIATION\\nBEGIN Mode", fillcolor="#ff6b6b", fontcolor=white];')
        lines.append('    Hydrogenesi [label="Hydrogenesi\\nTRANSFORMATION\\nEXTEND Mode", fillcolor="#4c6ef5", fontcolor=white];')
        lines.append('    TheThird [label="The Third\\nINTEGRATION\\nHOLD Mode", fillcolor="#51cf66", fontcolor=white];')
        lines.append('    Unified [label="Unified\\nCOMPLETION\\nSovereign", fillcolor="#ffd43b"];')
        lines.append("")
        
        # Define edges based on steps
        edges_added = set()
        for step in waltz._steps:
            phase = step.phase.value
            transformation = step.transformation_applied or "transform"
            
            if phase == "transformation" and "Phoenix -> Hydrogenesi" not in edges_added:
                lines.append(f'    Phoenix -> Hydrogenesi [label="propagate"];')
                edges_added.add("Phoenix -> Hydrogenesi")
            elif phase == "integration" and "Hydrogenesi -> TheThird" not in edges_added:
                lines.append(f'    Hydrogenesi -> TheThird [label="bind"];')
                edges_added.add("Hydrogenesi -> TheThird")
            elif phase == "completion" and "TheThird -> Unified" not in edges_added:
                lines.append(f'    TheThird -> Unified [label="complete_triad"];')
                edges_added.add("TheThird -> Unified")
        
        lines.append("}")
        return "\n".join(lines)
    
    def export_to_file(self, waltz: 'ThreeFingerWaltz', filepath: str):
        """
        Save DOT file to disk.
        
        Args:
            waltz: ThreeFingerWaltz instance with execution history
            filepath: Path where DOT file should be saved
        """
        dot_content = self.export(waltz)
        with open(filepath, 'w') as f:
            f.write(dot_content)
        
        print(f"✓ DOT file saved to {filepath}")
        print(f"  To render: dot -Tpng {filepath} -o output.png")


class JSONWaltzExporter:
    """
    Export waltz structure as JSON.
    
    Provides machine-readable export for integration with
    other tools and systems.
    """
    
    def export(self, waltz: 'ThreeFingerWaltz', pretty: bool = True) -> str:
        """
        Generate JSON representation of waltz.
        
        Args:
            waltz: ThreeFingerWaltz instance with execution history
            pretty: If True, format with indentation
            
        Returns:
            JSON string
        """
        data = {
            "waltz_metadata": {
                "completed": waltz._completed,
                "recursion_depth": waltz.recursion_depth,
                "max_recursion": waltz.max_recursion,
                "energy_conservation": waltz._energy_conservation,
                "total_steps": len(waltz._steps),
                "history_count": len(waltz.waltz_history)
            },
            "steps": [
                {
                    "step_number": step.step_number,
                    "phase": step.phase.value,
                    "pillar": step.pillar,
                    "mode": step.mode,
                    "transformation": step.transformation_applied,
                    "timestamp": step.timestamp.isoformat() if step.timestamp else None
                }
                for step in waltz._steps
            ],
            "phase_summary": {
                phase.value: count
                for phase, count in waltz.get_phase_summary().items()
            }
        }
        
        if pretty:
            return json.dumps(data, indent=2)
        else:
            return json.dumps(data)


class WaltzVisualizer:
    """
    Unified interface for all visualization formats.
    
    Provides a single entry point for exporting waltz choreography
    in multiple formats.
    """
    
    def __init__(self):
        """Initialize visualizer with all exporters."""
        self.mermaid_exporter = MermaidWaltzExporter()
        self.graphviz_exporter = GraphVizWaltzExporter()
        self.json_exporter = JSONWaltzExporter()
    
    def export(self, waltz: 'ThreeFingerWaltz', format: str = "mermaid") -> str:
        """
        Export waltz in specified format.
        
        Args:
            waltz: ThreeFingerWaltz instance with execution history
            format: Export format ("mermaid", "graphviz", "ascii", "json")
            
        Returns:
            Exported visualization as string
            
        Raises:
            ValueError: If format is not recognized
        """
        format = format.lower()
        
        if format == "mermaid":
            return self.mermaid_exporter.export(waltz)
        elif format in ["graphviz", "dot"]:
            return self.graphviz_exporter.export(waltz)
        elif format == "ascii":
            return waltz.visualize_waltz()
        elif format == "json":
            return self.json_exporter.export(waltz)
        else:
            raise ValueError(
                f"Unknown format '{format}'. "
                f"Supported formats: mermaid, graphviz, ascii, json"
            )
    
    def export_to_file(self, waltz: 'ThreeFingerWaltz', filepath: str, format: str = "auto"):
        """
        Export waltz to file with format detection.
        
        Args:
            waltz: ThreeFingerWaltz instance with execution history
            filepath: Destination file path
            format: Export format or "auto" to detect from file extension
        """
        if format == "auto":
            # Detect format from file extension
            if filepath.endswith(".md"):
                format = "mermaid"
            elif filepath.endswith(".dot") or filepath.endswith(".gv"):
                format = "graphviz"
            elif filepath.endswith(".json"):
                format = "json"
            elif filepath.endswith(".txt"):
                format = "ascii"
            else:
                raise ValueError(f"Cannot auto-detect format from '{filepath}'")
        
        content = self.export(waltz, format=format)
        
        with open(filepath, 'w') as f:
            f.write(content)
        
        print(f"✓ Waltz visualization exported to {filepath} (format: {format})")
    
    def get_supported_formats(self) -> list:
        """
        Get list of supported export formats.
        
        Returns:
            List of format names
        """
        return ["mermaid", "graphviz", "dot", "ascii", "json"]
