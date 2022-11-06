from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
score = Scoreboard()
food = Food()
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Colliding the snake head with food
    snake_head_x = snake.head.xcor()
    snake_head_y = snake.head.ycor()
    if food.distance(snake_head_x, snake_head_y) <= 15:
        food.refresh()
        snake.extend_snake()
        score.new_score += 1
        score.update_score()

    # Colliding the snake head with the wall
    if snake_head_x < -290 or snake_head_x > 290 or snake_head_y < -290 or snake_head_y > 290:
        game_on = False
        score.game_over()

    # Colliding the snake head with its tail
    if snake.bite_itself():
        game_on = False
        score.game_over()

screen.exitonclick()
