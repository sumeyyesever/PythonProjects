import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(paddle_l.move_up, "w")
screen.onkey(paddle_l.move_down, "s")
screen.onkey(paddle_r.move_up, "Up")
screen.onkey(paddle_r.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    scoreboard.create_scoreboard()
    ball.move()

    # collision with the walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # collision with the paddle
    if ball.xcor() > 330 and ball.distance(paddle_r) < 50 or ball.xcor() < - 330 and ball.distance(paddle_l) < 50:
        ball.bounce_x()

    # ball goes out of the edge
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.update_score_left()

    if ball.xcor() < - 380:
        ball.reset_position()
        scoreboard.update_score_right()


screen.exitonclick()
