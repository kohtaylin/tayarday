from turtle import Turtle
import random


COLORS = ["red", "blue", "black", "purple", "pink", "brown", "green"]
YPOSITION = [y for y in range(-260, 260, 60)]


class Car:

    def __init__(self):
        self.cars = []
        self.create()
        self.speed = 0.6

    def create(self):
        for i in YPOSITION:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=3)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(random.randint(500, 1000), i)
            new_car.setheading(180)
            self.cars.append(new_car)
        random.shuffle(self.cars)

    def driving(self):
        for car in self.cars:
            if car.xcor() > -560:
                car.forward(self.speed)
            else:
                self.speed += 0.01
                new_x = random.randint(500, 1000)
                new_y = random.choice([i for i in range(-260, 260)])
                car.hideturtle()
                car.goto(new_x, new_y)
                car.showturtle()
