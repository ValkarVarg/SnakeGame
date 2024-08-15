from turtle import Turtle
import random

ALIGNMENT = "center"
FONT = ("courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        with open("high_score.txt") as x:
            self.high_score = int(x.read())
        self.color("white")
        self.ht()
        self.goto(0, 280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f" Score  =  {self.current_score}   High Score = {self.high_score}", False, ALIGNMENT, FONT)

    def reset(self):
        if self.current_score > int(self.high_score):
            self.high_score = self.current_score
            with open("high_score.txt", mode="w") as x:
                x.write(f"{self.high_score}")
        self.current_score = 0
        self.update_score()
