"""MicroPython adaptation of Freenove 04 1 tracking sensor.py example."""
from freenove_car import Car
from time import sleep

car = Car()
try:
    while True:
        print("Tracking (L, M, R):", car.track_values())
        sleep(0.5)
finally:
    car.close()
