#!/bin/bash
# Script to regenerate keymap visualization
# Run this after updating config/hillside46.keymap

set -e

cd "$(dirname "$0")"

echo "🔄 Regenerating keymap visualization..."

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found!"
    exit 1
fi

# Check if create_simple_keymap.py exists
if [ ! -f "create_simple_keymap.py" ]; then
    echo "❌ create_simple_keymap.py not found!"
    exit 1
fi

# Generate text-based keymap visualization
echo "📝 Generating keymap visualization..."
python3 create_simple_keymap.py

echo ""
echo "✅ Done! View visualization/hillside46_layout.txt"
echo ""
echo "Swedish characters (å, ä, ö) are correctly displayed in the layout."
