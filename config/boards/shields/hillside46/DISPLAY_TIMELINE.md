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

3. **"Hillside View" project**: You mentioned looking at a "hillside view" project. This is:
   - A separate GitHub repository you have
   - A project primarily using nice!view displays (different from I2C SSD1306)
   - **Key Information**: Someone in that project successfully got an I2C display working
   - **Important**: You used that I2C display configuration, and it worked until a ZMK update broke it
   - This suggests the working configuration might have been different from what's currently in this repo

## Questions to Clarify

1. **Did the display ever work?**
   - Did it work when you first built the keyboard?
   - Or has it been non-functional from the start?

2. **When did it stop working?**
   - If it worked initially, when exactly did it stop?
   - Was it after a specific ZMK update?
   - Or after a firmware flash?

3. **"Hillside View" project connection**
   - **Confirmed**: You used I2C display configuration from the [HillSideView project](https://github.com/wannabecoffeenerd/HillSideView)
   - **Confirmed**: That configuration worked until a ZMK update broke it
   - **Found**: The working configuration was in commit `8d2b158` (November 14, 2024)
   - **Restored**: Configuration using `"solomon,ssd1306fb"` with additional parameters (`segment-offset`, `multiplex-ratio`, `segment-remap`, `com-invdir`, `prechargep`)
   - **Reference**: [Reddit discussion about HillSideView](https://www.reddit.com/r/ErgoMechKeyboards/comments/17opz7v/hillsideview_a_modified_hillside_46_with_niceview/)

4. **dalewking contribution**
   - **Confirmed**: You were in contact with "dalewking" who managed to get the I2C display working
   - **Note**: The restored configuration may have been based on or influenced by dalewking's work
   - **Action**: If you have any messages, emails, or forum posts from dalewking with configuration details, those could provide additional insights or alternative solutions

## Resolution

**November 15, 2025**: Found and restored the working I2C display configuration:

1. **Found working configuration**: Located in commit `8d2b158` which used the configuration from the HillSideView project
2. **Restored configuration**: Updated `hillside46_left.overlay` to use:
   - Compatible string: `"solomon,ssd1306fb"` (instead of `"ssd,ssd1306fb-i2c"`)
   - Additional display parameters: `segment-offset`, `page-offset`, `display-offset`, `multiplex-ratio`, `segment-remap`, `com-invdir`, `prechargep`
   - Display node label: `oled` (instead of `ssd1306`)
3. **Next step**: Test the restored configuration to verify the display works

## Current Status

- **Configuration restored**: Using the working configuration from HillSideView project (commit `8d2b158`)
- **Configuration details**:
  - Compatible string: `"solomon,ssd1306fb"` with full parameter set
  - I2C address: `0x3c` (lowercase)
  - Display node: `oled` with all display parameters
- **Next action**: Flash firmware and test if display works with restored configuration
- **If still not working**: May need to investigate:
  - Hardware connections (SDA/SCL, power, ground)
  - ZMK version compatibility with `"solomon,ssd1306fb"` driver
  - Display initialization timing issues

