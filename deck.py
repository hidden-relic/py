import turtle
import fractions
from tkinter import messagebox

DEBUG = True

def convert(n):
	dec_ft = n/12	# get feet (float)
	ret_ft = int(n/12)	# get feet (int)
	dec_in = (dec_ft-ret_ft)*12 # get the decimal remainder by subtracting the int from the float, then multiply by 12 to get inches (float)
	ret_in = int(dec_in)	# get inches (int)
	ret_fr = fractions.Fraction(dec_in-ret_in) # get the fraction of the inch by subtracting int from float and converting the float to a fraction object
	ret_fr = ret_fr.limit_denominator(8) # return the fraction in 8th's, simplified 
	if ret_fr == 0:
		ret_fr = ''	# if no fraction, use empty str
	return ret_ft, ret_in, ret_fr	# return 3 values either as an array or assigned to 3 separate vars
	
class deck:
	def __init__(self):
		self.t = turtle.Turtle()
		self.screen = self.t.getscreen()
		self.screen.setup(0.9, 0.9, 10, 10)	# window sizing to 9/10ths of screen resolution, offset from top left by x10, y10
		self.win_width=self.screen.window_width()*0.9
		self.win_height=self.screen.window_height()*0.9
		self.screen.screensize(self.win_width, self.win_height)	# drawing area sizing to 9/10ths of window
		self.axis_ratio=self.win_width/self.win_height	# get a width:height ratio as a float
		self.screen.update()
		self.t.reset()
		self.t.speed(0)
		self.t.width(1)
		self.t.ht()
		self.width = turtle.numinput('dimensions', 'width along building', 192)
		self.length = turtle.numinput('dimensions', 'length from building', 144)
		self.material = turtle.numinput('dimensions', 'width of material', 5.5)
		self.overhang = turtle.numinput('dimensions', 'overhang of deck boards', 1.5)
		self.gap =  turtle.numinput('dimensions', 'gap between boards', 0.25)
		# self.width, self.length, self.material, self.overhang, self.gap = 192, 144, 5.5, 1.5, 0.25
		
		self.joist_count=0
		self.deckboard_count=0
		self.joist_length = self.length-3
		self.deckboard_length = self.width+(self.overhang*2)
		self.mat_width = 1.5
	
		# self.scale = self.win_width/self.width if (self.axis_ratio < ((self.win_width/self.width)/(self.win_height/self.length))) else self.win_height/self.length
		self.scale = self.win_width/self.width if (self.axis_ratio <= (self.width/self.length)) else self.win_height/self.length
		self.inch = self.scale
	
		self.bounds={'left': -(self.toScale(self.width/2)), 'right': (self.toScale(self.width/2)), 'top': (self.toScale(self.length/2)), 'bottom': -(self.toScale(self.length/2))} # grabbing the real coordinates for edges of drawing area
		self.bounds['l'], self.bounds['r'], self.bounds['t'], self.bounds['b']=self.bounds['left'], self.bounds['right'], self.bounds['top'], self.bounds['bottom'] # creating an alias for the bounds ('top' as 't', etc)
		# bounds are the limits of the FRAMING, not the overhang of deck boards. this determines the start position, and the outer bounds
		if DEBUG:
			self.log = open('C:\\giz\\lib\\builder\\log.txt', 'w')
			self.log.write('')
			self.log.close()
			del self.log
			self.log = open('C:\\giz\\lib\\builder\\log.txt', 'a')
			
		logger = self.log.write('window width: '+str(self.screen.window_width())+'\twindow height: '+str(self.screen.window_height())) if DEBUG else ''
		logger = self.log.write('\ndrawing area width: '+str(self.win_width)+'\tdrawing area height: '+str(self.win_height)) if DEBUG else ''
		logger = self.log.write('\nbounds: '+str(self.bounds)) if DEBUG else ''
		logger = self.log.write('\nscale: '+str(self.scale)) if DEBUG else ''
		logger = self.log.write('\nwidth: '+str(self.width)+'\tscaled: '+str(self.toScale(self.width))) if DEBUG else ''
		logger = self.log.write('\nlength: '+str(self.length)+'\tscaled: '+str(self.toScale(self.length))) if DEBUG else ''

	def f(self, n):
		self.t.forward(self.toScale(n))
	def b(self, n):
		self.t.backward(self.toScale(n))
			
	def l(self, d):
		self.t.left(d)
	def r(self, d):
		self.t.right(d)
	
	def g(self, x, y):
		logger = self.log.write('Goto: '+str(x)+', '+str(y)+'\n') if DEBUG else ''
		self.u()
		self.t.goto(x, y)
	
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
		return n*self.scale

	def fromScale(self, n):
		return n/self.scale

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
			self.t.begin_fill()
			self.rect('v', self.length-3)
			self.t.end_fill()
			self.joist_count += 1
			logger = self.log.write('Joist #'+str(self.joist_count)+': '+str(self.t.pos())+'\n') if DEBUG else ''
		
		def decking():
			self.rect('h', self.width+(self.overhang*2))
			self.deckboard_count += 1
			logger = self.log.write('Deckboard #'+str(self.deckboard_count)+': '+str(self.t.pos())+'\n') if DEBUG else ''

		self.t.fillcolor('#007200')
		self.g(self.bounds['l'], self.bounds['t'])
		
		# self.log('outer rim')
		self.t.begin_fill()
		self.rect('h', self.width) # outer rim
		self.t.end_fill()
		self.y(self.toScale(-(self.length-1.5)))
		self.t.begin_fill()
		self.rect('h', self.width) # ledger
		self.t.end_fill()
		self.y(self.toScale((self.length-3)))
		joist() # first joist (outer rim)
		first_joist = self.t.pos()
		self.x(self.toScale(15.25))
		second_joist = self.t.pos()
		logger = self.log.write('\nfirst joist: '+str(first_joist)+'\t'+'second joist: '+str(second_joist)+'\ndifference: '+str(abs(first_joist-second_joist))+'\tdescaled: '+str(self.fromScale(abs(first_joist-second_joist)))) if DEBUG else ''
		joist() # second joist (15 1/4" from outside
					# of first joist to inside of second to
					# create true 16 on-center. every joist
					# after will be 16" away, except the last)
		limit = int(self.bounds['r'])-(self.toScale((16+1.5)))
		while self.t.xcor() < limit:
			self.x(self.toScale(16))
			joist()
		self.g(self.bounds['r']-(self.toScale(1.5)), self.t.ycor())
		joist()
		self.t.end_fill()

		self.t.color('brown')
		self.setMaterial(self.material)
		self.g(self.bounds['l'], self.bounds['t'])
		self.y(self.toScale(self.overhang))
		self.x(self.toScale(-self.overhang))
		# self.log('outer decking')
		limit = self.bounds['b']+(self.toScale(self.mat_width))+(self.toScale(self.gap))
		i = 1
		while self.t.ycor() > limit:
			i += 1
			# self.log('deckboard #' + str(i))
			decking()
			self.y(self.toScale(-(self.mat_width+self.gap)))
			
		self.setMaterial(self.fromScale(abs(self.bounds['bottom'])-abs(self.t.ycor())))
		logger = self.log.write('material size: '+str(self.mat_width)) if DEBUG else ''
		decking()

		self.ripft, self.ripin, self.ripfr = convert(self.mat_width)
		self.g(0, 0)
		self.y(self.toScale(-10))
		self.y(self.toScale(-10))
		self.joist_lengthft, self.joist_lengthin, self.joist_lengthfr = convert(self.joist_length)
		self.deckboard_lengthft, self.deckboard_lengthin, self.deckboard_lengthfr = convert(self.deckboard_length)
		
#turtle.tracer(2, 0)
test = deck()
test.draw()
data = 'Number of joists: '+str(test.joist_count)+'\tJoist Length: '+str(test.joist_lengthft)+"' "+str(test.joist_lengthin)+' '+str(test.joist_lengthfr)+'"\nNumber of deck boards: '+str(test.deckboard_count)+'\tDeckboard Length: '+str(test.deckboard_lengthft)+"' "+str(test.deckboard_lengthin)+' '+str(test.deckboard_lengthfr)+'"\nDeck board rip: '+str(test.ripft)+"' "+str(test.ripin)+' '+str(test.ripfr)+'"'

messagebox.showinfo('Data', data)
test.log.write('\nNumber of joists: '+str(test.joist_count)+'\tJoist Length: '+str(test.joist_lengthft)+"' "+str(test.joist_lengthin)+' '+str(test.joist_lengthfr)+'"')
test.log.write('\nNumber of deck boards: '+str(test.deckboard_count)+'\tDeckboard Length: '+str(test.deckboard_lengthft)+"' "+str(test.deckboard_lengthin)+' '+str(test.deckboard_lengthfr)+'"')
test.log.write('\nDeck board rip: '+str(test.ripft)+"' "+str(test.ripin)+' '+str(test.ripfr)+'"')
test.log.close()
info = turtle.Turtle()

turtle.mainloop()
