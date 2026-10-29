"""MicroPython adaptation of Freenove 02 2 ultrasonic ranging car.py example."""
from freenove_car import Car
from time import sleep

car = Car()
try:
    car.servo_angle(90)
    sleep(0.5)
    while True:
        ahead = car.distance_cm()
        if ahead is None or ahead < 25:
            car.stop()
            car.servo_angle(150)
            sleep(0.35)
            left = car.distance_cm() or 0
            car.servo_angle(30)
            sleep(0.35)
            right = car.distance_cm() or 0
            car.servo_angle(90)
            if max(left, right) < 25:
                car.drive(-40, -40)
            elif left > right:
                car.drive(-40, 40)
            else:
                car.drive(40, -40)
            sleep(0.5)
            car.stop()
        else:
            car.drive(40, 40)
        sleep(0.08)
finally:
    car.close()
