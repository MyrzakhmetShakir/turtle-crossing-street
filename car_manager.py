import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.cars = []

    def generate(self):
        r = random.randint(1, 7)
        if r == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(1, 2.5)
            new_car.goto(320, random.randint(-260, 280))
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            self.cars.append(new_car)

    def move(self):
        speed = STARTING_MOVE_DISTANCE + (self.level-1) * 10
        for car in self.cars:
            car.forward(speed)



