# Freenove Mecanum Car — MicroPython examples

Each example is in its own folder. Every folder contains:
- `main.py` — the example program
- `freenove_car.py` — the required hardware driver

## Upload using Thonny (Lubuntu)
1. Connect the Pico and choose **MicroPython (Raspberry Pi Pico)** in Thonny.
2. Open the folder of the example you want.
3. Upload **both files** from that folder to the **root** of the Pico (not into a subfolder).
   In Thonny, enable **View → Files**, then right-click each file on your
   computer and choose **Upload to /**. Alternatively use **File → Save as →
   Raspberry Pi Pico** for each file.
4. The Pico should show `/main.py` and `/freenove_car.py`.
5. Click **Run** (F5). On subsequent boots, `main.py` runs automatically.

## Changing example
Stop the current program in Thonny. Upload the two files from a DIFFERENT
example folder to the Pico root, replacing the existing `main.py` and
`freenove_car.py`. Only one example is installed as `/main.py` at a time.

## Safety and status
**Raise the wheels off the ground before running a driving example.**
These files are adaptations from the previous expanded package and have
NOT been hardware-tested. Obstacle avoidance, line following, and light
following are simplified adaptations; battery measurement needs calibration.
The LED matrix, RGB LEDs, infrared remote, Wi-Fi app protocol and
multifunction sketches have not been converted yet.

GPIO mappings and behavior follow the original expanded package.
