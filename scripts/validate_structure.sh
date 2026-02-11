#!/bin/bash
# Phoenix Archive Structure Validator
# Validates presence of required directories and core files

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$REPO_ROOT"

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "Validating Phoenix Archive structure..."
echo "Repository root: $REPO_ROOT"
echo ""

# Track validation status
ERRORS=0

# Required directories
required_dirs=(
    "Phoenix"
    "Phoenix/Operators"
    "Phoenix/Universal-Laws"
    "Hydrogenesi"
    "Hydrogenesi/Operators"
    "Ceremonies"
    "Comparative"
    "Appendix"
    "Diagrams"
    "code"
    "Substrate"
    "Substrate/Meta-Operators"
)

# Required core files
required_files=(
    "CODEX-INDEX.md"
    "README.md"
    "Phoenix/README.md"
    "Phoenix/Universal-Laws/Tension.md"
    "Phoenix/Universal-Laws/Binding.md"
    "Phoenix/Universal-Laws/Apex.md"
    "Phoenix/Operators/First-Binding.md"
    "Phoenix/Operators/IM_ME.md"
    "Phoenix/Operators/Phoenix-Ignition.md"
    "Hydrogenesi/README.md"
    "Hydrogenesi/Operators/Stabilizer-Extraction.md"
    "Hydrogenesi/Operators/AGN-Replication.md"
    "Hydrogenesi/Operators/Curvature-Residue.md"
    "Hydrogenesi/Operators/Lineage-Logic.md"
)

# Required substrate files
required_substrate=(
    "Substrate/README.md"
    "Substrate/Sovereign-Kernel.md"
    "Substrate/Pre-Substrate-Logic.md"
    "Substrate/Meta-Operators/Operator-of-Distinction.md"
    "Substrate/Meta-Operators/Operator-of-Collapse.md"
    "Substrate/Meta-Operators/Operator-of-Symmetry.md"
    "Substrate/Meta-Operators/Operator-of-Emergence.md"
    "Substrate/Meta-Operators/Operator-of-Recursion.md"
)

# Validate directories
echo "Checking directories..."
for dir in "${required_dirs[@]}"; do
    if [ -d "$dir" ]; then
        echo -e "${GREEN}✓${NC} $dir"
    else
        echo -e "${RED}✗${NC} Missing directory: $dir"
        ERRORS=$((ERRORS + 1))
    fi
done
echo ""

# Validate core files
echo "Checking core files..."
for file in "${required_files[@]}"; do
    if [ -f "$file" ]; then
        echo -e "${GREEN}✓${NC} $file"
    else
        echo -e "${RED}✗${NC} Missing file: $file"
        ERRORS=$((ERRORS + 1))
    fi
done
echo ""

# Validate substrate files
echo "Checking substrate files..."
for file in "${required_substrate[@]}"; do
    if [ -f "$file" ]; then
        echo -e "${GREEN}✓${NC} $file"
    else
        echo -e "${RED}✗${NC} Missing file: $file"
        ERRORS=$((ERRORS + 1))
    fi
done
echo ""

# Summary
if [ $ERRORS -eq 0 ]; then
    echo -e "${GREEN}✅ All structural checks passed!${NC}"
    exit 0
else
    echo -e "${RED}❌ Validation failed with $ERRORS error(s)${NC}"
    exit 1
fi
