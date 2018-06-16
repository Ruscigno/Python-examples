# Bouncing Ball Simulator
# By Sander Ruscigno
# Part 1: Getting Startted

import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Bouncing Ball Simulator")

ball = turtle.Turtle()
ball.shape("circle")
ball.color("green")
ball.penup()
ball.speed(0)
ball.goto(0, 200)
ball.dy = -2

gravity = 0.1

while True:
  ball.dy -= gravity
  ball.sety(ball.ycor() + ball.dy)

  #check for a bounce
  if ball.ycor() < - 300:
    ball.dy *= -1

wn.mainloop()