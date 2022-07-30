
root=tkinter.Tk()
# tracer(8, 0)

tur = Turtle()
cap=tkcap.CAP(root)
tur.getscreen().bgcolor("black")
# tur.penup()
# tur.goto((-200, -500))
# tur.pendown()

def star(turtle, size):
    if size <= 10:
        return
    else:
        turtle.write(turtle.pos())
        for i in range(8):
            
            sleep(1)
            turtle.forward(size)
            star(turtle, size/3)
  

            turtle.left(45)
for i in range(0, 1000, 100):
    print(i)
    tur.speed(0)
    tur.color("cyan")
    tur.penup()
    tur.sety(tur.ycor()-200)
    tur.pendown()
    star(tur, i)
    # sleep(1)
    cap.capture('C:\giz\SS.jpg')
    tur.reset()
tur.done()