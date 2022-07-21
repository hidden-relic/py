import turtle as turt

t = turt.Turtle()
turt.tracer(8, 0)

t.hideturtle()
t.speed('fastest')
t.right(-90)
angle = 45

def yaxis(size, lvl):   
    if lvl > 0:
        turt.colormode(255)
        t.pencolor(0, 255//lvl, 0)
        t.forward(size)
        t.right(angle)
        yaxis(0. * size, lvl-1)
        t.pencolor(0, 255//lvl, 0)
        t.lt( 2 * angle )
        yaxis(0.9 * size, lvl-1)
        t.pencolor(0, 255//lvl, 0)
        t.right(angle)
        t.forward(-size)
           
yaxis(80, int(turt.numinput('steps?', 'steps?')))
t.done()
