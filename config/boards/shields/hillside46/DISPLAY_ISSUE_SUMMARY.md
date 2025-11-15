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

### Important: Battery Impact

**If you have batteries connected to both sides**:
- External power controls (`EP_OFF`/`EP_ON`) typically control **USB/external power**, not battery power
- With batteries, the keyboard stays powered from battery even when USB is disconnected
- The display blanking is more likely due to **sleep/idle states** rather than power cutoff
- External power toggle might not work the same way with batteries

**For battery-powered keyboards**, the display typically blanks when:
- Keyboard enters idle state (after inactivity)
- Keyboard enters deep sleep (to save battery)
- Display doesn't re-initialize when keyboard wakes up

### Quick Fix Options

#### Option 1: External Power Toggle (If USB Connected)
If you're using USB power (even with battery connected), try:

1. **Activate ADJ layer** (check your keymap for the ADJ layer key)
2. **Press the key bound to `EP_OFF`** (turns off external/USB power)
3. **Wait 1-2 seconds**
4. **Press the key bound to `EP_ON`** (turns external/USB power back on)
5. **Display should re-initialize and show content**

#### Option 2: Power Cycle (Battery-Only)
If running on battery only (no USB):

1. **Turn off the keyboard** (power switch or disconnect battery)
2. **Wait 2-3 seconds**
3. **Turn keyboard back on**
4. **Display should initialize on boot**

#### Option 3: Prevent Display Blanking
Your config has `CONFIG_ZMK_DISPLAY_BLANK_ON_IDLE=n` which should prevent blanking on idle, but the display might still blank on deep sleep. You can try:

- **Disable deep sleep** (drains battery faster):
  ```conf
  CONFIG_ZMK_SLEEP=n
  ```
  Add this to `hillside46.conf` if not already there.

### Why This Works

The display re-initialization bug occurs when the keyboard wakes from sleep. Power cycling (or toggling external power if USB is connected) forces a full re-initialization, bypassing the bug.

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
3. **Let keyboard go to sleep** (wait for idle/sleep, or disconnect USB if connected)
4. **Wake keyboard** - Display is blank?
5. **Try one of these**:
   - **If USB connected**: Use ADJ layer → EP_OFF → wait → EP_ON
   - **If battery only**: Power cycle (turn off/on) or disconnect/reconnect battery
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
- ✅ **With batteries**: Display blanks on sleep, doesn't re-init on wake
- ✅ **Solution options**:
  - Power cycle (turn off/on) if battery-only
  - External power toggle (EP_OFF/EP_ON) if USB connected
  - Disable sleep (drains battery faster)
- ✅ **Convenience**: Consider adding EP_TOG key for easier toggling (if using USB)

**For battery-powered keyboards**: The display will likely blank when the keyboard goes to sleep. Power cycling is the most reliable way to get it back. This is a known limitation of ZMK display support.

