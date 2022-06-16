import turtle

ourWindow = turtle.Screen()#we make the window of our game
ourWindow.title("Ping Pong Game")#we put a title
ourWindow.bgcolor("#26BBDA")#we set the background color of the window
ourWindow.setup(width=800, height=600)#we decide how big we want the window to be
ourWindow.tracer() #it stops our window from updating so our game goes much faster


player1 = turtle.Turtle()
player1.speed(0)#so that we can move it with the maximum possible speed
player1.shape("square")
player1.color("white")
player1.shapesize(stretch_wid=5, stretch_len=1)
player1.penup()#like this we won't have a line after the paddle when we move it
player1.goto(-350, 0)

player2 = turtle.Turtle()
player2.speed(0)#so that we can move it with the maximum possible speed
player2.shape("square")
player2.color("white")
player2.shapesize(stretch_wid=5, stretch_len=1)
player2.penup()#like this we won't have a line after the paddle when we move it
player2.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 4
ball.dy = 4

score_1 = 0
score_2 = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Player 1: 0  Player 2: 0", align = "center", font = ("Sans-Serif", 15, "normal"))

def move_player1_up():
    y = player1.ycor()#it returns the y coordinates for us
    y = y+20
    player1.sety(y)

def move_player1_down():
    y = player1.ycor()#it returns the y coordinates for us
    y = y-20
    player1.sety(y)

def move_player2_up():
    y = player2.ycor()#it returns the y coordinates for us
    y = y+20
    player2.sety(y)

def move_player2_down():
    y = player2.ycor()#it returns the y coordinates for us
    y = y-20
    player2.sety(y)

ourWindow.listen()
ourWindow.onkeypress(move_player1_up, "w")
ourWindow.onkeypress(move_player1_down, "s")
ourWindow.onkeypress(move_player2_up, "Up")
ourWindow.onkeypress(move_player2_down, "Down")



while True:
    ourWindow.update()#it updates the screen everytime we get into the while True cycle

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 285:
        ball.sety(285)
        ball.dy *= -1
    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write(f"Player 1: {score_1}  Player 2: {score_2}", align = "center", font = ("Sans-Serif", 15, "normal"))
    if ball.ycor() < -285:
        ball.sety(-285)
        ball.dy *= -1
    if ball.xcor() < -380:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write(f"Player 1: {score_1}  Player 2: {score_2}", align = "center", font = ("Sans-Serif", 15, "normal"))
    if (ball.xcor() > 330 and ball.xcor() < 350) and (ball.ycor() < player2.ycor() + 50 and ball.ycor() > player2.ycor() - 50):
        ball.dx *= -1
        ball.setx(330)
    if (ball.xcor() < -330 and ball.xcor() >-350) and (ball.ycor() < player1.ycor() + 50 and ball.ycor() > player1.ycor() - 50):
        ball.dx *= -1
        ball.setx(-330)
    

