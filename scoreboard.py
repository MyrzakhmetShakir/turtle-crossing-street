from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.count = 1
        self.setpos(-260, 240)
        self.write(f"Level {self.count}", font=FONT)

    def add(self):
        self.count += 1
        self.clear()
        self.write(f"Level {self.count}", font=FONT)

    def game_over(self):
        self.setpos(-70, 0)
        self.write("GAME OVER", font=FONT)