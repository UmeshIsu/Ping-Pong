import  turtle
import time
game_on = True
wn = turtle.Screen()
wn.title("Ping Pong By Umesh")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

#score
score_a = 0
score_b = 0

# Paddle A
paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape("square")
paddle_A.shapesize(stretch_wid=5, stretch_len=1)
paddle_A.color("white")
paddle_A.penup()
paddle_A.goto(-350,0)

# Paddle B
paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.shapesize(stretch_wid=5, stretch_len=1)
paddle_B.color("white")
paddle_B.penup()
paddle_B.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = 2

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0 ",align="center",font=("courier",24,"normal"))

# Paddle A moves 
def paddle_A_up():
    y = paddle_A.ycor()
    y += 20
    paddle_A.sety(y)
def paddle_A_down():
    y = paddle_A.ycor()
    y -= 20
    paddle_A.sety(y)

# Paddle B moves 
def paddle_B_up():
    y = paddle_B.ycor()
    y += 20
    paddle_B.sety(y)
def paddle_B_down():
    y = paddle_B.ycor()
    y -= 20
    paddle_B.sety(y)


# Keybord moves
wn.listen()
wn.onkeypress(paddle_A_up,"w")
wn.onkeypress(paddle_A_down,"s")

wn.onkeypress(paddle_B_up,"Up")
wn.onkeypress(paddle_B_down,"Down")

# Main game loop
while game_on:
    time.sleep(0.01) 
    wn.update()
    # Ball k=movemet
    ball.setx(ball.xcor() + ball.dx )
    ball.sety(ball.ycor() + ball.dy)

    # Border 
    if ball.ycor() > 290: 
        ball.sety(290)
        ball.dy *= -1
     
    if ball.ycor() < -290: 
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *=-1
        score_a+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {} ".format(score_a,score_b),align="center",font=("courier",24,"normal"))
            
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *=-1
        score_b +=1
        pen.clear()
        pen.write("Player A: {}  Player B: {} ".format(score_a,score_b),align="center",font=("courier",24,"normal"))

    # paddle and ball combination
    if (ball.xcor() > 340 and ball.xcor() < 350) and (paddle_B.ycor() +40 and ball.ycor() > paddle_B.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (paddle_A.ycor() -40 and ball.ycor() < paddle_A.ycor() +40):
        ball.setx(-340)
        ball.dx *= -1
