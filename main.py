from pong import Pong
from turtle import Screen
import time
from ball import Ball
from score import Score
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("PongGame")
screen.tracer(0)
r_paddle = Pong((350, 0))
l_paddle = Pong((-350, 0))
ball = Ball()
score_r = Score((170, 250))
score_l = Score((-170, 250))
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "q")
screen.onkey(l_paddle.down, "a")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()
    if ball.distance(r_paddle) <= 50 and ball.xcor() > 320:
        ball.bounce_paddle()
    if ball.distance(l_paddle) <= 50 and ball.xcor() < -320:
        ball.bounce_paddle()

    # detect when paddle misses
    if ball.xcor() > 390:
        ball.reset_position()
        score_l.increase_score()
    if ball.xcor() < -390:
        ball.reset_position()
        score_r.increase_score()
screen.exitonclick()
