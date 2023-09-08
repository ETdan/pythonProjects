from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreBord import ScoreBored

<<<<<<< HEAD
=======
FILE = open("data.txt", mode="r+")

HIGH_SCORE = FILE.read()


>>>>>>> 0be6bcfcbc1bb9445fa3484fdede8d14e04d41d3
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
<<<<<<< HEAD
scoreBord = ScoreBored()
=======
scoreBord = ScoreBored(HIGH_SCORE)
>>>>>>> 0be6bcfcbc1bb9445fa3484fdede8d14e04d41d3
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
<<<<<<< HEAD
        game_is_on = False
        scoreBord.game_over()

    for s in snake.segments[1:]:
        if snake.head.distance(s) < 10:
            game_is_on = False
            scoreBord.game_over()

screen.exitonclick()
=======
        snake.reset()
        scoreBord.reset(FILE)

    for s in snake.segments[1:]:
        if snake.head.distance(s) < 10:
            snake.reset()
            scoreBord.reset(FILE)

screen.exitonclick()
FILE.close()
>>>>>>> 0be6bcfcbc1bb9445fa3484fdede8d14e04d41d3
