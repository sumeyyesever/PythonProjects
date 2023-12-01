from turtle import Turtle


class ScoreBoard:
    def __init__(self):
        self.score = 0
        self.board = Turtle()
        self.create_board()

    def create_board(self):
        self.board.penup()
        self.board.hideturtle()
        self.board.color("white")
        self.board.setposition(0, 280)
        self.update_board()

    def update_board(self):
        self.board.write(f"Score: {self.score}", False, "center", ("Courier", 12, "normal"))

    def game_over(self):
        self.board.goto(0, 0)
        self.board.write("GAME OVER", False, "center", ("Courier", 20, "normal"))

    def update_score(self):
        self.score += 1
        self.board.clear()
        self.create_board()
