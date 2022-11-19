from turtle import Turtle

ALIGNMENT = "left"
FONT = ('Arial', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.new_score = 0
        with open("data.txt", "r") as data:
            self.highest_score = int(data.read())
        self.update_score()

    def update_score(self):
        self.clear()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.goto(-250, 260)
        self.write(arg=f"Current Score: {self.new_score}  Highest Score: {self.highest_score}", move=False,
                   align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.high_score()
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def high_score(self):
        if self.new_score > self.highest_score:
            with open("data.txt", "w") as data:
                data.write(f"{self.new_score}")
