#!/bin/bash
# Phoenix Archive Substrate Validator
# Deep validation of substrate layer content and cross-references

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$REPO_ROOT"

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo "🌑 Deep Substrate Validation"
echo "============================"
echo ""

# Track validation status
ERRORS=0
WARNINGS=0

# Function to check if file contains required section
check_section() {
    local file=$1
    local section=$2
    
    if grep -q "## $section" "$file" 2>/dev/null; then
        return 0
    else
        return 1
    fi
}

# Function to check for invocation
check_invocation() {
    local file=$1
    
    if grep -q "Invocation:" "$file" 2>/dev/null || grep -q "INVOCATION" "$file" 2>/dev/null; then
        return 0
    else
        return 1
    fi
}

# Function to check for sigil
check_sigil() {
    local file=$1
    
    if grep -q "SIGIL" "$file" 2>/dev/null || grep -q "Sigil" "$file" 2>/dev/null; then
        return 0
    else
        return 1
    fi
}

# Function to check for symbol
check_symbol() {
    local file=$1
    
    if grep -q "Symbol:" "$file" 2>/dev/null; then
        return 0
    else
        return 1
    fi
}

echo "Validating Sovereign Kernel..."
if [ -f "Substrate/Sovereign-Kernel.md" ]; then
    echo -e "${BLUE}Checking Sovereign-Kernel.md content...${NC}"
    
    if check_section "Substrate/Sovereign-Kernel.md" "OVERVIEW"; then
        echo -e "${GREEN}✓${NC} Has OVERVIEW section"
    else
        echo -e "${YELLOW}⚠${NC} Missing OVERVIEW section"
        WARNINGS=$((WARNINGS + 1))
    fi
    
    if check_section "Substrate/Sovereign-Kernel.md" "FORMAL DEFINITION"; then
        echo -e "${GREEN}✓${NC} Has FORMAL DEFINITION section"
    else
        echo -e "${YELLOW}⚠${NC} Missing FORMAL DEFINITION section"
        WARNINGS=$((WARNINGS + 1))
    fi
    
    if check_invocation "Substrate/Sovereign-Kernel.md"; then
        echo -e "${GREEN}✓${NC} Has Invocation"
    else
        echo -e "${YELLOW}⚠${NC} Missing Invocation"
        WARNINGS=$((WARNINGS + 1))
    fi
    
    if check_sigil "Substrate/Sovereign-Kernel.md"; then
        echo -e "${GREEN}✓${NC} Has Sigil"
    else
        echo -e "${YELLOW}⚠${NC} Missing Sigil"
        WARNINGS=$((WARNINGS + 1))
    fi
    
    if check_symbol "Substrate/Sovereign-Kernel.md"; then
        echo -e "${GREEN}✓${NC} Has Symbol"
    else
        echo -e "${YELLOW}⚠${NC} Missing Symbol"
        WARNINGS=$((WARNINGS + 1))
    fi
else
    echo -e "${RED}✗${NC} Sovereign-Kernel.md not found"
    ERRORS=$((ERRORS + 1))
fi
echo ""

echo "Validating Pre-Substrate Logic..."
if [ -f "Substrate/Pre-Substrate-Logic.md" ]; then
    echo -e "${BLUE}Checking Pre-Substrate-Logic.md content...${NC}"
    
    if grep -q "Why must the Triad be three" "Substrate/Pre-Substrate-Logic.md"; then
        echo -e "${GREEN}✓${NC} Addresses 'Why three?' question"
    else
        echo -e "${YELLOW}⚠${NC} May not address 'Why three?' question"
        WARNINGS=$((WARNINGS + 1))
    fi
    
    if grep -q "recursion" "Substrate/Pre-Substrate-Logic.md" || grep -q "Recursion" "Substrate/Pre-Substrate-Logic.md"; then
        echo -e "${GREEN}✓${NC} Discusses recursion"
    else
        echo -e "${YELLOW}⚠${NC} May not discuss recursion"
        WARNINGS=$((WARNINGS + 1))
    fi
    
    if check_invocation "Substrate/Pre-Substrate-Logic.md"; then
        echo -e "${GREEN}✓${NC} Has Invocation"
    else
        echo -e "${YELLOW}⚠${NC} Missing Invocation"
        WARNINGS=$((WARNINGS + 1))
    fi
else
    echo -e "${RED}✗${NC} Pre-Substrate-Logic.md not found"
    ERRORS=$((ERRORS + 1))
fi
echo ""

echo "Validating Meta-Operators..."

meta_operators=(
    "Operator-of-Distinction.md"
    "Operator-of-Collapse.md"
    "Operator-of-Symmetry.md"
    "Operator-of-Emergence.md"
    "Operator-of-Recursion.md"
)

for op in "${meta_operators[@]}"; do
    op_path="Substrate/Meta-Operators/$op"
    op_name="${op%.md}"
    
    echo -e "${BLUE}Checking $op_name...${NC}"
    
    if [ -f "$op_path" ]; then
        # Check for required sections
        if check_section "$op_path" "OVERVIEW"; then
            echo -e "${GREEN}✓${NC} Has OVERVIEW"
        else
            echo -e "${YELLOW}⚠${NC} Missing OVERVIEW"
            WARNINGS=$((WARNINGS + 1))
        fi
        
        if check_section "$op_path" "FORMAL DEFINITION"; then
            echo -e "${GREEN}✓${NC} Has FORMAL DEFINITION"
        else
            echo -e "${YELLOW}⚠${NC} Missing FORMAL DEFINITION"
            WARNINGS=$((WARNINGS + 1))
        fi
        
        if check_section "$op_path" "MECHANISM"; then
            echo -e "${GREEN}✓${NC} Has MECHANISM"
        else
            echo -e "${YELLOW}⚠${NC} Missing MECHANISM"
            WARNINGS=$((WARNINGS + 1))
        fi
        
        if check_invocation "$op_path"; then
            echo -e "${GREEN}✓${NC} Has Invocation"
        else
            echo -e "${YELLOW}⚠${NC} Missing Invocation"
            WARNINGS=$((WARNINGS + 1))
        fi
        
        if check_sigil "$op_path"; then
            echo -e "${GREEN}✓${NC} Has Sigil"
        else
            echo -e "${YELLOW}⚠${NC} Missing Sigil"
            WARNINGS=$((WARNINGS + 1))
        fi
        
        if check_symbol "$op_path"; then
            echo -e "${GREEN}✓${NC} Has Symbol"
        else
            echo -e "${YELLOW}⚠${NC} Missing Symbol"
            WARNINGS=$((WARNINGS + 1))
        fi
        
        # Check for cross-references to Kernel or other substrate
        if grep -q "Sovereign-Kernel" "$op_path" || grep -q "Kernel" "$op_path"; then
            echo -e "${GREEN}✓${NC} References Kernel"
        else
            echo -e "${YELLOW}⚠${NC} May not reference Kernel"
            WARNINGS=$((WARNINGS + 1))
        fi
        
    else
        echo -e "${RED}✗${NC} $op not found"
        ERRORS=$((ERRORS + 1))
    fi
    echo ""
done

echo "Validating cross-references in CODEX-INDEX.md..."
if [ -f "CODEX-INDEX.md" ]; then
    if grep -q "SUBSTRATE" "CODEX-INDEX.md" || grep -q "Substrate" "CODEX-INDEX.md"; then
        echo -e "${GREEN}✓${NC} CODEX-INDEX.md includes Substrate section"
    else
        echo -e "${RED}✗${NC} CODEX-INDEX.md missing Substrate section"
        ERRORS=$((ERRORS + 1))
    fi
    
    if grep -q "Sovereign-Kernel" "CODEX-INDEX.md"; then
        echo -e "${GREEN}✓${NC} CODEX-INDEX.md references Sovereign Kernel"
    else
        echo -e "${YELLOW}⚠${NC} CODEX-INDEX.md may not reference Sovereign Kernel"
        WARNINGS=$((WARNINGS + 1))
    fi
else
    echo -e "${RED}✗${NC} CODEX-INDEX.md not found"
    ERRORS=$((ERRORS + 1))
fi
echo ""

# Summary
echo "============================"
echo "Validation Summary"
echo "============================"
if [ $ERRORS -eq 0 ] && [ $WARNINGS -eq 0 ]; then
    echo -e "${GREEN}✅ Perfect! All substrate validations passed!${NC}"
    exit 0
elif [ $ERRORS -eq 0 ]; then
    echo -e "${YELLOW}⚠ Validation passed with $WARNINGS warning(s)${NC}"
    echo -e "${YELLOW}Consider addressing warnings for completeness${NC}"
    exit 0
else
    echo -e "${RED}❌ Validation failed with $ERRORS error(s) and $WARNINGS warning(s)${NC}"
    exit 1
fi
