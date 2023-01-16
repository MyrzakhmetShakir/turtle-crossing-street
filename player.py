STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.setpos(STARTING_POSITION)

    def up(self):
        self.forward(10)

    def reset(self):
        self.setpos(STARTING_POSITION)

