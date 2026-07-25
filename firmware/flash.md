# Flashing MicoAir H743 V2

## File formats

| File | Format | Use case |
|------|--------|----------|
| `ardumotorblimp.apj` | ArduPilot JSON | MicoConfigurator, Mission Planner, QGroundControl |
| `ardumotorblimp_with_bl.hex` | Intel HEX (with bootloader) | STM32CubeProgrammer, dfu-util, MicoConfigurator (DFU) |

---

## Method 1: MicoConfigurator (recommended)

Web-based tool, no installation required. Supports both USB and DFU modes.

1. Open the [MicoAir Configurator](https://micoair.com/configurator/)
2. Connect MicoAir H743 V2 to your computer via USB
3. Navigate to the **Firmware** menu
4. Select `ardumotorblimp_with_bl.hex` (DFU) or `ardumotorblimp.apj` (USB)
5. Click **Flash**
6. **Disconnect and reconnect USB twice** (important for H743!)

## Method 2: Mission Planner

1. Connect the flight controller via USB
2. Go to **SETUP → Install Firmware → Load custom firmware**
3. Select `ardumotorblimp.apj`
4. Disconnect and reconnect USB twice

## Method 3: QGroundControl

1. Navigate to **Firmware** page
2. Check **Advanced settings**
3. Choose **Custom firmware file**
4. Select `ardumotorblimp.apj`
5. Click **Ok** to flash

## Method 4: STM32CubeProgrammer (DFU)

Use for first flash, recovery, or when other methods fail.

### Enter DFU mode
1. Hold the **BOOT** button on the flight controller
2. Connect USB while holding the button
3. Release the button after connecting

### Flash
1. Open [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html)
2. Select **USB1** as connection type
3. Click **Connect**
4. Load `ardumotorblimp_with_bl.hex`
5. Click **Start Programming**
6. Disconnect USB and reconnect normally

### Windows DFU driver
If the board is not detected in DFU mode:
1. Download [Zadig](https://zadig.akeo.ie/)
2. Options → List All Devices
3. Select **DFU in FS Mode**
4. Choose **WinUSB** → Replace Driver

## Method 5: dfu-util (Linux command line)

```bash
# Install dfu-util
sudo apt install dfu-util

# Enter DFU mode (hold BOOT + connect USB)

# Flash
dfu-util -a 0x08000000 -D firmware/build/ardumotorblimp_with_bl.hex

# Or from .bin (without bootloader, at flash offset)
dfu-util -a 0x08020000 -D firmware/build/ardumotorblimp.bin
```

## Method 6: waf --upload (serial bootloader)

Builds and uploads in one step via serial bootloader (requires USB connection with ArduPilot already running):

```bash
cd ardupilot
source venv/bin/activate
./waf configure --board MicoAir743v2
./waf build --target bin/ardublimp --upload
```

## Method 7: uploader.py (Python script)

ArduPilot's built-in uploader for serial bootloader:

```bash
cd ardupilot
python Tools/scripts/uploader.py build/MicoAir743v2/bin/ardublimp.apj
```

---

## Flash memory map (STM32H743)

| Address | Size | Content |
|---------|------|---------|
| `0x08000000` | 128 KB | Bootloader |
| `0x08020000` | ~1.9 MB | Application (ArduMotorBlimp) |
| Total | 2048 KB | Flash |
