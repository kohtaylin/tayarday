import turtle
import pandas


screen = turtle.Screen()
screen.title("Name The States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score = 0
states_data = pandas.read_csv("50_states.csv")
state_list = states_data["state"].to_list()
correct_list = []

while score < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What is another state's name? ").title()

    if answer_state in state_list:
        if answer_state not in correct_list:
            correct_list.append(answer_state)
            correct_guess = states_data[states_data["state"] == answer_state]
            writer = turtle.Turtle()
            writer.hideturtle()
            x = int(correct_guess["x"])
            y = int(correct_guess["y"])
            writer.penup()
            writer.goto(x, y)
            writer.write(arg=answer_state)
            score += 1






screen.exitonclick()
