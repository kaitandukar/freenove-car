"""Port of 01.1_Car_Move_and_Turn.ino; wheels will move!"""
from freenove_car import Car
from time import sleep

car = Car()
steps = [
    (50,50,50,50), (-50,-50,-50,-50),
    (-50,-50,50,50), (50,50,-50,-50),
    (-50,50,-50,50), (50,-50,50,-50),
    (-50,50,-50,50), (0,-50,0,-50),
    (50,0,50,0), (-50,0,-50,0),
]
try:
    while True:
        for speeds in steps:
            car.move(*speeds)
            sleep(1)
            car.stop()
            sleep(1)
finally:
    car.stop()
