#!/bin/bash
# Script to regenerate keymap visualization
# Run this after updating config/hillside46.keymap

set -e

cd "$(dirname "$0")"

echo "🔄 Regenerating keymap visualization..."

# Check if keymap command exists
if ! command -v keymap &> /dev/null; then
    echo "❌ keymap-drawer not found!"
    echo "Install it with: pipx install keymap-drawer"
    exit 1
fi

# Parse keymap to YAML
echo "📝 Parsing keymap..."
keymap -c visualization/keymap-drawer-config.yaml parse -z config/hillside46.keymap > visualization/hillside46_parsed.yaml

# Generate SVG
echo "🎨 Generating SVG..."
keymap -c visualization/keymap-drawer-config.yaml draw visualization/hillside46_parsed.yaml > visualization/hillside46_layout.svg

echo "✅ Done! View visualization/hillside46_layout.svg"
echo ""
echo "Swedish characters (å, ä, ö) should be visible in the keymap."

