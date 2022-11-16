from turtle import Turtle


ALIGNMENT = "center"
FONT = ('Arial', 28, 'bold')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.update()

    def update(self):
        self.penup()
        self.clear()
        self.goto(0, 260)
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
