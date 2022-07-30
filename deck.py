#pylint:disable=C0103

import turtle as turt
import fractions
from os.path import exists as file_exists

def convert(m):
	dec_ft = m/12
	ret_ft = int(m/12)
	dec_in = (dec_ft-ret_ft)*12
	ret_in = int(dec_in)
	ret_fr = fractions.Fraction(dec_in-ret_in)
	ret_fr = ret_fr.limit_denominator(8)
	if ret_fr == 0:
		ret_fr = ''
	return ret_ft, ret_in, ret_fr
	
def bounds(vert=0, horz=0):
	top = ['top', 't']
	bot = ['bottom', 'b']
	left = ['left', 'l']
	right = ['right', 'r']
	if vert in top:
		vert = 650
	elif vert in bot:
		vert = -650
	elif vert in left:
		vert = -325
	elif vert in right:
		vert = 325
	if horz in left:
		horz = -325
	elif horz in right:
		horz = 325
	if vert != 0 and horz == 0:
		return vert
	if vert != 0 and horz != 0:
		return (horz, vert)
	if vert == 0 and horz != 0:
		return horz
	return (horz, vert)
	
class log:
	current_pos_x = 0
	current_pos_y = 0
	step = 0
	
	def __init__(self, t):
		self.logfile = 'C:\giz\log.txt'
		self.file = open(self.logfile, 'w')
		self.file.write('')
		self.file.close()
		self.file = open(self.logfile, 'a')
	
		
	def __call__(self, data=''):
		self.step += 1
		x = ''
		y = ''
		arrow = '□'
		self.file.write('(' + str(self.step) + ')\t')
		if self.t.xcor() > self.current_pos_x:
			x = self.t.xcor()-self.current_pos_x
			arrow = '→'
		elif self.t.xcor() < self.current_pos_x:
			x = self.t.xcor()-self.current_pos_x
			arrow = '←'
		elif self.t.ycor() > self.current_pos_y:
			y = self.t.ycor()-self.current_pos_y
			arrow = '↑'
		elif self.t.ycor() < self.current_pos_y:
			y = self.t.ycor()-self.current_pos_y
			arrow = '↓'
		if x:
			self.file.write(str(x) + '\t')
			self.file.write(str(arrow))
		if y:
			self.file.write(str(y) + '\t')
			self.file.write(str(arrow))
		self.file.write('\t[x' + str(self.t.xcor()) + ', y' + str(self.t.ycor()) + ']\n')
		self.file.write('\t>' + str(data) + '\n\n')
			
		self.current_pos_x += self.t.xcor()
		self.current_pos_y += self.t.ycor()
	
class deck:
	def __init__(self):
		self.t = turt.Turtle()
		self.t.speed(0)
		self.t.width(1)
		self.t.ht()
		self.width = turt.numinput('dimensions', 'width along building', 192)
		self.length = turt.numinput('dimensions', 'length from building', 144)
		self.material = turt.numinput('dimensions', 'width of material', 5.5)
		self.overhang = turt.numinput('dimensions', 'overhang of deck boards', 0.75)
		self.gap =  turt.numinput('dimensions', 'gap between boards', 0.125)
		self.inch = 8
		self.mat_width = 1.5
		# self.log = log(turt.Turtle())
		#self.log('UNSCALED\tinch: ' + str(self.inch) + ' width: ' + str(self.width) + ' length: ' + str(self.length) + ' material: ' + str(self.material) + ' overhang: ' + str(self.overhang) + ' gap: ' + str(self.gap))
		self.scale = 650/(self.width*self.inch)
		self.inch = 8*self.scale
		#self.log('SCALED\tinch: ' + str(self.inch) + ' width: ' + str(self.width*self.inch) + ' length: ' + str(self.length*self.inch) + ' material: ' + str(self.material*self.inch) + ' overhang: ' + str(self.overhang*self.inch) + ' gap: ' + str(self.gap*self.inch))

	def f(self, n):
		self.t.forward(self.inch*n)
		#self.log()

	def b(self, n):
		self.t.backward(self.inch*n)
		#self.log()
			
	def l(self, d):
		self.t.left(d)
	def r(self, d):
		self.t.right(d)
	def g(self, xy):
		self.u()
		self.t.goto(xy)
		#self.log()
		self.d()
	def u(self):
		self.t.penup()
	def d(self):
		self.t.pendown()
	def x(self, n):
		self.g((self.t.xcor()+(n*self.inch), self.t.ycor()))
	def y(self, n):
		self.g((self.t.xcor(), self.t.ycor()+(n*self.inch)))
	def w(self, arg, align='center', font='Verdana', fontsize=6):
		self.t.write(arg, align=align, font=(font, fontsize))
		
	def setMaterial(self, n):
		self.mat_width = n
		
	def rect(self, orient, i):
		if orient == 'v':
			self.t.seth(0)
			self.f(self.mat_width)
			self.r(90)
			self.f(i)
			self.r(90)
			self.f(self.mat_width)
			self.r(90)
			self.f(i)
		elif orient == 'h':
			self.t.seth(0)
			self.f(i)
			self.r(90)
			self.f(self.mat_width)
			self.r(90)
			self.f(i)
			self.r(90)
			self.f(self.mat_width)
			
	def draw(self):
		def joist():
			self.rect('v', self.length-3)
		
		def decking():
			self.rect('h', self.width+(self.overhang*2))
		
		self.t.color('#007200')
		self.g((bounds('t', 'l')))
		self.log('outer rim')
		self.rect('h', self.width) # outer rim
		self.y(-(self.length-1.5))
		self.rect('h', self.width) # ledger
		self.y((self.length-3))
		joist() # first joist (outer rim)
		self.x(15.25)
		joist() # second joist (15 1/4" from outside
					# of first joist to inside of second to
					# create true 16 on-center. every joist
					# after will be 16" away, except the last)
		limit = int(bounds('r'))-((16+1.5)*self.inch)
		while self.t.xcor() < limit:
			self.x(16)
			joist()
		self.g((bounds('r')-(1.5*self.inch), self.t.ycor()))
		joist()
		
		self.t.color('brown')
		self.setMaterial(self.material)
		self.g(bounds('t', 'l'))
		self.y(self.overhang)
		self.x(-self.overhang)
		self.log('outer decking')
		limit = bounds('t')-(self.length*self.inch)+(self.mat_width*self.inch)+(self.gap*self.inch)
		i = 1
		while self.t.ycor() > limit:
			i += 1
			self.log('deckboard #' + str(i))
			decking()
			self.y(-(self.mat_width+self.gap))
			
		ripft, ripin, ripfr = convert(self.t.ycor()-limit)
		self.g((0, 0))
		self.w(str(limit))
		self.y(-10)
		self.w(str((bounds('t')+(self.overhang*self.inch))-limit))
		self.y(-10)
		self.w(str(((bounds('t')+(self.overhang*self.inch)-limit)/self.inch)))
		
test = deck()
test.draw()
turt.mainloop()
