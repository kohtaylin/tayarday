from turtle import Screen
from middle_line import Line
from paddle import Paddle
from ball import Ball
from score import ScoreBoard


screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

middle_line = Line()
left_paddle = Paddle((-470, 0))
right_paddle = Paddle((470, 0))
ball = Ball()
left_score = ScoreBoard((-30, 270))
right_score = ScoreBoard((30, 270))

screen.listen()
screen.onkey(fun=left_paddle.up, key="q")
screen.onkey(fun=left_paddle.down, key="a")
screen.onkey(fun=right_paddle.up, key="Up")
screen.onkey(fun=right_paddle.down, key="Down")

game_on = True
left_paddle_hit_ball = False
right_paddle_hit_ball = False

while game_on:
    screen.update()
    ball.move()
    # bounce against wall
    if ball.ycor() > 290:
        ball.step_y *= -1

    elif ball.ycor() < -290:
        ball.step_y *= -1

    # bounce against paddle
    if ball.xcor() > -470 and left_paddle.distance(ball) < 30:
        if ball.step_x < 0:
            ball.step_x *= -1
            ball.speed_up()
        left_paddle_hit_ball = True

    if left_paddle_hit_ball and ball.xcor() > 0:
        left_score.score += 1
        left_score.update()
        left_paddle_hit_ball = False

    if ball.xcor() < 470 and right_paddle.distance(ball) < 30:
        if ball.step_x > 0:
            ball.step_x *= -1
        right_paddle_hit_ball = True

    if right_paddle_hit_ball and ball.xcor() < 0:
        right_score.score += 1
        right_score.update()
        right_paddle_hit_ball = False

    # game over if ball passed paddle
    if ball.xcor() - left_paddle.xcor() < -25 or ball.xcor() - right_paddle.xcor() > 25:
        game_on = False
        if left_score.score == right_score.score:
            result = "Draw"
        elif left_score.score > right_score.score:
            result = "LEFT PLAYER WON."
        else:
            result = "RIGHT PLAYER WON."

        middle_line.wirte_result(result)
        if result != "Draw":
            if result == "LEFT PLAYER WON.":
                crown_position = -250
            else:
                crown_position = 250
            middle_line.crown(crown_position)

screen.exitonclick()
