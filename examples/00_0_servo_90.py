"""MicroPython adaptation of Freenove 00 0 servo 90.py example."""
from freenove_car import Car
from time import sleep

car = Car()
try:
    car.servo_angle(90)
    sleep(1)
finally:
    car.close()
