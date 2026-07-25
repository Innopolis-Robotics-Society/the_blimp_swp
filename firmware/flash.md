# Flashing MicoAir H743 V2

## Using MicoAir Configurator (USB DFU)

1. Open the [MicoAir Configurator](https://micoair.com/configurator/)
2. Connect MicoAir H743 V2 to your computer via USB
3. Navigate to the **Firmware** menu
4. Select the `ardumotorblimp_with_bl.hex` file from `firmware/build/`
5. Click **Flash**
6. **Disconnect and reconnect USB twice** (important for H743!)

## Alternative: Mission Planner

1. Connect the flight controller via USB
2. Go to **SETUP → Install Firmware → Load custom firmware**
3. Select `ardumotorblimp.apj`
4. Disconnect and reconnect USB twice

## Alternative: DFU via STM32CubeProgrammer

For initial firmware load or recovery:

1. Put the board into DFU mode:
   - Hold the **BOOT** button on the flight controller
   - Connect USB while holding the button
   - Release the button after connecting
2. Open STM32CubeProgrammer
3. Select **USB1** as the connection type
4. Click **Connect**
5. Load `ardumotorblimp_with_bl.hex`
6. Click **Start Programming**
7. Disconnect USB and reconnect normally

**Note:** `ardumotorblimp_with_bl.hex` includes the bootloader and is ready for DFU flashing. `ardumotorblimp.apj` is for use with ArduPilot-compatible tools (Mission Planner, MicoAir Configurator).
