"""Port of 02.1_Ultrasonic_Ranging.ino."""
from freenove_car import Car
from time import sleep

car = Car()
try:
    car.servo_angle(90)
    sleep(.5)
    while True:
        for angle in (150,90,30,90):
            car.servo_angle(angle)
            sleep(.5)
            print('Distance:', car.distance_cm(), 'cm')
finally:
    car.stop()
