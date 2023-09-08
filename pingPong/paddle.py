<<<<<<< HEAD
from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.penup()
        self.goto(position)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.move_up()

    def move_up(self):
        if self.ycor() < 255:
            self.sety(self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -255:
=======
from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.penup()
        self.goto(position)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.move_up()

    def move_up(self):
        if self.ycor() < 255:
            self.sety(self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -255:
>>>>>>> 0be6bcfcbc1bb9445fa3484fdede8d14e04d41d3
            self.sety(self.ycor() - 20)