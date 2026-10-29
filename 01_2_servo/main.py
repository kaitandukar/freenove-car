"""MicroPython adaptation of Freenove 01 2 servo.py example."""
from freenove_car import Car
from time import sleep

car = Car()
try:
    car.servo_angle(90)
    sleep(1)
    while True:
        car.servo_sweep(90, 30)
        car.servo_sweep(30, 150)
        car.servo_sweep(150, 90)
finally:
    car.close()
