import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from score import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#686D76")
screen.tracer(0)


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()



game_is_on = True
level = 0

while game_is_on:
    time.sleep(round(car_manager.velocidad,2))
    screen.update()



    screen.onkey(player.move, "Up")
    screen.listen()


    if player.revision_de_meta(): # que paso al siguiente nivelll vllegue al tope
        car_manager.subir_de_nivel()
        scoreboard.aumentar_score()


#Que se muevan mis carros
    car_manager.move()

#creador de carros
    if level >= car_manager.num_de_carro: # esto se refiera a que cada ves que pasen eñl loop 6 veces me crea un nuevo carro pero si lo redusco me va a crear carros mas rapidooo entonces eso va aumentar la dificultad
        car_manager.crear_otro_carrito()
        level = 0
        print("Este es ni num_carro:",car_manager.num_de_carro)
        print("creadon carro")
    else:
        level += 1
    print(level)

    if car_manager.choco(player):
        game_is_on = False
        scoreboard.game_over()


    #comprobar si gannee
    if car_manager.win():
        scoreboard.win()
        break


screen.exitonclick()


