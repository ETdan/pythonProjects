from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()

    def write_score(self):
        self.hideturtle()
        self.clear()
        self.goto(-290, 260)
        self.write(arg=f"Level: {self.level}", move=False, align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", move=False, align="center", font=FONT)

