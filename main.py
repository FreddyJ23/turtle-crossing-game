import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
import random
from scoreboard import Scoreboard
FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    # Detect collision with cars
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
    # check if player has reach line
    if player.ycor() > FINISH_LINE_Y:
        player.restart()
        car_manager.increase_speed()
        # Update level
        scoreboard.update_level()


screen.exitonclick()
