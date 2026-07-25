# Flashing MicoAir H743 V2

## File formats

| File | Format | Use case |
|------|--------|----------|
| `ardumotorblimp.apj` | ArduPilot JSON | MicoConfigurator, Mission Planner, QGroundControl |
| `ardumotorblimp_with_bl.hex` | Intel HEX (with bootloader) | STM32CubeProgrammer, dfu-util, MicoConfigurator (DFU) |

---

## Two flashing processes

### Regular flashing (USB serial)

This is the normal way to update firmware when ArduPilot is already running on the board.

**How it works:**
1. You connect the flight controller via USB while ArduPilot is running
2. ArduPilot's bootloader listens on the serial/USB port for upload commands
3. The flashing tool sends the firmware data over the serial connection
4. The bootloader writes it to flash memory (application area only, bootloader is preserved)
5. After flashing, the board reboots into the new firmware

**When to use:**
- Routine firmware updates
- ArduPilot is already installed and working
- The board shows up as `ArduPilot(COMx)` in device manager

**Requirements:**
- ArduPilot bootloader must be present on the board
- USB cable connected to the flight controller
- Board powered on (via USB)

**What gets written:**
- Only the application area (`0x08020000` and above)
- Bootloader (`0x08000000`) is NOT overwritten

**After flashing:**
- Disconnect USB
- Reconnect USB twice (important for H743!)
- Board should boot into new firmware

### DFU flashing (Device Firmware Upgrade)

This is a low-level flashing method that writes directly to flash memory via the built-in STM32 DFU bootloader in ROM.

**How it works:**
1. You put the board into DFU mode by holding the BOOT button during power-up
2. The STM32H743's ROM bootloader activates and appears as a USB DFU device
3. The flashing tool communicates with the ROM bootloader over USB
4. It writes the entire flash image (bootloader + application) starting at `0x08000000`
5. After flashing, you disconnect and reconnect USB normally

**When to use:**
- First-time firmware installation (board has no ArduPilot bootloader)
- Recovery when the board is bricked or won't boot
- Switching between firmware types (ArduPilot ↔ PX4 ↔ Betaflight)
- When regular USB flashing fails

**Requirements:**
- BOOT button on the flight controller
- USB cable
- DFU driver installed (Windows: via Zadig, Linux/macOS: works out of the box)

**What gets written:**
- Bootloader (`0x08000000`, 128 KB)
- Application (`0x08020000`, ~1.9 MB)
- Everything in the `_with_bl.hex` file

**After flashing:**
- Disconnect USB
- Reconnect USB normally (no double-reconnect needed)
- Board should boot into new firmware

### Comparison

| | Regular (USB serial) | DFU |
|---|---|---|
| Bootloader preserved | Yes | No (overwritten) |
| Requires running firmware | Yes | No |
| Speed | ~30 sec | ~1-2 min |
| File format | `.apj` | `_with_bl.hex` |
| Recovery capability | No | Yes |
| Driver needed | No (CDC) | Yes (Windows: Zadig) |

---

## Methods

### Method 1: MicoConfigurator (recommended)

Web-based tool, no installation required. Supports both USB and DFU modes.

1. Open the [MicoAir Configurator](https://micoair.com/configurator/)
2. Connect MicoAir H743 V2 to your computer via USB
3. Navigate to the **Firmware** menu
4. Select `ardumotorblimp_with_bl.hex` (DFU) or `ardumotorblimp.apj` (USB)
5. Click **Flash**
6. **Disconnect and reconnect USB twice** (important for H743!)

### Method 2: Mission Planner

Regular USB serial flashing.

1. Connect the flight controller via USB
2. Go to **SETUP → Install Firmware → Load custom firmware**
3. Select `ardumotorblimp.apj`
4. Disconnect and reconnect USB twice

### Method 3: QGroundControl

Regular USB serial flashing.

1. Navigate to **Firmware** page
2. Check **Advanced settings**
3. Choose **Custom firmware file**
4. Select `ardumotorblimp.apj`
5. Click **Ok** to flash

### Method 4: STM32CubeProgrammer (DFU)

Low-level DFU flashing via GUI tool.

#### Enter DFU mode
1. Hold the **BOOT** button on the flight controller
2. Connect USB while holding the button
3. Release the button after connecting

#### Flash
1. Open [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html)
2. Select **USB1** as connection type
3. Click **Connect**
4. Load `ardumotorblimp_with_bl.hex`
5. Click **Start Programming**
6. Disconnect USB and reconnect normally

#### Windows DFU driver
If the board is not detected in DFU mode:
1. Download [Zadig](https://zadig.akeo.ie/)
2. Options → List All Devices
3. Select **DFU in FS Mode**
4. Choose **WinUSB** → Replace Driver

### Method 5: dfu-util (Linux command line)

Low-level DFU flashing via CLI.

```bash
# Install dfu-util
sudo apt install dfu-util

# Enter DFU mode (hold BOOT + connect USB)

# Flash with bootloader
dfu-util -a 0x08000000 -D firmware/build/ardumotorblimp_with_bl.hex

# Or flash application only (without bootloader)
dfu-util -a 0x08020000 -D firmware/build/ardumotorblimp.bin
```

### Method 6: waf --upload (serial bootloader)

Builds and uploads in one step via serial bootloader.

```bash
cd ardupilot
source venv/bin/activate
./waf configure --board MicoAir743v2
./waf build --target bin/ardublimp --upload
```

### Method 7: uploader.py (Python script)

ArduPilot's built-in uploader for serial bootloader.

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
