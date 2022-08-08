class Draw(RawTurtle):

	def __init__(self, canvas):
		super().__init__(canvas)
		self.speed(0)
		self.width(1)
		self.ht()


	def f(self, n):
		self.forward(self.fix(n))
	def b(self, n):
		self.backward(self.fix(n))
			
	def l(self, d):
		self.left(d)
	def r(self, d):
		self.right(d)
	
	def g(self, x, y):
		self.u()
		self.goto(x, y)
		self.d()

	def u(self):
		self.penup()
	def d(self):
		self.pendown()
	
	def x(self, n):
		self.g(self.xcor()+n, self.ycor())
	def y(self, n):
		self.g(self.xcor(), self.ycor()+n)

	def drawRoof(self):
		