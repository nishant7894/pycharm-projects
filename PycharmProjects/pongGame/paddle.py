from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coordinate):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(coordinate)
        self.speed("fastest")

    def go_up(self):
        self.speed("fastest")
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def go_down(self):
        self.speed("fastest")
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)
