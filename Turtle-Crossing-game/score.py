FONT = ("Courier", 24, "normal")
from turtle import *

class Scoreboard(Turtle):
    def __init__(self):
        self.score = 1
        super().__init__(visible=0)
        self.penup()
        self.goto(-220,250)
        self.write(f"Level {self.score}",align="center",font=FONT)
    def aumentar_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score {self.score}", align="center", font=FONT)
    def game_over(self):
        self.reset()
        self.write("GAME OVER",align="center",font=FONT)

    def win(self):
        self.reset()
        self.write("YOUU WIN ",align="center", font=FONT)