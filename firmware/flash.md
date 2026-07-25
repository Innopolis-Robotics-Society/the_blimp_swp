# Flashing MicoAir H743 V2

## Method 1: MicoConfigurator (recommended)

1. Open the [MicoAir Configurator](https://micoair.com/configurator/)
2. Connect MicoAir H743 V2 to your computer via USB
3. Navigate to the **Firmware** menu
4. Select the `ardumotorblimp_with_bl.hex` file from `firmware/build/`
5. Click **Flash**
6. **Disconnect and reconnect USB twice** (important for H743!)

**Note:** MicoConfigurator supports DFU flashing directly — no need for STM32CubeProgrammer.

## Method 2: Mission Planner

1. Connect the flight controller via USB
2. Go to **SETUP → Install Firmware → Load custom firmware**
3. Select `ardumotorblimp.apj`
4. Disconnect and reconnect USB twice

## Method 3: STM32CubeProgrammer (DFU — for first flash or recovery)

Use this when the board has no ArduPilot bootloader or needs recovery.

### Enter DFU mode
1. Hold the **BOOT** button on the flight controller
2. Connect USB while holding the button
3. Release the button after connecting

### Flash
1. Open [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html)
2. Select **USB1** as connection type
3. Click **Connect**
4. Load `ardumotorblimp_with_bl.hex` from `firmware/build/`
5. Click **Start Programming**
6. Disconnect USB and reconnect normally

### Windows DFU driver
If the board is not detected in DFU mode:
1. Download [Zadig](https://zadig.akeo.ie/)
2. Options → List All Devices
3. Select **DFU in FS Mode**
4. Choose **WinUSB** → Replace Driver

## Method 4: QGroundControl (for PX4)

1. Navigate to **Firmware** page
2. Check **Advanced settings**
3. Choose **Custom firmware file**
4. Select the `.apj` file
5. Click **Ok** to flash

## File formats

| File | Format | Use case |
|------|--------|----------|
| `ardumotorblimp.apj` | ArduPilot JSON | MicoConfigurator, Mission Planner, QGroundControl |
| `ardumotorblimp_with_bl.hex` | Intel HEX (with bootloader) | STM32CubeProgrammer DFU |
