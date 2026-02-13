# Phoenix Archive Makefile
# Version: 1.0.0

.PHONY: help validate substrate all clean

# Default target
help:
	@echo "Phoenix Archive - Make Commands"
	@echo "================================"
	@echo ""
	@echo "Available targets:"
	@echo "  make validate   - Validate complete archive structure"
	@echo "  make substrate  - Validate substrate layer"
	@echo "  make all        - Run all validations"
	@echo "  make help       - Show this help message"
	@echo ""

# Validate complete archive structure
validate:
	@echo "🔥 Validating Phoenix Archive structure..."
	@bash scripts/validate_structure.sh
	@echo "✅ Structure validation complete"

# Validate substrate structure
substrate: validate
	@echo "🌑 Validating substrate layer..."
	@bash scripts/validate_substrate.sh
	@echo "✅ Substrate validation complete"

# Run all validations
all: validate substrate
	@echo "✅ All validations complete"

# Clean temporary files (if needed)
clean:
	@echo "🧹 Cleaning temporary files..."
	@find . -name "*.tmp" -type f -delete
	@find . -name ".DS_Store" -type f -delete
	@echo "✅ Clean complete"
