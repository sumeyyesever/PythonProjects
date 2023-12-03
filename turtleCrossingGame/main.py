import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=500)
screen.tracer(0)
player = Player()
cars = []
scoreboard = Scoreboard()


for _ in range(30):
    x_cor = random.randint(-300, 300)
    y_cor = random.randint(-200, 200)
    car = CarManager(x_cor, y_cor)
    cars.append(car)


screen.listen()
screen.onkey(player.move_player, "Up")

game_is_on = True
game_number = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.create_scoreboard()
    for car in cars:
        car.move_car()
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    game_number += 1
    if game_number % 6 == 0:
        y_cor = random.randint(-200, 200)
        car = CarManager(300, y_cor)
        cars.append(car)

    if player.is_finish_line():  # this is not working right
        scoreboard.level_count()
        for car in cars:
            car.inc_speed()


screen.exitonclick()
