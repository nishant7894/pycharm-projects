"""from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color('coral')
timmy.forward(200)
timmy.tilt(60)
timmy.back(200)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()"""
from prettytable import prettytable

table = prettytable.PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = 'c'
print(table)
