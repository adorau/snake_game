from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.turtlesize(0.5, 0.5, 0)
        self.shape("circle")
        self.color("#00ff44")
        self.speed(10)
        self.go_to_the()

    def go_to_the(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
