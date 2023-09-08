import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
scoreboard.write_score()

car = CarManager()

screen.listen()
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    screen.onkey(fun=player.move, key="Up")

    car.make_cars()
    car.move()

    for c in car.cars:
        if player.distance(c) < 30:
            player.spawn()
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > player.finish_line:
        scoreboard.level += 1
        scoreboard.write_score()
        player.spawn()
        for c in car.cars:
            car.speed_up()

screen.exitonclick()
