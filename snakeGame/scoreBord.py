from turtle import Turtle


class ScoreBored(Turtle):

    score = -1

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)

    def write_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=("Arial", 12, "bold"))

    def game_over(self):
        self.pendown()
        self.goto(0, 0)
        self.write(arg=f"Game over", move=False, align="center", font=("Arial", 12, "bold"))
        self.pendown()
