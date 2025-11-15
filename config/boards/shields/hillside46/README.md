Hillside 46 is a split ergonomic keyboard with 3x6+5 choc-spaced keys.
It has the aggressive stagger of the Ferris but a longer thumb arc and a break-off outer pinkie column.
More information is at [github/mmccoyd](https://github.com/mmccoyd/hillside/).

The default keymap is described in
  [QMK](https://github.com/qmk/qmk_firmware/tree/master/keyboards/handwired/hillside/46).
  
For ZMK, the adjust layer has a few differences from the QMK version:

- Extra keys for bluetooth, reset and output.
- No swap Alt GUI keys.
- No RGB controls as RGB eats power.
- Bluetooth clear is deliberately in an inconvenient spot to avoid unpairing.

If used, the following must be manually enabled in hillside46.conf:

- Encoders
- Underglow

If desired, you could hardwire a display to the I2C header,
  which is arranged for a haptic feedback board.

**Display Configuration:**
For detailed information about setting up and configuring the OLED display,
see [DISPLAY_CONFIG.md](DISPLAY_CONFIG.md). This includes hardware connections,
firmware configuration, troubleshooting, and important notes about the display
setup for Hillside 46.

**If display doesn't work with current ZMK:**
See [FINDING_CURRENT_SOLUTION.md](FINDING_CURRENT_SOLUTION.md) for a guide on
finding a solution that works with the current ZMK version, including how to
pin to older versions or find updated configurations.