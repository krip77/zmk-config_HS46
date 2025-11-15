# Repository Structure and File Relationships

This document explains the structure of the ZMK firmware configuration repository for Hillside keyboards and how all the files relate to each other.

## Overview

This repository contains ZMK (Zephyr-based keyboard firmware) configuration for three Hillside keyboard variants:
- **Hillside 46**: 3x6+5 keys (46 keys total)
- **Hillside 48**: 3x6+1+5 keys (48 keys total)  
- **Hillside 52**: 3x6+3+5 keys (52 keys total)

All keyboards are **split keyboards**, meaning they have separate left and right halves that communicate wirelessly via Bluetooth.

## Repository Structure

```
zmk-config_HS46/
├── build.yaml                    # GitHub Actions build matrix
├── README.md                     # Main repository documentation
├── LICENSE                       # License file
├── CODE_REVIEW_ISSUES.md        # Code review notes and issues
├── FLASHING_GUIDE.md            # Guide for flashing firmware
└── config/                       # Main configuration directory
    ├── west.yml                  # West manifest (Zephyr package manager)
    ├── Kconfig.shield            # Root-level shield definitions
    ├── Kconfig.defconfig         # Root-level default configurations
    ├── keymap_KP_swe.h          # Custom keymap header (Swedish layout)
    │
    ├── hillside46.*             # Root-level configs (legacy/deprecated)
    ├── hillside48.*             # Root-level configs (legacy/deprecated)
    ├── hillside52.*             # Root-level configs (legacy/deprecated)
    │
    └── boards/
        └── shields/
            ├── hillside46/      # Hillside 46 shield definition
            ├── hillside48/      # Hillside 48 shield definition
            └── hillside52/      # Hillside 52 shield definition
```

## File Types and Their Purposes

### Build Configuration Files

#### `build.yaml`
**Purpose**: Defines which keyboard configurations to build in GitHub Actions
**Location**: Root directory
**Key Points**:
- Lists all board + shield combinations to build
- Each split keyboard needs two builds: `*_left` and `*_right`
- Comment out keyboards you don't have to save build time
- Pushing changes to this file triggers a build

**Example**:
```yaml
include:
  - board: nice_nano_v2
    shield: hillside46_left
  - board: nice_nano_v2
    shield: hillside46_right
```

#### `west.yml`
**Purpose**: West manifest file for Zephyr package management
**Location**: `config/west.yml`
**Key Points**:
- Defines where to fetch ZMK firmware from (GitHub)
- Specifies which ZMK branch/version to use
- Tells West that this `config/` directory is the configuration root

### Shield Definition Files

Shield files define the hardware configuration for each keyboard variant. Each shield directory (e.g., `hillside46/`) contains:

#### `*.zmk.yml`
**Purpose**: Shield metadata and feature definitions
**Location**: `config/boards/shields/hillside46/hillside46.zmk.yml`
**Key Points**:
- Defines shield name, ID, and type
- Lists required hardware (e.g., `pro_micro` for nice!nano)
- Declares available features (keys, encoder, underglow)
- Defines sibling shields (left/right halves)

**Example**:
```yaml
id: hillside46
name: Hillside46
type: shield
requires: [pro_micro]
features: [keys, encoder, underglow]
siblings: [hillside46_left, hillside46_right]
```

#### `Kconfig.shield`
**Purpose**: Defines Kconfig symbols for shield detection
**Location**: `config/boards/shields/hillside46/Kconfig.shield`
**Key Points**:
- Creates boolean symbols like `SHIELD_HILLSIDE46_LEFT` and `SHIELD_HILLSIDE46_RIGHT`
- These symbols are used to conditionally enable features
- Allows different configurations for left vs right halves

#### `Kconfig.defconfig`
**Purpose**: Default Kconfig settings for the shield
**Location**: `config/boards/shields/hillside46/Kconfig.defconfig`
**Key Points**:
- Sets default values for configuration options
- Can be conditional based on shield (left/right)
- For Hillside 46: Enables display only for left side
- Example: `CONFIG_ZMK_DISPLAY=y` only when `SHIELD_HILLSIDE46_LEFT`

### Device Tree Files

Device Tree files define the hardware layout and pin assignments.

#### `*.dtsi`
**Purpose**: Base device tree source (shared between left/right)
**Location**: `config/boards/shields/hillside46/hillside46.dtsi`
**Key Points**:
- Contains common hardware definitions
- Defines key matrix, encoders, sensors
- **Important**: Should NOT contain side-specific things (like display)
- Included by both left and right overlays

**Contains**:
- `chosen` node with kscan and matrix transform
- Key matrix definition (`default_transform`)
- Keyboard scan configuration (`kscan0`)
- Encoder definitions (left/right, both disabled by default)
- Sensor definitions

#### `*_left.overlay` / `*_right.overlay`
**Purpose**: Side-specific device tree overlays
**Location**: `config/boards/shields/hillside46/hillside46_left.overlay`
**Key Points**:
- Overrides and extends the base `.dtsi` file
- Left overlay: Contains display configuration, left encoder enable
- Right overlay: Contains right encoder enable, column offset
- Each side has different column GPIO assignments

**Left Overlay Contains**:
- Column GPIO pin assignments
- I2C configuration for display
- Display node definition (SSD1306)
- Display reference in `chosen` node
- Left encoder enable

**Right Overlay Contains**:
- Column GPIO pin assignments (mirrored)
- Column offset for matrix transform
- Right encoder enable

#### `boards/nice_nano*.overlay`
**Purpose**: Board-specific hardware configuration
**Location**: `config/boards/shields/hillside46/boards/nice_nano_v2.overlay`
**Key Points**:
- Configures board-specific features (nice!nano v2)
- Contains SPI configuration for RGB underglow
- Only included when building for that specific board

### Keymap Files

#### `*.keymap`
**Purpose**: Defines the key layout and behaviors
**Location**: `config/boards/shields/hillside46/hillside46.keymap`
**Key Points**:
- Defines all layers and key assignments
- Includes behaviors (tap-dance, combos, macros, etc.)
- Can include custom header files
- Same keymap used for both left and right (ZMK handles mirroring)

**Structure**:
- Layer definitions (QWERTY, NAV, SYM, ADJ, etc.)
- Combo definitions
- Behavior definitions (hold-tap, tap-dance, macros)
- Key bindings for each layer

#### `keymap_KP_swe.h`
**Purpose**: Custom keymap header with Swedish layout definitions
**Location**: `config/keymap_KP_swe.h`
**Key Points**:
- Contains Swedish-specific key definitions
- Included by keymap files that need Swedish layout
- Defines macros and shortcuts

### Configuration Files

#### `*.conf`
**Purpose**: Kconfig configuration file (feature flags)
**Location**: `config/hillside46.conf`
**Key Points**:
- Enables/disables features at build time
- Can enable: encoders, RGB underglow, display widgets, etc.
- **Note**: For Hillside 46, display configs are in `Kconfig.defconfig` instead
- Legacy root-level configs may exist but are deprecated

**Common Settings**:
- `CONFIG_EC11=y` - Enable encoder support
- `CONFIG_ZMK_RGB_UNDERGLOW=y` - Enable RGB
- `CONFIG_ZMK_DISPLAY=y` - Enable display (for Hillside 46, use Kconfig.defconfig)

### Documentation Files

#### `README.md`
**Purpose**: Main repository documentation
**Location**: Root and in each shield directory
**Key Points**:
- Explains how to build and flash firmware
- Documents keyboard-specific features
- Points to other documentation

#### `DISPLAY_CONFIG.md`
**Purpose**: Detailed display configuration documentation
**Location**: `config/boards/shields/hillside46/DISPLAY_CONFIG.md`
**Key Points**:
- Hardware connection guide
- Firmware configuration details
- Troubleshooting steps
- History of display fixes

#### `FLASHING_GUIDE.md`
**Purpose**: Step-by-step flashing instructions
**Location**: Root directory
**Key Points**:
- How to enter bootloader mode
- How to flash left and right halves
- Troubleshooting flashing issues

#### `CODE_REVIEW_ISSUES.md`
**Purpose**: Notes from code review
**Location**: Root directory
**Key Points**:
- Documents known issues
- Configuration conflicts
- Recommendations for fixes

## File Relationships and Build Process

### How Files Are Combined During Build

1. **West reads `west.yml`** → Fetches ZMK firmware from GitHub
2. **Build system reads `build.yaml`** → Determines what to build
3. **For each shield (e.g., `hillside46_left`)**:
   - Reads `hillside46.zmk.yml` → Gets shield metadata
   - Reads `Kconfig.shield` → Sets shield symbols
   - Reads `Kconfig.defconfig` → Applies default configs
   - Reads `*.conf` → Applies user configs
   - Reads `*.dtsi` → Base hardware definition
   - Reads `*_left.overlay` → Left-specific overrides
   - Reads `boards/nice_nano_v2.overlay` → Board-specific config
   - Reads `*.keymap` → Key layout
   - All combined → Compiled firmware

### File Inclusion Hierarchy

```
ZMK Base Firmware
    ↓
west.yml (fetches ZMK)
    ↓
build.yaml (defines builds)
    ↓
Shield Definition (hillside46.zmk.yml)
    ↓
Kconfig Files (Kconfig.shield, Kconfig.defconfig)
    ↓
Device Tree (hillside46.dtsi)
    ↓
Device Tree Overlays (*_left.overlay, boards/*.overlay)
    ↓
Keymap (*.keymap)
    ↓
Compiled Firmware (.uf2 file)
```

### Important Relationships

#### Split Keyboard Configuration
- **Left and Right are separate shields**: `hillside46_left` and `hillside46_right`
- **Shared base**: Both use `hillside46.dtsi` for common definitions
- **Different overlays**: `hillside46_left.overlay` vs `hillside46_right.overlay`
- **Same keymap**: Both use `hillside46.keymap` (ZMK handles mirroring)
- **Different configs**: Left has display, right doesn't (via `Kconfig.defconfig`)

#### Display Configuration (Hillside 46)
- **Only on left side**: Display is defined in `hillside46_left.overlay`
- **Not in dtsi**: Display reference must NOT be in shared `hillside46.dtsi`
- **Conditional config**: Display Kconfig only enabled for left side
- **Critical compatible string**: Must use `"ssd,ssd1306fb-i2c"` (not `"solomon,ssd1306fb"`)

#### Legacy vs Modern Structure
- **Root-level files** (`config/hillside46.*`): Legacy, may be deprecated
- **Shield files** (`config/boards/shields/hillside46/*`): Modern, preferred
- **Shield files take precedence** over root-level files

## File Modification Guidelines

### Files You Should Modify

✅ **Safe to modify**:
- `*.keymap` - Your key layout
- `*.conf` - Feature flags (encoders, RGB, etc.)
- `build.yaml` - Which keyboards to build
- `*_left.overlay` / `*_right.overlay` - Side-specific hardware (with caution)

### Files You Should NOT Modify (Usually)

❌ **Avoid modifying** (unless you know what you're doing):
- `*.dtsi` - Base hardware definition (shared by both sides)
- `*.zmk.yml` - Shield metadata
- `Kconfig.shield` - Shield detection symbols
- `west.yml` - ZMK version/URL
- `boards/*.overlay` - Board-specific configs

### When to Modify Overlays

Modify overlays when:
- Adding/removing hardware (display, encoders, RGB)
- Changing pin assignments
- Enabling/disabling hardware features

**Important**: 
- Changes to `*_left.overlay` only affect left side
- Changes to `*_right.overlay` only affect right side
- Changes to `*.dtsi` affect BOTH sides

## Common File Patterns

### For Adding a New Feature (e.g., Display)

1. **Hardware definition**: Add to `*_left.overlay` (if left-side only)
2. **Kconfig enable**: Add to `Kconfig.defconfig` (conditional on shield)
3. **Keymap binding**: Add to `*.keymap` (if user-controllable)

### For Changing Key Layout

1. **Modify**: `*.keymap` file
2. **Test**: Build and flash
3. **No other files needed** (usually)

### For Enabling Encoders

1. **Enable in overlay**: Set `status = "okay"` in `*_left.overlay` or `*_right.overlay`
2. **Enable driver**: Uncomment `CONFIG_EC11=y` in `*.conf`
3. **Add to keymap**: Bind encoder actions in `*.keymap`

## Troubleshooting File Issues

### Build Fails: "undefined node label"
- **Cause**: Reference to hardware that doesn't exist
- **Fix**: Remove reference from shared files (`.dtsi`), move to side-specific overlay

### Display Not Working
- **Check**: `hillside46_left.overlay` has display definition
- **Check**: `Kconfig.defconfig` enables display for left side only
- **Check**: Compatible string is `"ssd,ssd1306fb-i2c"`

### Right Side Build Fails
- **Check**: No display references in `hillside46.dtsi`
- **Check**: Display configs are conditional in `Kconfig.defconfig`

## Summary

- **`build.yaml`**: What to build
- **`west.yml`**: Where to get ZMK from
- **`*.zmk.yml`**: Shield metadata
- **`*.dtsi`**: Shared hardware definition
- **`*_left.overlay` / `*_right.overlay`**: Side-specific hardware
- **`*.keymap`**: Key layout
- **`*.conf`**: Feature flags
- **`Kconfig.*`**: Build-time configuration

Understanding these relationships helps you modify the firmware correctly and troubleshoot issues effectively.

