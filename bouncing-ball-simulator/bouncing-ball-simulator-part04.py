# Bouncing Ball Simulator
# By Sander Ruscigno
# Part 4: Randomizing

import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Bouncing Ball Simulator")
#wn.tracer(0.5)
wn.delay(0)

balls = []
color = ["red","blue","yellow","orange","green","white","purple"]
shapes = ["circle","triangle","square"]

for _ in range(25):
  balls.append(turtle.Turtle())


for ball in balls:
  ball.shape(random.choice(shapes))
  ball.color(random.choice(color))
  ball.penup()
  ball.speed(0)
  x = random.randint(-290, 290)
  y = random.randint(200, 400)
  ball.goto(x, y)
  ball.dy = 0
  ball.dx = random.randint(-3, 3)
  ball.da = random.randint(-5, 5)

gravity = 0.10

while True:
  #wn.update()
  for ball in balls:
    ball.rt(ball.da)
    ball.dy -= gravity
    ball.sety(ball.ycor() + ball.dy)

    ball.setx(ball.xcor() + ball.dx)

    # Check for a wall colision
    if ball.xcor() > 300:
      ball.dx *= -1
      ball.da *= -1

    if ball.xcor() < -300:
      ball.dx *= -1
      ball.da *= -1

    #check for a bounce
    if ball.ycor() < -300:
      ball.sety(-300)
      ball.dy *= -1
      ball.da *= -1

wn.mainloop()