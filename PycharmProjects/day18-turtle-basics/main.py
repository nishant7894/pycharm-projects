import turtle
from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape('turtle')
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


"""============================================================================================================="""
'''The closed figure drawing in turtle graphics'''
# tim.penup()
# tim.left(90)
# tim.forward(50)
# tim.left(90)
# tim.forward(50)
# tim.left(180)
# tim.pendown()
#
#
#
# num_sides = 3
# while num_sides < 14:
#     for _ in range(num_sides):
#         tim.color(random_color())
#         angle = 360/ num_sides
#         tim.forward(100)
#         tim.right(angle)
#     num_sides +=1
'''========================================================================================================'''

"""Program to print random walk"""
# direction = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
# for _ in range(200):
#     tim.forward(30)
#     tim.color(random_color())
#     tim.setheading(random.choice(direction))
"""==================================================================================================="""
"""Program to print a Spirograph"""
# tim.speed("fastest")
# def spirograph(gap):
#     for _ in range(int(360/gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + gap)
#
# spirograph(5)
#


"""==================================================================================================="""

screen = Screen()
screen.exitonclick()
