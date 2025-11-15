# Flashing Firmware to Hillside 46 Split Keyboard

## Important: You MUST flash firmware to BOTH halves!

For split keyboards, you need separate firmware files for the left and right halves. Both halves must be flashed for the keyboard to work properly.

## Entering Bootloader Mode Manually

Since your keyboard shortcut isn't working, use the **physical reset button** on the nice!nano board:

### Method 1: Double-tap Reset Button (Recommended)
1. **Locate the reset button** on your nice!nano v2 board (small button on the board)
2. **Double-tap** the reset button quickly (press twice in quick succession)
3. The board should enter bootloader mode (you may see a new USB device appear)

### Method 2: Reset Button + Power
1. **Press and hold** the reset button
2. While holding reset, **disconnect and reconnect** power (or USB)
3. **Release** the reset button
4. The board should enter bootloader mode

## Flashing Firmware

### Step 1: Flash the LEFT half
1. Put the **LEFT** half into bootloader mode (using reset button method above)
2. Flash the firmware file: `hillside46_left-nice_nano_v2-zmk.uf2`
   - On Windows/Mac: The board will appear as a USB drive. Drag and drop the `.uf2` file onto it.
   - On Linux: You may need to use `uf2conv` or copy the file to `/media/BOOT/`

### Step 2: Flash the RIGHT half
1. Put the **RIGHT** half into bootloader mode (using reset button method above)
2. Flash the firmware file: `hillside46_right-nice_nano_v2-zmk.uf2`
   - Same process as above

### Step 3: Pair the halves
1. After flashing both halves, they should automatically pair
2. The **LEFT** half is typically the central side (connects to your computer)
3. If they don't pair automatically, you may need to reset both halves once more

## Troubleshooting

- **If one half won't enter bootloader mode**: Try the reset button method multiple times, or try holding reset while plugging in USB
- **If halves won't pair**: Make sure both have the correct firmware (left firmware on left, right firmware on right)
- **If keyboard still doesn't work**: Verify you downloaded the correct firmware files for both halves

## Finding Your Firmware Files

After building, you should have two separate `.uf2` files:
- `hillside46_left-nice_nano_v2-zmk.uf2` (for LEFT half)
- `hillside46_right-nice_nano_v2-zmk.uf2` (for RIGHT half)

Make sure you flash the correct file to each half!
