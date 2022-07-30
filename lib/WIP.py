import turtle

class log:

    def __init__(self, data=''):
        self.log=open('C:\\giz\\lib\\log.txt', 'w')
        self.log.write('')
        self.log.close()
        self.log=open('C:\\giz\\lib\\log.txt', 'a')
        self.log.write(data)
        self.log.write('\n') if data != '' else self.log.write('')
    
    def __call__(self, data):
        self.log.write('\n'+data)

class hatch(log):

    t=turtle.Turtle()
    
    def __init__(self, name, x=0, y=0, color='black'):
        self.name=name
        log.__init__(self, self.name+' hatched @ x'+str(x)+', y'+str(y))
        self.t.color=color
        self.t.width=1
        self.s=self.t.getscreen()
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()

    def e(self):
        self.t.setheading(0)
    def w(self):
        self.t.setheading(180)
    def n(self):
        self.t.setheading(90)
    def s(self):
        self.t.setheading(270)

    def f(self, n):
        self.t.forward(n)
    def b(self, n):
        self.t.backward(n)
        
    def l(self, d):
        self.t.left(d)
    def r(self, d):
        self.t.right(d)
        
    def g(self, x, y):
        self.log('Goto: '+str(x)+', '+str(y)+'\n')
        self.u()
        self.t.goto(x, y)
        self.d()

    def u(self):
        self.t.penup()
    def d(self):
        self.t.pendown()

    def xa(self, n):
        self.g(n, self.t.ycor())
    def ya(self, n):
        self.g(self.t.xcor(), n)
    def xr(self, n):
        self.g(self.t.xcor()+n, self.t.ycor())
    def yr(self, n):
        self.g(self.t.xcor(), self.t.ycor()+n)
        
    def wr(self, arg, align='center', font='Verdana', fontsize=6):
        self.t.write(arg, align=align, font=(font, fontsize))
        

t = hatch(name='first', x=50, y=50, color='blue')
t.s.mode('world')
for i in range(0, 4):
    t.r(90)
    t.f(50)
t.s.update()

t.log.close()
turtle.mainloop()
