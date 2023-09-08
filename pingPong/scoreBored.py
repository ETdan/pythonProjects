<<<<<<< HEAD
from turtle import Turtle


class ScoreBored(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-100, 200)

    def left_score(self):
        self.clear()
        self.goto(x=-100, y=200)
        self.write(f"{self.l_score}",False, "center",  ("Arial", 64, "normal"))

    def right_score(self):
        self.clear()
        self.goto(x=100, y=200)
=======
from turtle import Turtle


class ScoreBored(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-100, 200)

    def left_score(self):
        self.clear()
        self.goto(x=-100, y=200)
        self.write(f"{self.l_score}",False, "center",  ("Arial", 64, "normal"))

    def right_score(self):
        self.clear()
        self.goto(x=100, y=200)
>>>>>>> 0be6bcfcbc1bb9445fa3484fdede8d14e04d41d3
        self.write(f"{self.r_score}",False, "center",  ("Arial", 64, "normal"))