from turtle import Screen
from the_turtle import TheTurtle
from cars import Car
from scoreboard import Score


screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.tracer(0)

my_turtle = TheTurtle()
the_cars = Car()
player_score = Score()

screen.listen()
screen.onkey(fun=my_turtle.move, key="Up")

game_on = True

while game_on:
    screen.update()
    the_cars.driving()
    if my_turtle.ycor() > 290:
        player_score.score += 1
        player_score.update()
        my_turtle.reposition()

    # car hit turtle
    for car in the_cars.cars:
        if abs(car.ycor() - my_turtle.ycor()) < 10 and abs(car.xcor() - my_turtle.xcor()) < 30:
            player_score.update()
            player_score.game_over()
            game_on = False

screen.exitonclick()
