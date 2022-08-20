import turtle

class t(turtle.Turtle):
	
	def __init__(self):
		super().__init__()
		self.tilt=45
		self.scale=1
	
	def supplement(self):
		return 90-self.tilt

	def scaled(self):
		self.scale*=0.66

	def scaleu(self, n):
		self.scale/=0.66

	def fix(self, n):
		return n*self.scale

	def f(self, n):
		self.forward(self.fix(n))
	def b(self, n):
		self.backward(self.fix(n))
			
	def l(self, d):
		self.left(d)
	def r(self,  d):
		self.right(d)

	def u(self):
		self.penup()
	def d(self):
		self.pendown()
	
	def g(self, x, y):
		self.u()
		self.goto(self.fix(x), self.fix(y))
		self.d()
	
	def x(self, n):
		self.g(self.unfix(self.xcor())+n, self.unfix(self.ycor()))
	def y(self, n):
		self.g(self.unfix(self.xcor()), self.unfix(self.ycor())+n)

	def north(self):
		self.seth(90)
	def south(self):
		self.seth(270)
	def east(self):
		self.seth(0)
	def west(self):
		self.seth(180)

	def square(self, x):
		for _ in range(4):
			self.f(self.fix(x))
			self.l(90)

	def fixedsquare(self, x):
		self.east()
		self.f(self.fix(x))
		self.north()
		self.f(self.fix(x))
		self.west()
		self.f(self.fix(x))
		self.south()
		self.f(self.fix(x))

	def rectangle(self, x, y):
		self.east()
		self.f(self.fix(x))
		self.south()
		self.f(self.fix(y))
		self.west()
		self.f(self.fix(x))
		self.north()
		self.f(self.fix(y))

	def cube(self, x):
		self.l(45)
		self.square(x)
		self.l(self.tilt)
		self.f(x)
		self.r(self.tilt)
		self.scaled()
		self.square(x)

n = t()
n.scale=0.5
n.cube(50)

