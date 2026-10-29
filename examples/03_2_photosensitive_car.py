"""MicroPython adaptation of Freenove 03 2 photosensitive car.py example."""
from freenove_car import Car
from time import sleep

car = Car()
try:
    car.beep()
    while True:
        left, right = car.light_values()
        # Adjust threshold and direction based on actual sensor response.
        if abs(left - right) < 70:
            car.drive(35, 35)
        elif left > right:
            car.drive(-25, 35)
        else:
            car.drive(35, -25)
        sleep(0.08)
finally:
    car.close()
