from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(1.0, 2.0, 1.0)
        self.color(random.choice(COLORS))
        self.goto(x_cor, y_cor)
        self.car_speed = STARTING_MOVE_DISTANCE

    def move_car(self):
        self.forward(-self.car_speed)

    def inc_speed(self):
        self.car_speed += MOVE_INCREMENT
