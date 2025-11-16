#!/usr/bin/env python3
"""
Simple keymap visualizer for Hillside46
Creates a clean, readable text representation with Swedish characters
"""

layers = {
    "Default (QWERTY Swedish)": [
        ["ESC", "Q", "W", "E", "R", "T", "", "", "Copy", "Paste", "Undo", "O", "P", "Å"],
        ["TAB", "A", "S", "D↓⌘", "F↓⇧", "G", "", "", "H", "J↓⇧", "K↓⌘", "L↓⌥", ";", "Ä"],
        ["⌥", "Z", "X", "C", "V", "B", "CAPS", "PrtSc", "N", "M", ",", ".", "/", "DEL"],
        ["", "", "", "⌘", "⇧", "⌫↓SYM", "→NAV", "→NUM", "SPC↓NAV", "⌘", "⌃", "", "", ""]
    ],
    
    "Navigation": [
        ["Copy", "1/F1", "2/F2", "3/F3", "4/F4", "5/F5", "", "", "6/F6", "7/F7", "8/F8", "9/F9", "0/F10", "0"],
        ["Cut", "⌘", "⌥", "⌃", "⇧", "!", "", "", "Sft+-", "←", "↑", "→", "▽", "Ä"],
        ["▽", "F1", "F2", "F3", "F4", "F5", "Undo", "▽", "END", "PgUp", "↓", "PgDn", "F10", "⌃"],
        ["", "", "", "⌘", "⇧", "⌫↓SYM", "▽", "→ADJ", "SPC", "⌘", "⌥", "", "", ""]
    ],
    
    "Symbols": [
        ["INS", "@", "Sft+2", "Sft+3", "AltGr+5", "Sft+5", "", "", "Sft+6", "Sft+7", "Sft+8", "Sft+9", "⏯", "⏭"],
        ["Sft++", "\\", "-", "Sft+0↓⌃", "Sft+8↓⇧", "\\", "", "", "/", "|", "AltGr+8", "AltGr+9", "Vol-", "Vol+"],
        ["▽", "AltGr+7", "_", "+", "AltGr+8", "|", "AltGr", "APP", "Sft+/", "Vol-", ",", ".", "⏮", "⏭"],
        ["", "", "", "⌘", "⇧", "⌫", "→ADJ", "▽", "SPC↓NAV", "⌘", "⌥", "", "", ""]
    ],
    
    "Adjust": [
        ["", "→0", "→0", "→0", "", "", "", "", "", "F11", "F12", "PrtSc", "EP_OFF", "EP_ON"],
        ["RESET", "BT0", "BT1", "BT2", "BT3", "BT4", "", "", "", "", "", "", "", "RESET"],
        ["BOOTL", "⌘", "⌥", "⌃", "⇧", "", "BT_CLR", "", "", "", "USB", "BLE", "", "BOOTL"],
        ["", "", "", "⌘", "⇧", "⌫↓SYM", "▽", "▽", "SPC↓NAV", "⌘", "⌥", "", "", ""]
    ],
    
    "NumPad": [
        ["▽", "▽", "F1", "F2", "F3", "F4", "", "", "-", "7", "8", "9", "Sft+7", "Sft+0"],
        ["TAB", "▽", "F5", "F6", "F7", "F8", "", "", "/", "4", "5", "6", "Sft+#", "."],
        ["▽", "▽", "F9", "F10", "F11", "F12", "▽", "▽", "0", "1", "2", "3", "↵", ","],
        ["", "", "", "⌘", "⇧", "⌫↓SYM", "0", "▽", "SPC↓NAV", "⌘", "⌥", "", "", ""]
    ]
}

def create_layer_diagram(name, keys):
    """Create ASCII art representation of one layer"""
    lines = []
    lines.append(f"\n{'='*100}")
    lines.append(f"{name:^100}")
    lines.append('='*100)
    
    # Row 1 - 6 keys left, 6 keys right
    row1_left = keys[0][:6]
    row1_right = keys[0][8:14]
    line1 = "  ".join(f"{k:^7}" for k in row1_left) + "    " + "  ".join(f"{k:^7}" for k in row1_right)
    lines.append(line1)
    
    # Row 2 - 6 keys left, 6 keys right  
    row2_left = keys[1][:6]
    row2_right = keys[1][8:14]
    line2 = "  ".join(f"{k:^7}" for k in row2_left) + "    " + "  ".join(f"{k:^7}" for k in row2_right)
    lines.append(line2)
    
    # Row 3 - 7 keys left (including thumb), 7 keys right
    row3_left = keys[2][:7]
    row3_right = keys[2][7:14]
    line3 = "  ".join(f"{k:^7}" for k in row3_left) + "  " + "  ".join(f"{k:^7}" for k in row3_right)
    lines.append(line3)
    
    # Row 4 - thumb cluster (4 keys each side in middle)
    thumbs = [k for k in keys[3] if k]  # Filter out empty strings
    line4 = " " * 20 + "  ".join(f"{k:^7}" for k in thumbs[:4]) + "    " + "  ".join(f"{k:^7}" for k in thumbs[4:])
    lines.append(line4)
    
    return "\n".join(lines)

# Generate all layers
output = []
output.append("╔═══════════════════════════════════════════════════════════════════════════════════════════════════╗")
output.append("║                            HILLSIDE 46 KEYMAP - SWEDISH UNICODE                                 ║")
output.append("╚═══════════════════════════════════════════════════════════════════════════════════════════════════╝")

for layer_name, keys in layers.items():
    output.append(create_layer_diagram(layer_name, keys))

output.append("\n" + "="*100)
output.append("Legend:")
output.append("  ↓ = Hold modifier  |  → = Layer switch  |  ▽ = Transparent  |  ⌘ = Command  |  ⌥ = Option")
output.append("  ⇧ = Shift  |  ⌃ = Control  |  Å/Ä/Ö = Swedish Unicode characters")
output.append("="*100)

# Write to file
with open("visualization/hillside46_layout.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(output))

print("✅ Created visualization/hillside46_layout.txt")
print("📄 Open it to see your keymap with Swedish characters!")

