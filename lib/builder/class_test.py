class a:
	def __init__(self):
		self.var=1
		self.vara='a'
	def show(self):
		print(self.var, self.vara)
class b(a):
	def __init__(self):
		super().__init__()
		self.var=2
		self.varb='b'
	def show(self):
		print(self.var, self.vara, self.varb)
class c:
	def __init__(self, b):
		self.b=b
		self.var=3
		self.varc='c'
	def show(self):
		print(self.var, self.b.vara, self.b.varb, self.varc, self.b.show())

test=a()
test.show()
test2=b()
test2.show()
test3=c(test2)
test3.show()