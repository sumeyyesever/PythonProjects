from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score_left = 0
        self.score_right = 0

    def create_scoreboard(self):
        self.goto(-100, 200)
        self.write(f"{self.score_left}", align="center", font=("Courier", 70, "normal"))
        self.goto(100, 200)
        self.write(arg=f"{self.score_right}", align="center", font=("Courier", 70, "normal"))

    def update_score_left(self):
        self.clear()
        self.score_left += 1

    def update_score_right(self):
        self.clear()
        self.score_right += 1
