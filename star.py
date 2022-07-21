from turtle import *
import turtle

turtle.tracer(8, 0)

tur = turtle.Turtle()
tur.speed(6)
tur.getscreen().bgcolor("black")
tur.color("cyan")
tur.penup()
tur.goto((-200, -500))
tur.pendown()

def star(turtle, size):
    if size <= 10:
        return
    else:
        for i in range(8):
            

            turtle.forward(size)
            star(turtle, size/2.5)
  

            turtle.left(45)
 
star(tur, 240)
turtle.done()