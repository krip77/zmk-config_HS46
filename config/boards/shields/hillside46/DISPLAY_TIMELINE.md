# Display Issue Timeline

## Repository and Keyboard History

### Repository Creation
- **November 2021**: Repository forked/created from mmccoyd/zmk-config
- **June 2022**: Hillside 46 configuration added (copied from Hillside 52)

### Keyboard Build
- **Q3/Q4 2024**: Keyboard was physically built
- **October 2024**: Multiple attempts to fix display (October 22, 2024)

## Display Issue Timeline

### Key Dates
- **Q3/Q4 2024**: Keyboard built - Display may have never worked, or worked briefly
- **October 22, 2024**: Multiple attempts to fix display configuration
  - Updated `hillside46_left.overlay` multiple times
  - Updated `hillside46.dtsi` multiple times
  - Updated `Kconfig.defconfig` and `Kconfig.shield`
  - Added display configuration (commented: "Lagt till detta för att dispaylen skall funka 2024-10-22")

### What This Tells Us

1. **Display may have never worked**: If you built the keyboard in Q3/Q4 2024 and immediately tried to fix it in October, the display may have never worked from the start.

2. **ZMK update timing**: The display configuration was added in October 2024, suggesting:
   - Either the display was never configured initially
   - Or a ZMK update broke it shortly after building
   - Or the display worked initially but stopped after a ZMK update

3. **"Hillside View" project**: You mentioned looking at a "hillside view" project. This might be:
   - A different keyboard variant
   - A different firmware configuration
   - A reference design or example

## Questions to Clarify

1. **Did the display ever work?**
   - Did it work when you first built the keyboard?
   - Or has it been non-functional from the start?

2. **When did it stop working?**
   - If it worked initially, when exactly did it stop?
   - Was it after a specific ZMK update?
   - Or after a firmware flash?

3. **"Hillside View" project connection**
   - Did you use any code/config from a "hillside view" project?
   - Was that a different keyboard or firmware setup?
   - Could that have affected the display configuration?

## Next Steps

Based on this timeline, we should:

1. **Verify if display ever worked**: Test with the configuration from commit `24e0535` (October 22, 2024) which was when you added display config
2. **Check for "hillside view" references**: See if there's a different configuration that might have worked
3. **Investigate ZMK changes**: Look for ZMK display driver changes between when you built the keyboard and when you tried to fix it

## Current Status

- Configuration matches the last known attempt (October 2024)
- Display still not working
- Need to determine if this is:
  - A configuration issue (never worked)
  - A ZMK update issue (stopped working)
  - A hardware issue (display not properly connected)

