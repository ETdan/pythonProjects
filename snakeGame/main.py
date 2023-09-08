from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreBord import ScoreBored

FILE = open("data.txt", mode="r+")

HIGH_SCORE = FILE.read()


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreBord = ScoreBored(HIGH_SCORE)
scoreBord.write_score()
screen.listen()
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.right, key='Right')
screen.onkey(fun=snake.left, key='Left')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreBord.write_score()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -282:
        snake.reset()
        scoreBord.reset(FILE)

    for s in snake.segments[1:]:
        if snake.head.distance(s) < 10:
            snake.reset()
            scoreBord.reset(FILE)

screen.exitonclick()
FILE.close()
