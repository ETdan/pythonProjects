from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.finish_line = FINISH_LINE_Y
        self.spawn()
        self.left(90)

    def spawn(self):
        self.goto(STARTING_POSITION)

    def move(self):
        self.sety(self.ycor() + MOVE_DISTANCE)




