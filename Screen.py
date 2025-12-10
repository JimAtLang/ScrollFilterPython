from turtle import *
import turtle

class Screen:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.turtle = turtle.Turtle()
        self.turtle.speed(10)
        self.screen = turtle.Screen()
        self.screen.setworldcoordinates(0, width, height, 0)

    def render(self, sprite, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.setheading(90)
        for i in range(2):
            turtle.begin_fill()
            turtle.forward(sprite.width)
            turtle.right(90)
            turtle.forward(sprite.height)
            turtle.right(90)
            turtle.end_fill()
