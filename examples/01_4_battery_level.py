"""MicroPython adaptation of Freenove 01 4 battery level.py example."""
from freenove_car import Car
from time import sleep

car = Car()
try:
    while True:
        print("Battery ADC:", car.battery_adc(), "Estimated voltage:", car.battery_voltage())
        sleep(0.3)
finally:
    car.close()
