"""MicroPython adaptation of Freenove 01 3 buzzer.py example."""
from freenove_car import Car
from time import sleep

car = Car()
try:
    for _ in range(3):
        for _ in range(4):
            car.beep()
            sleep(0.1)
        sleep(0.4)
finally:
    car.close()
