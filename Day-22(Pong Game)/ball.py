from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.x = 0
        self.y = 0
        step = [0.3, -0.3]
        self.step_x = random.choice(step)
        self.step_y = random.choice(step)

    def move(self):
        self.speed("slowest")
        self.x += self.step_x
        self.y += self.step_y
        self.goto(self.x, self.y)

    def speed_up(self):
        self.step_x *= 1.2
        self.step_y *= 1.2
