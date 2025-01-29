import pandas
import turtle
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



data = pandas.read_csv("50_states.csv")
all_states = data['state'].to_list()
guessed_state = []
states_to_learn=[]


while len(guessed_state)<50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States correct", prompt="What's another state's name?").title()
    if answer_state == 'Exit':
        for state in all_states:
            if state not in guessed_state:
                states_to_learn.append(state)
        df = pandas.DataFrame(states_to_learn)
        df.to_csv('states_to_learn.csv')
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)

        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        state_data = data[data.state==answer_state]
        tim.goto(state_data.x.item(), state_data.y.item())
        tim.write(answer_state)





