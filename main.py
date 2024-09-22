import turtle
import  pandas
data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
# state_list = data.state.to_list()

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

guessed_states = []


answer_state = screen.textinput(title=f"Guess the State : {len(guessed_states)}/50", prompt="what's another state's name?").title()
print(answer_state)
while len(guessed_states)< 50 :
    if answer_state == 'Exit':
        missing_states = []
        for state in state_list:
            if state not in guessed_states:
                missing_states.append(state)
                new_data = pandas.DataFrame(missing_states)
                new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in state_list:
        guessed_states.append(answer_state)


        state_data = data[data.state == answer_state]  # row

        new_state = turtle.Turtle()
        new_state.penup()
        new_state.hideturtle()
        new_state.goto(int(state_data.x.iloc[0]),int(state_data.y.iloc[0]))
        new_state.write(state_data.state.item())
        # new_state.write(answer_state)
    answer_state = screen.textinput(title=f"Guess the State : {len(guessed_states)}/50",
                                        prompt="what's another state's name?").title()

screen.exitonclick()
