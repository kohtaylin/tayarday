from turtle import Turtle


class Line(Turtle):

    def __init__(self):
        super().__init__()
        self.create_line()

    def create_line(self):
        self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.setheading(90)
        self.penup()
        self.forward(280)
        self.pensize(5)
        while self.ycor() > -280:
            self.pendown()
            self.back(10)
            self.penup()
            self.back(10)
