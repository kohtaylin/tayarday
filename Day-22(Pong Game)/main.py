from turtle import Screen
from middle_line import Line
from paddle import Paddle
import time


screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

middle_line = Line()
left_paddle = Paddle((-470, 0))
right_paddle = Paddle((470, 0))

screen.listen()
screen.onkey(fun=left_paddle.up, key="q")
screen.onkey(fun=left_paddle.down, key="z")
screen.onkey(fun=right_paddle.up, key="Up")
screen.onkey(fun=right_paddle.down, key="Down")

game_on = True

while game_on:
    screen.update()






screen.exitonclick()