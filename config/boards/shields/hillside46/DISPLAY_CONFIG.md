# Hillside 46 Display Configuration

## Overview

The Hillside 46 keyboard supports an OLED display on the **left half only**. The display is connected via I2C to the nice!nano v2 microcontroller.

## Hardware Setup

### Display Module
- **Type**: SSD1306 OLED Display
- **Resolution**: 128x32 pixels
- **Interface**: I2C
- **I2C Address**: 0x3C (0x3C in hex)
- **Location**: Left half of the keyboard only

### Physical Connections

The display connects to the Hillside 46 PCB via the I2C header, which is arranged for a haptic feedback board but can also be used for displays.

**Connection Points on Hillside 46 PCB:**
- **SDA** (Serial Data) - I2C data line
- **SCL** (Serial Clock) - I2C clock line
- **VCC** - Power supply (3.3V)
- **GND** - Ground

**Connection to nice!nano v2:**
- **SDA** → P0.30 (Pin 30 on Port 0)
- **SCL** → P0.31 (Pin 31 on Port 0)
- **VCC** → 3.3V power
- **GND** → Ground

### Important Notes
- The display requires **pull-up resistors** (typically 4.7kΩ) on SDA and SCL lines. These should be present on the Hillside PCB or the display module.
- The display only works on the **left half** (central role) of the split keyboard.
- The right half does not have display support and should not reference the display in firmware.

## Firmware Configuration

### Key Configuration Files

1. **`hillside46_left.overlay`** - Display definition (left side only)
2. **`hillside46.dtsi`** - Shared base configuration (no display reference)
3. **`Kconfig.defconfig`** - Display feature flags (left side only)

### Critical Configuration Details

#### Compatible String
The display uses the **`"solomon,ssd1306fb"`** compatible string with additional display parameters. This configuration was found to work in the [HillSideView project](https://github.com/wannabecoffeenerd/HillSideView) where someone successfully got an I2C display working.

**Note**: You mentioned being in contact with "dalewking" who managed to get the I2C display working. The restored configuration may have been influenced by or based on their work. If you have any messages, emails, or forum posts from dalewking with additional configuration details, those could provide further insights.

**Working Configuration (from hillside view project):**
```dts
oled: ssd1306@3c {
    compatible = "solomon,ssd1306fb";
    reg = <0x3c>;
    label = "SSD1306";
    width = <128>;
    height = <32>;
    segment-offset = <0>;
    page-offset = <0>;
    display-offset = <0>;
    multiplex-ratio = <31>;
    segment-remap;
    com-invdir;
    prechargep = <0x22>;
};
```

**Note**: This configuration was restored from commit `8d2b158` which used the working I2C display setup. The simpler `"ssd,ssd1306fb-i2c"` compatible string may not work with this specific hardware setup.

#### I2C Pin Configuration
The I2C pins are configured using pinctrl:
```dts
&pinctrl {
    i2c1_default: i2c1_default {
        group1 {
            psels = <NRF_PSEL(TWIM_SDA, 0, 30)>,
                    <NRF_PSEL(TWIM_SCL, 0, 31)>;
        };
    };
};

&i2c1 {
    status = "okay";
    pinctrl-0 = <&i2c1_default>;
    pinctrl-names = "default";
    // ... display node ...
};
```

#### Display Reference
The display is referenced in the `chosen` node **only in the left overlay**:
```dts
/ {
    chosen {
        zephyr,display = &oled;
    };
};
```

**Note**: The display node is labeled `oled` (not `ssd1306`) to match the working configuration.

**Important**: This reference must NOT be in the shared `hillside46.dtsi` file, as it would cause build errors for the right side (which doesn't have a display).

### Kconfig Configuration

Display features are enabled conditionally for the left side only in `Kconfig.defconfig`:

```kconfig
if SHIELD_HILLSIDE46_LEFT
    # Display configuration - only for left side (central role)
    CONFIG_DISPLAY=y
    CONFIG_SSD1306=y
    CONFIG_ZMK_DISPLAY=y
    CONFIG_ZMK_WIDGET_LAYER_STATUS=y
    CONFIG_ZMK_WIDGET_BATTERY_STATUS=y
    CONFIG_ZMK_WIDGET_BATTERY_STATUS_SHOW_PERCENTAGE=y
    CONFIG_ZMK_WIDGET_OUTPUT_STATUS=y
    # ... other display configs ...
endif
```

## Display Features

When properly configured, the display shows:
- **Layer Status** - Current active layer
- **Battery Status** - Battery level with percentage
- **Output Status** - Bluetooth/USB connection status
- **WPM Status** - Words per minute (optional, disabled by default)

## Troubleshooting

### Display Not Working

1. **Check Compatible String**
   - Current configuration uses `"solomon,ssd1306fb"` with additional parameters
   - This configuration was found to work in the HillSideView project
   - If this doesn't work, try `"ssd,ssd1306fb-i2c"` (simpler, but may not work with all displays)

2. **Verify I2C Address**
   - Default is `0x3C`
   - Some displays use `0x3D` - try changing `reg = <0x3C>` to `reg = <0x3D>` if needed

3. **Check Pin Connections**
   - Verify SDA is connected to P0.30
   - Verify SCL is connected to P0.31
   - Check for loose connections or cold solder joints

4. **Pull-up Resistors**
   - I2C requires 4.7kΩ pull-up resistors on SDA and SCL
   - Verify these are present on the PCB or display module

5. **Power Supply**
   - Ensure display is receiving 3.3V power
   - Check VCC and GND connections

6. **Build Configuration**
   - Ensure display configs are only enabled for left side
   - Right side should NOT have display references

### Build Errors

**Error: `undefined node label 'ssd1306'`**
- **Cause**: Display reference in shared dtsi file
- **Fix**: Move `zephyr,display = &ssd1306;` to left overlay only

**Error: Display not initializing**
- **Cause**: Wrong compatible string or I2C address
- **Fix**: Use `"ssd,ssd1306fb-i2c"` and verify I2C address

## History

- **2024-10-22**: Initial display configuration added
- **2025-01**: Display stopped working after ZMK update
- **2025-01**: Fixed by restoring `"ssd,ssd1306fb-i2c"` compatible string from git history (commit 24e0535)
- **2025-01**: Fixed build error for right side by moving display reference to left overlay only

## References

- [ZMK Display Documentation](https://zmk.dev/docs/config/displays)
- [Hillside Keyboard Repository](https://github.com/mmccoyd/hillside/)
- Last known working configuration: commit `24e0535` in this repository

