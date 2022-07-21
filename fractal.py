from turtle import *
import turtle as t
import time

t.tracer(56, 0)

length=1
a_or_b='b'
dept=5
turtle1 = t.Turtle()
turtle2 = t.Turtle()
log = t.Turtle()
log.hideturtle()
i=0
turtle1.hideturtle()
turtle2.hideturtle()
turtle1.speed(0)
turtle2.speed(0)

def fractdraw(stp, rule, ang, dept, t):
  global i
  i += 1
  if dept > 0:
      x = lambda: fractdraw(stp, "a", ang, dept - 1, t)
      y = lambda: fractdraw(stp, "b", ang, dept - 1, t)
      left = lambda: t.left(ang)
      right = lambda: t.right(ang)
      forward = lambda: t.forward(stp)
      if rule == "a":
        left(); y(); forward(); right(); x(); forward(); x(); right(); forward(); y(); left();
      if rule == "b":
        right(); x(); forward(); left(); y(); forward(); y(); left(); forward(); x(); right();
        

# for dept in range(1, 10):
  # log.write(str(dept))
for angle in range(0, 180, 10):
  fractdraw(length, 'a', angle, dept, turtle1)
  fractdraw(length, 'b', angle, dept, turtle2)
    # log.write(str(dept)+'\t'+str(angle))
    # time.sleep(0.05)
    # log.reset()
  turtle1.reset()
  turtle2.reset()
  # log.reset()
 
t.mainloop()