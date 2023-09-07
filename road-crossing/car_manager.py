import time
from turtle import Turtle
from random import choice,randint


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.make_cars()
        self.speed = STARTING_MOVE_DISTANCE

    def make_cars(self):
        random_number = randint(1, 6)
        if random_number == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.color(choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(250, randint(-260, 260))
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(10)

    def speed_up(self):
        self.speed += MOVE_INCREMENT

