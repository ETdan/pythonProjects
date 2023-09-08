from turtle import Turtle

TOP_BOTTOM_BORDERS = 280


class Ball(Turtle):

    # def __init__(self):
    #     super().__init__()
        # self.y_move = 10

    def __init__(self):
        super().__init__()
        # super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("fast")
        self.x_move = 10
        self.y_move = 10

        # self.shapesize(stretch_wid=10, stretch_len=10)

    def move(self):
        self.setx(self.xcor() + self.x_move)
        self.sety(self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        if self.x_move > 0:
            self.x_move += 2
        else:
            self.x_move -= 2

        self.x_move *= -1

    def reset_ball(self):
        self.goto(0, 0)
        self.bounce_x()
        self.x_move = 10
