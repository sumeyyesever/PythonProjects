from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.ball_xcor = 10
        self.ball_ycor = 10
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.ball_xcor
        new_y = self.ycor() + self.ball_ycor
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.ball_ycor *= -1

    def bounce_x(self):
        self.ball_xcor *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        self.home()
        self.bounce_x()
        self.ball_speed = 0.1
