import turtle
import pandas
#Tdo esto de aqui es parte de mi cofiguracion
screen = turtle.Screen()
image = "blank_states_img.gif"
screen.title("U.S States Game")
screen.setup(width=725, height=491)
screen.addshape(image)
turtle.shape(image)


score = 0
states_correct = []
data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
text = turtle.Turtle(visible=0)
text.penup()

def repasar(states_correct,states):
    repasar_stados = []
    for i in range(len(states)):
        if states[i] not in states_correct:
            repasar_stados.append(states[i])
    repaso = {
        "state": repasar_stados
    }
    archivo = pandas.DataFrame(repaso)
    archivo.to_csv("Repaso.csv")




while len(states_correct) >= 49:
    answer = screen.textinput(title=f"{score}/50 Guees and State", prompt="What's another state name? ")

    if answer != None:
        if answer.title() in states:
            score += 1
            cordenadas = data[data["state"] == answer.title()]
            x = cordenadas["x"].values[0]
            y = cordenadas["y"].values[0]
            text.goto(x, y)
            text.write(cordenadas["state"].values[0])
            states_correct.append(answer.title())

    else:
        game_is_on = False
        repasar(states_correct,states)





screen.exitonclick()



