from turtle import Turtle
import random


COLORS = ["red", "blue", "black", "purple", "pink", "brown", "green"]
NUMBER_OF_CARS = 20


class Car:

    def __init__(self):
        self.cars = []
        self.create()
        self.car_speed = 0.7

    def create(self):
        for i in range(NUMBER_OF_CARS):
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_x = random.randint(500, 2000)
            new_y = random.choice([i for i in range(-250, 250)])
            new_car.goto(new_x, new_y)
            new_car.setheading(180)
            self.cars.append(new_car)

    def driving(self):
        for car in self.cars:
            if car.xcor() > -560:
                car.forward(self.car_speed)
            else:
                new_x = random.randint(500, 2000)
                new_y = random.choice([i for i in range(-250, 250)])
                car.hideturtle()
                car.goto(new_x, new_y)
                car.showturtle()
