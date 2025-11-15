# Display Issue Summary and Solution

## Problem Timeline

Based on your git history:
- **October 22, 2024**: You made multiple attempts to fix the display
- **Late 2023 / Early 2024**: Display stopped working after a ZMK update
- **Over 1 year**: Display has been non-functional

## Root Cause Analysis

### Most Likely Issue: ZMK Known Bug #674

**ZMK GitHub Issue**: [#674 - OLED Re-init on ext_pwr on](https://github.com/zmkfirmware/zmk/issues/674)

**The Problem**:
- Display works fine on initial boot
- Display goes blank when keyboard goes to sleep or external power is cut
- Display **does not re-initialize** when power is restored
- This is a **known bug in ZMK** - display support is still "proof of concept"

**Why This Matches Your Situation**:
1. ✅ Display worked before ZMK update
2. ✅ Stopped working after ZMK update (late 2023/early 2024)
3. ✅ Keyboard itself works fine (only display affected)
4. ✅ Configuration appears correct (compatible string, pins, etc.)
5. ✅ You have external power controls in keymap (EP_OFF/EP_ON)

## The Solution: External Power Toggle

### Quick Fix (Try This First!)

Your keymap already has external power controls in the **ADJ layer**:
- `EP_OFF` - Turns off external power
- `EP_ON` - Turns on external power

**To fix the blank display**:

1. **Activate ADJ layer** (check your keymap for the ADJ layer key)
2. **Press the key bound to `EP_OFF`** (turns off external power)
3. **Wait 1-2 seconds**
4. **Press the key bound to `EP_ON`** (turns external power back on)
5. **Display should re-initialize and show content**

### Why This Works

Toggling external power forces the display to re-initialize, which bypasses the bug where it doesn't re-init automatically after sleep.

## Alternative: Add Toggle Key (More Convenient)

Instead of using two keys (EP_OFF then EP_ON), you can add a single toggle key:

In your `hillside46.keymap`, replace one of the external power keys with:
```dts
&ext_power EP_TOG
```

This gives you a single key that toggles external power on/off, making it easier to fix the display when it goes blank.

## Testing Steps

1. **Flash your current firmware** (configuration is correct)
2. **Power on keyboard** - Does display show on boot?
   - **Yes**: Hardware is fine, it's the re-init bug
   - **No**: Check hardware connections
3. **Let keyboard go to sleep** (or disconnect power briefly)
4. **Wake keyboard** - Display is blank?
5. **Use ADJ layer → EP_OFF → wait → EP_ON**
6. **Display should come back!**

## If External Power Toggle Doesn't Work

### Check 1: Display Works on Fresh Boot?
- Flash firmware
- Power cycle completely (disconnect USB, wait, reconnect)
- Does display show anything on boot?
  - **Yes**: Confirms it's the re-init bug, toggle should work
  - **No**: Hardware issue or configuration problem

### Check 2: Try Alternative I2C Address
Some displays use 0x3D instead of 0x3C. In `hillside46_left.overlay`:
```dts
reg = <0x3D>;  // Try this instead of 0x3C
```

### Check 3: Verify Hardware
- Check SDA/SCL connections (P0.30, P0.31)
- Verify pull-up resistors are present
- Check power connections (VCC, GND)

## Long-Term Solution

This is a **known ZMK bug** that hasn't been fixed yet. Options:

1. **Use the workaround** (external power toggle) - Works reliably
2. **Disable sleep** (not recommended - kills battery):
   ```conf
   CONFIG_ZMK_SLEEP=n
   ```
3. **Wait for ZMK fix** - Monitor [Issue #674](https://github.com/zmkfirmware/zmk/issues/674)

## Summary

- ✅ Your configuration is **correct**
- ✅ Hardware is likely **fine** (keyboard works)
- ✅ This is a **known ZMK bug** (Issue #674)
- ✅ **Solution**: Toggle external power using EP_OFF/EP_ON keys
- ✅ **Convenience**: Consider adding EP_TOG key for easier toggling

**Try the external power toggle first** - this is almost certainly the fix you need!

