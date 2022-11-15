from turtle import Turtle


SPEED = 20


class TheTurtle(Turtle):

    def __init__(self):
        super().__init__()
        self.create()

    def create(self):
        self.shape("turtle")
        self.penup()
        self.color("orange")
        self.setheading(90)
        self.reposition()

    def move(self):
        self.forward(SPEED)

    def reposition(self):
        self.goto(0, -280)
