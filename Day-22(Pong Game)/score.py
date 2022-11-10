from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 18, 'bold')


class ScoreBoard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.score = 0
        self.update()

    def update(self):
        self.clear()
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.goto(self.position)
        self.write(arg=self.score, move=False, align=ALIGNMENT, font=FONT)

