from turtle import *
import random


def draw_rect(h):
    for _ in range(2):
        forward(20)
        left(90)
        forward(h)
        left(90)


def draw_infation():
    penup()
    goto(-300, -50)
    height = random.randint(10, 30)
    pendown()
    for _ in range(25):
        draw_rect(height)
        height += random.randint(0, 20)
        penup()
        forward(25)
        pendown()


speed("fastest")
draw_infation()

exitonclick()
