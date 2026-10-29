"""MicroPython adaptation of Freenove 04 2 track car.py example."""
from freenove_car import Car
from time import sleep

car = Car()
try:
    # Verify whether black reads as 0 or 1 on your sensors.
    BLACK = 0
    while True:
        left, middle, right = (v == BLACK for v in car.track_values())
        if middle and not left and not right:
            car.drive(40, 40)
        elif left and not right:
            car.drive(-25, 40)
        elif right and not left:
            car.drive(40, -25)
        else:
            car.stop()
        sleep(0.03)
finally:
    car.close()
