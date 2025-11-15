# Display Troubleshooting - Known ZMK Issues and Fixes

## Timeline of the Issue

Based on git history:
- **October 22, 2024**: Multiple attempts to fix display after it stopped working
- **Late 2023 / Early 2024**: Display likely stopped working after a ZMK update
- **Over 1 year**: Display has been non-functional since then

## Known ZMK Display Issues

### Issue #1: Display Remains Blank After External Power Cutoff

**ZMK GitHub Issue**: [#674](https://github.com/zmkfirmware/zmk/issues/674)

**Problem**: 
- Display works initially after flashing firmware
- Display goes blank after keyboard goes to sleep or external power is cut
- Display does not re-initialize when power is restored

**Status**: This is a known issue in ZMK. Display support is still considered "proof of concept" and may not be fully stable.

**Workaround Solutions**:

#### Solution 1: Toggle External Power
Your keymap already includes external power controls (`EP_OFF` and `EP_ON`). Try toggling external power:

1. Press the key bound to `&ext_power EP_OFF` to turn off external power
2. Wait a moment
3. Press the key bound to `&ext_power EP_ON` to turn external power back on
4. The display should re-initialize

**Your current keymap has these bound in the ADJ layer** (check your keymap for exact key positions).

#### Solution 2: Disable Deep Sleep (Temporary)
Add to your `hillside46.conf`:
```conf
CONFIG_ZMK_SLEEP=n
```
**Warning**: This will significantly reduce battery life. Use only for testing.

#### Solution 3: Power Cycle the Keyboard
- Disconnect USB / turn off power
- Wait a few seconds
- Reconnect power / turn on
- Display should initialize on boot

### Issue #2: Compatible String Change

**Problem**: 
- ZMK updated the display driver
- Old compatible string `"ssd,ssd1306fb-i2c"` may have been deprecated
- New compatible string `"solomon,ssd1306fb"` may not work with all hardware

**Current Status**: 
- Your configuration uses `"ssd,ssd1306fb-i2c"` (restored from working version)
- This is the correct compatible string for your hardware

**If display still doesn't work**, try:
1. Verify the compatible string is exactly `"ssd,ssd1306fb-i2c"` (case-sensitive)
2. Check if your ZMK version still supports this compatible string
3. Consider updating to latest ZMK if this string was deprecated

### Issue #3: Display Initialization Priority

**Problem**: Display may not initialize at the correct time during boot

**Potential Fix**: Some users have reported success by adjusting display initialization priority, but this requires modifying ZMK source code (not recommended for most users).

## Current Configuration Status

Your current configuration appears correct:
- ✅ Compatible string: `"ssd,ssd1306fb-i2c"` (correct for your hardware)
- ✅ I2C pins: P0.30 (SDA), P0.31 (SCL) (correct)
- ✅ I2C address: 0x3C (standard)
- ✅ Display only on left side (correct)
- ✅ Display configs conditional (correct)
- ✅ External power controls in keymap (present)

## Diagnostic Steps

### Step 1: Verify Display Initializes on Boot
1. Flash fresh firmware
2. Power on keyboard (fresh boot, not from sleep)
3. **Does the display show anything?**
   - **Yes**: Display hardware works, issue is with re-initialization after sleep
   - **No**: Continue to Step 2

### Step 2: Test External Power Toggle
1. If display works on boot but goes blank after sleep:
2. Use the `EP_OFF` / `EP_ON` keys in your ADJ layer
3. Toggle external power off and back on
4. **Does display come back?**
   - **Yes**: This confirms the known ZMK issue #674
   - **No**: Continue to Step 3

### Step 3: Hardware Verification
1. **Check I2C communication**:
   - Verify SDA/SCL connections are secure
   - Check for cold solder joints
   - Verify pull-up resistors (4.7kΩ) are present

2. **Check power**:
   - Display should receive 3.3V on VCC
   - Verify GND connection is solid

3. **Test with different I2C address**:
   - Some displays use 0x3D instead of 0x3C
   - Try changing `reg = <0x3C>` to `reg = <0x3D>` in overlay

### Step 4: ZMK Version Check
1. Check what ZMK version you're using (in `west.yml`)
2. Check if there are known display issues with that version
3. Consider updating to latest ZMK main branch
4. **Warning**: Updating ZMK may require configuration changes

## Recommended Actions

### Immediate Actions

1. **Test External Power Toggle**:
   - Use your ADJ layer keys for `EP_OFF` and `EP_ON`
   - Toggle external power and see if display comes back
   - This is the most likely fix for your issue

2. **Verify Display Works on Fresh Boot**:
   - Flash firmware
   - Power cycle keyboard completely
   - Check if display initializes

3. **Check ZMK Version**:
   - Your `west.yml` pulls from ZMK main branch
   - Check if there have been display-related fixes since your last update

### If Display Works on Boot but Not After Sleep

This confirms **ZMK Issue #674**. Options:

1. **Use External Power Toggle** (workaround):
   - Add a convenient key binding for `&ext_power EP_TOG` (toggle)
   - Use it when display goes blank

2. **Disable Sleep** (not recommended):
   - Set `CONFIG_ZMK_SLEEP=n` in config
   - Will drain battery quickly

3. **Wait for ZMK Fix**:
   - Monitor [ZMK Issue #674](https://github.com/zmkfirmware/zmk/issues/674)
   - This is a known issue being tracked

### If Display Never Works (Even on Boot)

1. **Hardware Check**:
   - Verify all connections
   - Test with multimeter if possible
   - Check for damaged components

2. **Try Alternative I2C Address**:
   - Change to `reg = <0x3D>` in overlay
   - Some displays use different address

3. **Verify ZMK Version Compatibility**:
   - The `"ssd,ssd1306fb-i2c"` compatible string may have been removed
   - Check ZMK changelog for display driver changes
   - May need to update configuration for newer ZMK

## Additional Resources

- [ZMK Display Documentation](https://zmk.dev/docs/config/displays)
- [ZMK Issue #674 - Display blank after external power](https://github.com/zmkfirmware/zmk/issues/674)
- [ZMK Display Feature Status](https://zmk.dev/docs/features/displays) - Note: Display is "proof of concept"
- [KEEBD Display Troubleshooting](https://docs.keebd.com/troubleshooting/display-issues)

## Next Steps

1. **Test external power toggle** - Most likely to work
2. **Verify display works on fresh boot** - Confirms hardware is OK
3. **Check ZMK version and updates** - May need to update configuration
4. **Report findings** - If it's the known issue, you're not alone!

The fact that your keyboard works fine but display doesn't, combined with the timeline (stopped working after ZMK update), strongly suggests this is the known ZMK display re-initialization issue (#674).

