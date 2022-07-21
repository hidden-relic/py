from tkinter import messagebox
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
	

# class log:
# 	current_pos_x = 0
# 	current_pos_y = 0
# 	step = 0
	
# 	def __init__(self, t):
# 		self.logfile = 'C:\giz\log.txt'
# 		if not file_exists(self.logfile):
# 			self.file = open(self.logfile, 'x')
# 		else:
# 			self.file = open(self.logfile, 'r')
# 			tst = self.file.readline(0)
# 			self.file.close()
# 			self.file = open(self.logfile, 'w')
# 			self.file.write('')
# 			self.file.close()
# 			self.file = open(self.logfile, 'a')
	
		
# 	def __call__(self, data=''):
# 		self.step += 1
# 		x = ''
# 		y = ''
# 		arrow = '□'
# 		self.file.write('(' + str(self.step) + ')\t')
# 		if self.t.xcor() > self.current_pos_x:
# 			x = self.t.xcor()-self.current_pos_x
# 			arrow = '→'
# 		elif self.t.xcor() < self.current_pos_x:
# 			x = self.t.xcor()-self.current_pos_x
# 			arrow = '←'
# 		elif self.t.ycor() > self.current_pos_y:
# 			y = self.t.ycor()-self.current_pos_y
# 			arrow = '↑'
# 		elif self.t.ycor() < self.current_pos_y:
# 			y = self.t.ycor()-self.current_pos_y
# 			arrow = '↓'
# 		if x:
# 			self.file.write(str(x) + '\t')
# 			self.file.write(str(arrow))
# 		if y:
# 			self.file.write(str(y) + '\t')
# 			self.file.write(str(arrow))
# 		self.file.write('\t[x' + str(self.t.xcor()) + ', y' + str(self.t.ycor()) + ']\n')
# 		self.file.write('\t>' + str(data) + '\n\n')
			
# 		self.current_pos_x += self.t.xcor()
# 		self.current_pos_y += self.t.ycor()
	
class deck:
	def __init__(self):
		self.t = turt.Turtle()
		self.screen = self.t.getscreen()
		self.screen.setup(0.9, 0.9, 10, 10)
		self.win_width=self.screen.window_width()*0.9
		self.win_height=self.screen.window_height()*0.9
		self.screen.screensize(self.win_width, self.win_height)
		self.axis_ratio=self.win_width/self.win_height
		self.bounds={'left': -(self.win_width)/2, 'right': (self.win_width)/2, 'top': (self.win_height)/2, 'bottom': -(self.win_height)/2}
		self.bounds['l'], self.bounds['r'], self.bounds['t'], self.bounds['b']=self.bounds['left'], self.bounds['right'], self.bounds['top'], self.bounds['bottom']
		# messagebox.showinfo('self.bounds: ', self.bounds['r'])
		self.screen.update()
		self.t.reset()
		self.t.speed(0)
		self.t.width(1)
		self.t.ht()
		self.width = turt.numinput('dimensions', 'width along building', 192)
		self.length = turt.numinput('dimensions', 'length from building', 144)
		self.material = turt.numinput('dimensions', 'width of material', 5.5)
		self.overhang = turt.numinput('dimensions', 'overhang of deck boards', 1.5)
		self.gap =  turt.numinput('dimensions', 'gap between boards', 0.25)
		self.joist_count=0
		self.deckboard_count=0
		self.joist_length = self.length-3
		self.deckboard_length = self.width+(self.overhang*2)
		self.inch = 8
		self.mat_width = 1.5
		#self.log = log(turt.Turtle())
		#self.log('UNSCALED\tinch: ' + str(self.inch) + ' width: ' + str(self.width) + ' length: ' + str(self.length) + ' material: ' + str(self.material) + ' overhang: ' + str(self.overhang) + ' gap: ' + str(self.gap))
		self.scale = self.win_width/(self.width*self.inch) if (self.axis_ratio < (self.win_width/(self.width*self.inch)/self.win_height/(self.length*self.inch))) else self.win_height/(self.length*self.inch)
		self.width_scale = self.win_heightlength
		#self.bounds['right'] = (self.win_width*(/2 if (self.axis_ratio < (self.win_width/(self.width*self.inch)/self.win_height/(self.length*self.inch))) else self.win_height/(self.length*self.inch)
		self.inch = self.inch*self.scale
		#self.log('SCALED\tinch: ' + str(self.inch) + ' width: ' + str(self.width*self.inch) + ' length: ' + str(self.length*self.inch) + ' material: ' + str(self.material*self.inch) + ' overhang: ' + str(self.overhang*self.inch) + ' gap: ' + str(self.gap*self.inch))
		self.log = open('C:\\giz\\lib\\builder\\log.txt', 'a')
		self.log.write('width: '+str(self.width)+'\tscaled: '+str(self.toScale(self.width)))
		self.log.write('length: '+str(self.length)+'\tscaled: '+str(self.toScale(self.length)))
		self.log.write('scale: '+str(self.scale)+'\tinch: '+str(self.inch))

	def f(self, n):
		self.t.forward(self.toScale(n))
		#self.log()

	def b(self, n):
		self.t.backward(self.toScale(n))
		#self.log()
			
	def l(self, d):
		self.t.left(d)
	def r(self, d):
		self.t.right(d)
	def g(self, x, y):
		self.u()
		self.t.goto(x, y)
		#self.log()
		self.d()
	def u(self):
		self.t.penup()
	def d(self):
		self.t.pendown()
	def x(self, n):
		self.g(self.t.xcor()+n, self.t.ycor())
	def y(self, n):
		self.g(self.t.xcor(), self.t.ycor()+n)
	def w(self, arg, align='center', font='Verdana', fontsize=6):
		self.t.write(arg, align=align, font=(font, fontsize))
		
	def setMaterial(self, n):
		self.mat_width = n

	def toScale(self, n):
		return n*self.inch

	def fromScale(self, n):
		return n/self.inch

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
			self.joist_count += 1
		
		def decking():
			self.rect('h', self.width+(self.overhang*2))
			self.deckboard_count += 1
		
		self.t.color('#007200')
		self.g(self.bounds['l'], self.bounds['t'])
		
		# self.log('outer rim')
		self.rect('h', self.width) # outer rim
		self.y(self.toScale(-(self.length-1.5)))
		self.rect('h', self.width) # ledger
		self.y(self.toScale((self.length-3)))
		joist() # first joist (outer rim)
		first_joist_x = self.t.xcor()
		self.x(self.toScale(15.25))
		second_joist_x = self.t.xcor()
		self.log.write('first joist: '+str(first_joist_x)+'\t'+'second joist: '+str(second_joist_x)+'\tdifference: '+str(abs(first_joist_x-second_joist_x))+'\tscaled: '+str(self.toScale(abs(first_joist_x-second_joist_x))))
		joist() # second joist (15 1/4" from outside
					# of first joist to inside of second to
					# create true 16 on-center. every joist
					# after will be 16" away, except the last)
		limit = int(self.fromScale(self.bounds['r']))-(self.toScale((16+1.5)))
		while self.t.xcor() < limit:
			self.x(self.toScale(16))
			joist()
		self.g(self.bounds['r']-(self.toScale(1.5)), self.t.ycor())
		joist()
		
		self.t.color('brown')
		self.setMaterial(self.material)
		self.g(self.bounds['l'], self.bounds['t'])
		self.y(self.toScale(self.overhang))
		self.x(self.toScale(-self.overhang))
		# self.log('outer decking')
		limit = self.bounds['t']-(self.toScale(self.length))+(self.toScale(self.mat_width))+(self.toScale(self.gap))
		i = 1
		while self.t.ycor() > limit:
			i += 1
			# self.log('deckboard #' + str(i))
			decking()
			self.y(self.toScale(-(self.mat_width+self.gap)))
			
		ripft, ripin, ripfr = convert(self.t.ycor()-limit)
		self.g(0, 0)
		self.y(self.toScale(-10))
		self.y(self.toScale(-10))
		
test = deck()
test.draw()
turt.mainloop()
