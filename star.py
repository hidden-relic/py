from turtle import *
# import tkcap
from time import sleep

tracer(500, 0)

tur = Turtle()
# cap=tkcap.CAP(root)
tur.getscreen().bgcolor("black")
# tur.penup()
tur.goto((-200, 500))
# tur.pendown()

def star(turtle, size):
    turtle.pendown()
    t=1
    if size <= 2:
        return
    else:
        for i in range(3):
            # sleep(t)
            # t*=0.9
            turtle.forward(size)
            turtle.penup()
            star(turtle, ((size/3)*2))
  

            turtle.left(36)
t = 0.5
for i in range(0, 1000, 10):
    tur.speed(0)
    t*=1.1
    tur.color("cyan")
    tur.penup()
    tur.sety(tur.ycor()-200)
    star(tur, i)
    # sleep(1)
    # cap.capture('C:\giz\SS.jpg')
    tur.reset()
tur.done()