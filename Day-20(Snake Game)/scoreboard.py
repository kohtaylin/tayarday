from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 12, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.new_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.write(arg=f"Score: {self.new_score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)
