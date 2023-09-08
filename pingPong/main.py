import turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreBored import ScoreBored
PADDLE_POSITION = [(-350, 0), (350, 0)]

screen = Screen()

screen.setup(width=800, height=600)
screen.title("PingPong")
screen.bgcolor("black")
screen.tracer(0)

ball = Ball()
r_paddle = Paddle(PADDLE_POSITION[1])
l_paddle = Paddle(PADDLE_POSITION[0])
l_score = ScoreBored()
r_score = ScoreBored()
l_score.left_score()
r_score.right_score()


screen.listen()
while True:
    time.sleep(0.09)
    screen.update()

    screen.onkey(fun=r_paddle.move_up, key="Up")
    screen.onkey(fun=r_paddle.move_down, key="Down")
    screen.onkey(fun=l_paddle.move_up, key="w")
    screen.onkey(fun=l_paddle.move_down, key="s")
    ball.move()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    if ball.xcor() > 330 and ball.distance(r_paddle) < 50 or ball.xcor() < -330 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    if ball.xcor() > 380:
        l_score.l_score += 1
        l_score.left_score()
        ball.reset_ball()

    if ball.xcor() < -380:
        r_score.r_score += 1
        r_score.right_score()
        ball.reset_ball()

screen.exitonclick()