"""MicroPython adaptation of Freenove 03 1 photosensitive.py example."""
from freenove_car import Car
from time import sleep

car = Car()
try:
    while True:
        print("Light (left, right):", car.light_values())
        sleep(0.5)
finally:
    car.close()
