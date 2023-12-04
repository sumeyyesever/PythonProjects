from turtle import Turtle
with open("data.txt") as file:
    high_score = int(file.read())


class ScoreBoard:
    def __init__(self):
        self.score = 0
        self.high_score = high_score
        self.board = Turtle()
        self.create_board()

    def create_board(self):
        self.board.penup()
        self.board.hideturtle()
        self.board.color("white")
        self.board.setposition(0, 280)
        self.update_board()

    def update_board(self):
        self.board.write(f"Score: {self.score} High score: {self.high_score}", False, "center", ("Courier", 12, "normal"))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.board.clear()
        self.update_board()

    def update_score(self):
        self.score += 1
        self.board.clear()
        self.create_board()
