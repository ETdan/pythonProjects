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
            self.sety(self.ycor() - 20)