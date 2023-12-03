from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0

    def create_scoreboard(self):
        self.hideturtle()
        self.penup()
        self.goto(-270, 190)
        self.write(f"Level : {self.level}", align="left", font=FONT)

    def level_count(self):
        self.clear()
        self.level += 1

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=FONT)
