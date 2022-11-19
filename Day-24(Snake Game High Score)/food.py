from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.refresh()

    def refresh(self):
        self.clear()
        self.shape("circle")
        self.penup()
        self.turtlesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.goto(random.randint(-270, 270), random.randint(-270, 270))
