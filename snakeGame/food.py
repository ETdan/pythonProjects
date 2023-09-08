from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.color('purple')
        self.penup()
        self.shape('circle')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        x_position = randint(-280, 280)
<<<<<<< HEAD
        y_position = randint(-280, 280)
=======
        y_position = randint(-270, 270)
>>>>>>> 0be6bcfcbc1bb9445fa3484fdede8d14e04d41d3
        self.goto(x_position, y_position)
