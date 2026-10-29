# Freenove Mecanum wheels — MicroPython port (in progress)

Target: Raspberry Pi Pico/Pico W, MicroPython firmware. This is **not yet a complete 1:1 conversion** of the Arduino Sketches folder. All included examples are untested on physical hardware.

## Install

1. Flash MicroPython on your Pico/Pico W and open Thonny.
2. Copy `freenove_car.py` to the Pico root.
3. Open one file from `examples/` in Thonny and run it on the Pico.
4. Test with wheels lifted off the floor first. Use Stop in Thonny to halt a running example.

## Included

Motor movement, servo, buzzer, battery ADC, ultrasonic distance and avoidance, light sensors/light-following, and line sensors/line-following.

## Limitations

- Light-following, line-following and obstacle avoidance are simplified adaptations, **not exact translations** of Freenove's algorithms; tune on your hardware.
- Battery voltage coefficient is an estimate; calibrate before using it to determine battery safety.
- Matrix display (VK16K33), WS2812 LEDs, infrared remote (NEC decoding), Wi-Fi app protocol, and both multifunction-car sketches remain **unconverted**.
- GPIO mapping is from Freenove's Mecanum source: motors 18/19,21/20,7/6,9/8; servo 13; buzzer 2; ultrasonic 4/5; battery 26; light 28/27; tracking 12/11/10.
- Do not power motors directly from Pico GPIO. Use the original motor driver board.
- The original C++ uses custom libraries and some examples require extra modules. The conversion does not implement those modules yet.
