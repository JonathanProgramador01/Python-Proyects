from turtle import *



STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.setheading(90)


    def move(self):
        self.forward(20)


    def revision_de_meta(self,):
        if self.ycor() >= 280:
            self.goto(STARTING_POSITION)
            print("Se llego a la metaaaa")
            return True

