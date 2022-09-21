import turtle

wn = turtle.Screen()
wn.title("Pyong by Ryan DeFea")
wn.bgcolor("black")
wn.setup(width=800, height=800)
wn.tracer(0)

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

   # Border checking left border
   if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1