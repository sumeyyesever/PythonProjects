import turtle as turtle_module
import random

turtle_module.colormode(255)
turtle = turtle_module.Turtle()
color_palette = [(219, 153, 108), (132, 172, 195), (221, 72, 88), (213, 132, 150), (26, 119, 151),
                 (240, 208, 99), (122, 176, 148), (39, 119, 84), (20, 164, 203), (140, 86, 63), (219, 85, 78),
                 (134, 81, 99), (174, 185, 216), (236, 161, 173), (25, 167, 123), (162, 209, 168)]

print(turtle.pos())
turtle.hideturtle()
turtle.penup()
x = -200
y = -200
turtle.setpos(x, y)

for _ in range(10):
    turtle.penup()
    turtle.setpos(x, y)
    for _ in range(10):
        turtle.dot(20, random.choice(color_palette))
        turtle.penup()
        turtle.forward(50)
    y = y + 50


screen = turtle_module.Screen()
screen.exitonclick()
