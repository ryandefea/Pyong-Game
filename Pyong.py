import turtle

wn = turtle.Screen()
wn.title("Pyong by Ryan DeFea")
wn.bgcolor("black")
wn.setup(width=800, height=800)
wn.tracer(0)

# Score
score_a = 10
score_b = 10
score_c = 10
score_d = 10

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

# Paddle C
paddle_c = turtle.Turtle()
paddle_c.speed(0)
paddle_c.shape("square")
paddle_c.color("white")
paddle_c.shapesize(stretch_wid=1, stretch_len=5)
paddle_c.penup()
paddle_c.goto(0, 350)

# Paddle D
paddle_d = turtle.Turtle()
paddle_d.speed(0)
paddle_d.shape("square")
paddle_d.color("white")
paddle_d.shapesize(stretch_wid=1, stretch_len=5)
paddle_d.penup()
paddle_d.goto(0, -350)

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
pen.write("Player A: 10 Player B: 10 Player C: 10 Player D: 10", align="center", font=("Comic Sans", 24, "normal"))

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

def paddle_c_left():
    x = paddle_c.xcor()
    x -= 20
    paddle_c.setx(x)

def paddle_c_right():
    x = paddle_c.xcor()
    x += 20
    paddle_c.setx(x)    

def paddle_d_left():
    x = paddle_d.xcor()
    x -= 20
    paddle_d.setx(x)

def paddle_d_right():
    x = paddle_d.xcor()
    x += 20
    paddle_d.setx(x)   
    

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "q")
wn.onkeypress(paddle_a_down, "a")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(paddle_c_left, "y")
wn.onkeypress(paddle_c_right, "u")
wn.onkeypress(paddle_d_left, "n")
wn.onkeypress(paddle_d_right, "m")    

#main game loop
while True:
   wn.update()


   # Move ball takes where the ball is starting xcor or ycor and then applies the speed and movement ball.dx or ball.dy
   ball.setx(ball.xcor() + ball.dx)
   ball.sety(ball.ycor() + ball.dy)
   
   # Border checking top border

  #  uncomment for 2 player
  #  if ball.ycor() > 390:
  #       ball.sety(390)
  #       ball.dy *= -1

   # Border checking bottom border
  #  uncomment for 2 player
  #  if ball.ycor() < -390:
  #       ball.sety(-390)
  #       ball.dy *= -1

   # Border checking for bottom boarder
   if ball.ycor() < -390:
        ball.goto(0, 0)
        ball.dy *= -1
        score_d -= 1
        pen.clear()
        pen.write("Player A: {} Player B: {} Player C: {} Player D: {}".format(score_a, score_b, score_c, score_d), align="center", font=("Comic Sans", 24, "normal"))

   # Border checking for top boarder
   if ball.ycor() > 390:
        ball.goto(0, 0)
        ball.dy *= -1
        score_c -= 1
        pen.clear()
        pen.write("Player A: {} Player B: {} Player C: {} Player D: {}".format(score_a, score_b, score_c, score_d), align="center", font=("Comic Sans", 24, "normal"))

   # Border checking right border
   if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b -= 1
        pen.clear()
        pen.write("Player A: {} Player B: {} Player C: {} Player D: {}".format(score_a, score_b, score_c, score_d), align="center", font=("Comic Sans", 24, "normal"))

   # Border checking left border
   if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a -= 1
        pen.clear()
        pen.write("Player A: {} Player B: {} Player C: {} Player D: {}".format(score_a, score_b, score_c, score_d), align="center", font=("Comic Sans", 24, "normal"))


   # Paddle and ball collisions - if ball x coordinate is greater than 340 and less than 350 and the balls y coordinate is less than paddle b's y coordinate + 50 and the ball's y coordinate is greater than paddle b's y coordinate -50. ball.setx moves the ball back to the left a little and ball.dx *1 -1 reverses the ball  
   if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
       ball.setx(335)
       ball.dx *= -1

   if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
       ball.setx(-335)
       ball.dx *= -1
       