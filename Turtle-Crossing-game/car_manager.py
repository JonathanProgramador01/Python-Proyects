COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import *
import random
class CarManager:
    def __init__(self):
        self.carritos = []
        self.velocidad = 0.1
        self.num_de_carro = 6
        for i in range(random.randint(15,20)):
            self.carritos.append(self.creador_de_carros())

    def creador_de_carros(self):
        turtle = Turtle(shape="square")
        turtle.penup()
        turtle.shapesize(stretch_wid=1, stretch_len=2)
        turtle.color(random.choice(COLORS))
        turtle.goto(random.randint(350, 550), random.randint(-250, 250))
        turtle.setheading(180)
        return turtle

    def move(self):
        for caro in self.carritos:
            caro.forward(5)

    def crear_otro_carrito(self):
        self.carritos.append(self.creador_de_carros())


    def choco(self,player):
        for carro in self.carritos:
            if carro.distance(player)<20:
                return True

    def subir_de_nivel(self):
        self.velocidad = max(0.01, self.velocidad - 0.05)
        self.num_de_carro -= 1
        print(self.velocidad)

    def win(self):
        if self.num_de_carro == 1:
            return True





