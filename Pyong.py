import turtle

wn = turtle.Screen()
wn.title("Pyong by Ryan DeFea")
wn.bgcolor("black")
wn.setup(width=800, height=800)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .05
ball.dy = .05

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 340)
pen.write("Player A: 0 Player B: 0", align="center", font=("Comic Sans", 24, "normal"))

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)    
    

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "q")
wn.onkeypress(paddle_a_down, "a")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")    

#main game loop
while True:
   wn.update()


   # Move ball takes where the ball is starting xcor or ycor and then applies the speed and movement ball.dx or ball.dy
   ball.setx(ball.xcor() + ball.dx)
   ball.sety(ball.ycor() + ball.dy)
   
   # Border checking top border
   if ball.ycor() > 390:
        ball.sety(390)
        ball.dy *= -1

   # Border checking bottom border
   if ball.ycor() < -390:
        ball.sety(-390)
        ball.dy *= -1

   # Border checking right border
   if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Comic Sans", 24, "normal"))

   # Border checking left border
   if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Comic Sans", 24, "normal"))


   # Paddle and ball collisions - if ball x coordinate is greater than 340 and less than 350 and the balls y coordinate is less than paddle b's y coordinate + 50 and the ball's y coordinate is greater than paddle b's y coordinate -50. ball.setx moves the ball back to the left a little and ball.dx *1 -1 reverses the ball  
   if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
       ball.setx(335)
       ball.dx *= -1

   if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
       ball.setx(-335)
       ball.dx *= -1
       