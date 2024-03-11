import turtle
import random

# screen
win = turtle.Screen()
win.title("PONG in PYTHON")
win.bgcolor("orange")
win.setup(width=800, height=600)
win.tracer(0)

# MAIN GAME LOGIC

# score
p1 = 0
p2 = 0

# pong1
pong1 = turtle.Turtle()
pong1.speed(0)
pong1.color("black")
pong1.shape("square")
pong1.shapesize(stretch_wid=6, stretch_len=1)
pong1.penup()
pong1.goto(-350, 0)

# pong2
pong2 = turtle.Turtle()
pong2.speed(0)
pong2.color("black")
pong2.shape("square")
pong2.shapesize(stretch_wid=6, stretch_len=1)
pong2.penup()
pong2.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.color("black")
ball.shape("square")
ball.penup()
ball.goto(0, 0)
ball.xd = random.choice([-0.2, 0.2])  # Random initial x direction
ball.yd = random.choice([-0.2, 0.2])  # Random initial y direction

# Ball speed and speed increase factor
ball_speed = 0.2
speed_increase_factor = 1.1

# pen?
pen = turtle.Turtle()
pen.speed(0)
pen.color("White")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("P1 : 0  P2: 0", align="center", font=("courier", 23, "bold"))


# Paddle movement functions
def move_paddle_up(paddle):
    y = paddle.ycor()
    y += 20
    paddle.sety(y)


def move_paddle_down(paddle):
    y = paddle.ycor()
    y -= 20
    paddle.sety(y)


# Keyboard bindings
turtle.listen()
turtle.onkeypress(lambda: move_paddle_up(pong1), "w")
turtle.onkeypress(lambda: move_paddle_down(pong1), "s")
turtle.onkeypress(lambda: move_paddle_up(pong2), "Up")
turtle.onkeypress(lambda: move_paddle_down(pong2), "Down")

# MAIN GAME LOOP
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.xd)
    ball.sety(ball.ycor() + ball.yd)

    # Border checking
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.yd *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.xd *= -1
        p1 += 1
        ball_speed *= speed_increase_factor  # Increase ball speed
        pen.clear()
        pen.write(f"P1 : {p1}  P2: {p2}", align="center", font=("courier", 23, "bold"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.xd *= -1
        p2 += 1
        ball_speed *= speed_increase_factor  # Increase ball speed
        pen.clear()
        pen.write(f"P1 : {p1}  P2: {p2}", align="center", font=("courier", 23, "bold"))

    # Check for game end and restart
    if p1 == 10 or p2 == 10:
        winner = "Player 1" if p1 == 10 else "Player 2"
        pen.clear()
        pen.write(
            f"Game Over\n{winner} wins!", align="center", font=("courier", 30, "bold")
        )
        turtle.update()
        turtle.done()
        break

    # Collisions
    if (
        pong2.xcor() - 20 < ball.xcor() < pong2.xcor() + 20
        and pong2.ycor() + 50 > ball.ycor() > pong2.ycor() - 50
    ):
        ball.setx(pong2.xcor() - 20)
        ball.xd *= -1

    if (
        pong1.xcor() - 20 < ball.xcor() < pong1.xcor() + 20
        and pong1.ycor() + 50 > ball.ycor() > pong1.ycor() - 50
    ):
        ball.setx(pong1.xcor() + 20)
        ball.xd *= -1

    # Set the new speed
    ball.setx(ball.xcor() + ball_speed * ball.xd)
    ball.sety(ball.ycor() + ball_speed * ball.yd)
