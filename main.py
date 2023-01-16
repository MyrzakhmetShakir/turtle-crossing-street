import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("#EFA3C8")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car = CarManager()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.generate()
    car.move()
    for one_car in car.cars:
        if player.distance(one_car) < 31:
            if 23 > player.ycor() - one_car.ycor() > -23:
                scoreboard.game_over()
                game_is_on = False
        elif player.ycor() >= 300:
            player.reset()
            scoreboard.add()
            car.level += 1


screen.exitonclick()



