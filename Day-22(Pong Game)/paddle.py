from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.speed("fastest")
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.goto(position)
        self.setheading(90)

    def up(self):
        if self.ycor() < 270:
            self.forward(20)

    def down(self):
        if self.ycor() > -270:
            self.backward(20)
