#pylint:disable=E1101
#pylint:disable=W0602
#pylint:disable=C0116
#pylint:disable=C0103
#pylint:disable=E0001
import turtle as t
import math
import fractions

def toDegrees(pitch):
	return math.degrees(math.atan(pitch/12))

def revDegrees(degree):
	return 90 - degree
	
def getLeg(a, b):
	return math.sqrt((a **2)+(b**2))
	
def bounds(vert=0, horz=0):
	top = ['top', 't']
	bot = ['bottom', 'b']
	left = ['left', 'l']
	right = ['right', 'r']
	if vert in top:
		vert = 700
	elif vert in bot:
		vert = -700
	if horz in left:
		horz = -350
	elif horz in right:
		horz = 350
	if vert != 0 and horz == 0:
		return vert
	if vert != 0 and horz != 0:
		return (horz, vert)
	if vert == 0 and horz != 0:
		return horz
	return (horz, vert)
  
class builder:
  """builder drawer class"""
  def __init__(self, pitch=0, run=600):
    if pitch != 0:
    	self.pitch = pitch
    else:
    	self.pitch = t.numinput("Pitch", "Roof Pitch", 9)
    self.width = t.numinput("Building Width", "Building Width FEET", 8)*12
    self.width += t.numinput("Building Width", "Building Width INCHES", 0)
    self.rafter_width = t.numinput("Rafter Width", "Rafter Width (5.5, 7.5, 9.5...)", 7.5
    )
    self.run = run
    self.run_steps = (self.run/2)/12
    self.rise = self.run_steps * self.pitch
    self.leg = getLeg(self.run/2, self.rise)
    self.rafters = {'peak': {'x': 0, 'y': 0}, 'wall': {'x': 0, 'y': 0}}
    self.turtle = t.Turtle()
    self.turtle.speed(0)
    self.screen = t.Screen()  
    self.scale = {'x': 600, 'y': 700}
    self.scale_to = self.run/self.width
    self.heel_cut = self.toPixel(3.5)
    self.heel_step = 0
    self.heel_plum = self.toPixel(self.pitch/self.heel_cut)

    
  def f(self, n):
  	self.turtle.forward(n)
  def b(self, n):
  	self.turtle.backward(n)
  def l(self, d):
  	self.turtle.left(d)
  def r(self, d):
  	self.turtle.right(d)
  def u(self):
  	self.turtle.penup()
  def d(self):
  	self.turtle.pendown()
  def w(self, arg, align='center', font='Verdana', fontsize=6):
  	self.turtle.write(arg, align=align, font=(font, fontsize))
  	
  def done(self, x, y):
  	self.screen.reset()
  	del self
  	main()
  	
  def toPixel(self, i):
  	return i * self.scale_to
  	
  def convert(self, i):
  		return math.floor(i/12), round(i % 12)
  	
  def rafter(self):
  	self.turtle.color('brown')
  	self.turtle.hideturtle()
  	self.u()
  	self.turtle.goto(self.turtle.xcor()+self.run/2, bounds('t') - self.toPixel(self.rafter_width))
  	self.d()
  	self.l(90)
  	self.f(self.toPixel(self.rafter_width))
  	self.rafters['peak']['x'] = self.turtle.xcor()
  	self.rafters['peak']['y'] = self.turtle.ycor()
  	self.l(90 + toDegrees(self.pitch))
  	self.f(self.leg*2)
  	self.rafters['wall']['x'] = self.turtle.xcor()
  	self.rafters['wall']['y'] = self.turtle.ycor()
  	self.l(revDegrees(toDegrees(self.pitch)))
  	self.f(self.toPixel(self.rafter_width))
  	self.l(180 - revDegrees(toDegrees(self.pitch)))
  	self.f(self.toPixel(getLeg(self.pitch, 12)))
  	self.l(revDegrees(toDegrees(self.pitch)))
  	
  	if self.toPixel(3.5) > self.toPixel(self.rafter_width)/3:
  		self.heel_cut = self.rafter_width/3
  	self.heel_step = self.heel_cut/12
  	self.heel_plum = self.pitch*self.heel_step
  	self.f(self.toPixel(self.heel_plum))
  	self.heel_corner = self.turtle.pos()
  	self.r(90)
  	self.f(self.toPixel(self.heel_cut))
  	self.l(toDegrees(self.pitch))
  	
  	self.f(self.leg*2-(self.toPixel(getLeg(self.heel_plum, self.heel_cut))+self.toPixel(getLeg(12, self.pitch))))
  	self.u()
  	
  	def wall(o):
  		wt = t.Turtle()
  		wt.color('tan')
  		wt.speed(0)
  		wt.ht()
  		wt.pu()
  		wt.goto(o.heel_corner)
  		wt.pd()
  		wt.fd(o.toPixel(5.5))
  		wt.right(90)
  		wt.fd(o.toPixel(1.5))
  		wt.right(90)
  		wt.fd(o.toPixel(5.5))
  		wt.right(90)
  		wt.fd(o.toPixel(1.5))
  		wt.right(90)
  		wt.fd(o.toPixel(5.5))
  		wt.right(90)
  		wt.fd(o.toPixel(3))
  		wt.right(90)
  		wt.fd(o.toPixel(5.5))
  		wt.right(90)
  		wt.fd(o.toPixel(1.5))
  		wt.right(90)
  		wt.fd(o.toPixel(5.5))
  		wt.right(90)
  		wt.sety(0)
  		wt.right(90)
  		wt.fd(o.toPixel(5.5))
  		wt.right(90)
  		wt.goto(o.heel_corner)
  		
  	def ruler(o):
  		rt = t.Turtle()
  		rt.color('red')
  		rt.speed(0)
  		rt.hideturtle()
  		rt.penup()
  		rt.goto(o.rafters['peak']['x'] - 50, o.rafters['peak']['y'])
  		rt.stamp()
  		top = rt.pos()
  		rt.pendown()
  		rt.backward((o.run-50)/2)
  		info_ft, info_in = o.convert(o.width/2)
  		rt.write(str(info_ft) + "' " + str(info_in) + '"')
  		rt.backward((o.run-50)/2)
  		corner = rt.pos()
  		rt.right(45)
  		rt.width(2)
  		rt.fd(10)
  		rt.backward(15)
  		rt.fd(5)
  		rt.right(45)
  		rt.width(1)
  		rt.fd((o.rise*2-50)/2)
  		info_ft, info_in = o.convert(o.rise/o.scale_to)
  		rt.write(str(info_ft) + "' " + str(info_in) + '"')
  		rt.fd((o.rise*2-50)/2)
  		rt.stamp()
  		bottom = rt.pos()
  		rt.left(90+toDegrees(o.pitch))
  		rt.goto(bottom[0]+((top[0]-bottom[0])/2), bottom[1]+((abs(top[1])-abs(bottom[1]))/2))
  		info_ft, info_in = o.convert(o.leg/o.scale_to)
  		rt.write(str(info_ft) + "' " + str(info_in) + '"')
  		leg_center = rt.pos()
  		rt.goto(top[0], top[1])
  		rt.pu()
  		rt.goto(o.heel_corner[0]+o.toPixel(12), o.heel_corner[1])
  		rt.write("heel cut: " + str(float(o.heel_cut)))
  	wall(self)
  	ruler(self)
  def roof(self):
  	self.turtle.home()
  	self.turtle.color("green")
  	self.turtle.hideturtle()
  	self.u()
  	self.turtle.goto(bounds('b'), (self.turtle.ycor() + (600 - self.rise)))
  	self.b(self.run/2)
  	self.fascia_left = self.turtle.pos()
  	self.l(toDegrees(self.pitch))
  	self.d()
  	self.f(self.leg)
  	self.peak = {"x": self.turtle.xcor(), "y": self.turtle.ycor()}
  	self.turtle.write(str(self.pitch) + " pitch / " + str(round(toDegrees(self.pitch), 2)) + "°")
  	self.r((toDegrees(self.pitch) * 2))
  	self.f(self.leg)
  	self.fascia_right = self.turtle.pos()
  	self.r(90 + revDegrees(toDegrees(self.pitch)))
  	self.f(self.run)
  	self.u()
  	
  def house(self):
  	self.turtle.color("black")
  	self.l(90)
  	self.f(self.run/2)
  	self.l(90)
  	self.f(self.run)
  	self.l(90)
  	self.f(self.run/2)
    
  	
  
def main():
	ol = builder()
	ol.rafter()
	ol.roof()
	ol.house()
	ol.screen.onclick(ol.done)
	ol.screen.mainloop()

def doLoop():
	i = 0.05
	run = 200
	while run > 1:
		run = 200 - i
		ol = builder(i, run)
		ol.roof()
		del ol
		i += 0.5
		
main()
#doLoop()

t.mainloop()
