from turtle import Turtle




class ScoreBored(Turtle):

    def __init__(self, HIGH_SCORE):
        super().__init__()
        self.score = -1
        self.high_score = int(HIGH_SCORE)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)

    def write_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align="center", font=("Arial", 12, "bold"))

    def reset(self, FILE):
        if self.score > self.high_score:
            self.high_score = self.score
            FILE.write(str(self.high_score))
        self.score = 0
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align="center", font=("Arial", 12, "bold"))
        return self.high_score if self.high_score > self.score else self.score

    # def game_over(self):
    #     self.pendown()
    #     self.goto(0, 0)
    #     self.write(arg=f"Game over", move=False, align="center", font=("Arial", 12, "bold"))
    #     self.pendown()
