#pylint:disable=R0902
#pylint:disable=R1705
#pylint:disable=C0103
#pylint:disable=C0301
#pylint:disable=R0915
#pylint:disable=E1101
#pylint:disable=W0602
#pylint:disable=C0116
#pylint:disable=E0001
import math
import fractions
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from turtle import RawTurtle

myfont = ('Verdana', 10)
infofont = ('Verdana', 8)
b_w = {}
d_w = {}
d_l = {}
vals = {'ft': [], 'in': []}
cv = {}

for i in range(0, 500):
	vals['ft'].append(i)
	if i < 12:
		vals['in'].append(i)

def toDegrees(pitch):
	return math.degrees(math.atan(pitch/12))

def supplementary(degree):
	return 90 - degree
	
def getLeg(a, b):
	return math.sqrt((a**2)+(b**2))
	
def convert(m):
	dec_ft = m/12
	ret_ft = int(m/12)
	dec_in = (dec_ft-ret_ft)*12
	ret_in = int(dec_in)
	ret_fr = fractions.Fraction(dec_in-ret_in)
	ret_fr = ret_fr.limit_denominator(16)
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
	
def checkNum(n):
	if n.isdigit():
		return True
	elif n == '':
		messagebox.showerror('Input', 'Please input a number')
		return False
	else:
		messagebox.showerror('Input', 'Only accepts number values')
		return False
	
def roofClicked():
	o = {}
	o['width'] = int(b_w['ft'].get())*12+int(b_w['in'].get())+float(fractions.Fraction(b_w['fr'].get()))
	o['pitch'] = float(b_w['pitch'].get())
	o['cv'] = cv
	if o['width'] and o['pitch'] > 0:
		o['t'] = RawTurtle(canvas=cv)
		o['screen'] = o['t'].getscreen()
		o['tail'] = int(b_w['tail'].get())
		o['outline'] = sketchRoof(o)
		
def sketchRoof(o):
	ol = builder(o)
	ol.rafter()
	ol.roof()
	ol.house()
	ol.screen.onclick(ol.roofdone)
	ol.screen.mainloop()
	return ol
		
def deckClicked():
		pass
		
def sketchDeck(o):
	pass

def main():
	global cv
	root = tk.Tk()
	root.title("Builder")
	root.geometry('350x200')
	
	# notebook
	nb = ttk.Notebook(root)
	nb.pack(pady = 10, side = 'top')
	
	# Roof tab
	tab_roof = tk.Frame(nb, width = 400, height = 280)
	tab_roof.pack(fill = 'both', expand = True)
	nb.add(tab_roof, text = 'Roof')
	
		# - Building width frame
	b_w_frame = tk.Frame(tab_roof)
			# - - label frame
	b_w_lbl_frame = tk.Frame(b_w_frame)
	tk.Label(b_w_lbl_frame, text = "Building width:", font = myfont).pack(side = 'top', padx=12, pady=1)
	b_w_lbl_frame.pack(side = 'top')
			# - - measurements frame
	b_w_measurements_frame = tk.Frame(b_w_frame)
				# - - - ft frame
	b_w_ft_frame = tk.Frame(b_w_measurements_frame)
	b_w_ft_frame.grid(column = 0, row = 0, sticky = 'w')
	tk.Label(b_w_ft_frame, text = "ft.", font = myfont).pack(padx = 6, ipadx = 12)
	
	b_w['ft'] = ttk.Combobox(b_w_ft_frame, height = 20, width = 6, values = tuple(vals['ft']), font = myfont, state = 'readonly')
	b_w['ft'].pack(padx = 6, pady=12, ipadx = 12)
	b_w['ft'].set(10)
				# - - - in frame
	b_w_in_frame = tk.Frame(b_w_measurements_frame)
	b_w_in_frame.grid(column = 1, row = 0)
	tk.Label(b_w_in_frame, text = "in.", font = myfont).pack(padx = 6, ipadx = 12)
	b_w['in'] = ttk.Combobox(b_w_in_frame, height = 20, width = 6, values = tuple(vals['in']), font = myfont, state = 'readonly')
	b_w['in'].pack(padx = 6, pady=12, ipadx = 12)
	b_w['in'].set(0)
				# - - - fraction frame
	b_w_fr_frame = tk.Frame(b_w_measurements_frame)
	b_w_fr_frame.grid(column = 2, row = 0, sticky = 'e')
	tk.Label(b_w_fr_frame, text = bytes.fromhex('BE'), font = myfont).pack(padx = 6, ipadx = 12)
	b_w['fr'] = ttk.Combobox(b_w_fr_frame, height = 20, width = 6, values = ("0", "1/16", "1/8", "3/16", "1/4", "5/16", "3/8", "7/16", "1/2", "9/16", "5/8", "11/16", "3/4", "13/16", "7/8", "15/16"), font = myfont, state = 'readonly')
	b_w['fr'].pack(padx = 6, pady=12, ipadx = 12)
	b_w['fr'].set(0)
	b_w_measurements_frame.pack(side = 'top')
	
	b_w_frame.pack(fill = 'x')
	
	sep = ttk.Separator(b_w_frame, orient='horizontal')
	sep.pack(fill='both', pady=12)
	
	other_frame = tk.Frame(tab_roof)
	pitch_lbl = tk.Label(other_frame, text = 'Pitch: ', font = myfont)
	pitch_lbl.pack(side = 'left', padx=12, pady = 12)
	b_w['pitch'] = tk.Entry(other_frame, width=4, font=myfont, justify='center')
	b_w['pitch'].pack(side = 'left', padx=12, pady=12)
	b_w['pitch'].insert(0, 9)
	
	b_w['tail'] = tk.Entry(other_frame, width=4,  font=myfont, justify='center')
	b_w['tail'].pack(side = 'right', padx=12, pady=12)
	b_w['tail'].insert(0, 12)
	tail_lbl = tk.Label(other_frame, text = 'Soffit: ', font = myfont)
	tail_lbl.pack(side = 'right', padx=12, pady = 12)
	
	other_frame.pack(fill='x', padx=12)
	
	reg = root.register(checkNum)
	b_w['pitch'].config(validate = "key", validatecommand = (reg, '%P'))
	
	btn = tk.Button(tab_roof, text = "GO", command = roofClicked)
	btn.pack()
	
	# --------------------‐-------------------------------------------------------- #
	
		# Deck tab
	tab_deck = tk.Frame(nb, width = 400, height = 280)
	tab_deck.pack(fill = 'both', expand = True)
	nb.add(tab_deck, text = 'Deck')
	
		# - Deck width frame
	d_w_frame = tk.Frame(tab_deck)
			# - - label frame
	d_w_lbl_frame = tk.Frame(d_w_frame)
	tk.Label(d_w_lbl_frame, text = "Deck width:", font = myfont).pack(side = 'top', padx=12, pady=1)
	tk.Label(d_w_lbl_frame, text = "(Along Building)", font = infofont, fg='orange').pack(side = 'top', padx=12, pady=1)
	d_w_lbl_frame.pack(side = 'top')
			# - - measurements frame
	d_w_measurements_frame = tk.Frame(d_w_frame)
				# - - - ft frame
	d_w_ft_frame = tk.Frame(d_w_measurements_frame)
	d_w_ft_frame.grid(column = 0, row = 0, sticky = 'w')
	tk.Label(d_w_ft_frame, text = "ft.", font = myfont).pack(padx = 6, ipadx = 12)
	
	d_w['ft'] = ttk.Combobox(d_w_ft_frame, height = 20, width = 6, values = tuple(vals['ft']), font = myfont, state = 'readonly')
	d_w['ft'].pack(padx = 6, pady=12, ipadx = 12)
	d_w['ft'].set(10)
				# - - - in frame
	d_w_in_frame = tk.Frame(d_w_measurements_frame)
	d_w_in_frame.grid(column = 1, row = 0)
	tk.Label(d_w_in_frame, text = "in.", font = myfont).pack(padx = 6, ipadx = 12)
	
	d_w['in'] = ttk.Combobox(d_w_in_frame, height = 20, width = 6, values = tuple(vals['in']), font = myfont, state = 'readonly')
	d_w['in'].pack(padx = 6, pady=12, ipadx = 12)
	d_w['in'].set(0)
				# - - - fraction frame
	d_w_fr_frame = tk.Frame(d_w_measurements_frame)
	d_w_fr_frame.grid(column = 2, row = 0, sticky = 'e')
	tk.Label(d_w_fr_frame, text = bytes.fromhex('BE'), font = myfont).pack(padx = 6, ipadx = 12)
	
	d_w['fr'] = ttk.Combobox(d_w_fr_frame, height = 20, width = 6, values = ("0", "1/16", "1/8", "3/16", "1/4", "5/16", "3/8", "7/16", "1/2", "9/16", "5/8", "11/16", "3/4", "13/16", "7/8", "15/16"), font = myfont, state = 'readonly')
	d_w['fr'].pack(padx = 6, pady=12, ipadx = 12)
	d_w['fr'].set(0)
	d_w_measurements_frame.pack(side = 'top')
	d_w_frame.pack(fill = 'x')
	
			# - Deck width frame
	d_l_frame = tk.Frame(tab_deck)
			# - - label frame
	d_l_lbl_frame = tk.Frame(d_l_frame)
	tk.Label(d_l_lbl_frame, text = "Deck length:", font = myfont).pack(side = 'top', padx=12, pady=1)
	tk.Label(d_l_lbl_frame, text = "(Away from Building)", font = infofont, fg='orange').pack(side = 'top', padx=12, pady=1)
	d_l_lbl_frame.pack(side = 'top')
			# - - measurements frame
	d_l_measurements_frame = tk.Frame(d_l_frame)
				# - - - ft frame
	d_l_ft_frame = tk.Frame(d_l_measurements_frame)
	d_l_ft_frame.grid(column = 0, row = 0, sticky = 'w')
	tk.Label(d_l_ft_frame, text = "ft.", font = myfont).pack(padx = 6, ipadx = 12)
	
	d_l['ft'] = ttk.Combobox(d_l_ft_frame, height = 20, width = 6, values = tuple(vals['ft']), font = myfont, state = 'readonly')
	d_l['ft'].pack(padx = 6, pady=12, ipadx = 12)
	d_l['ft'].set(10)
				# - - - in frame
	d_l_in_frame = tk.Frame(d_l_measurements_frame)
	d_l_in_frame.grid(column = 1, row = 0)
	tk.Label(d_l_in_frame, text = "in.", font = myfont).pack(padx = 6, ipadx = 12)
	
	d_l['in'] = ttk.Combobox(d_l_in_frame, height = 20, width = 6, values = tuple(vals['in']), font = myfont, state = 'readonly')
	d_l['in'].pack(padx = 6, pady=12, ipadx = 12)
	d_l['in'].set(0)
				# - - - fraction frame
	d_l_fr_frame = tk.Frame(d_l_measurements_frame)
	d_l_fr_frame.grid(column = 2, row = 0, sticky = 'e')
	tk.Label(d_l_fr_frame, text = bytes.fromhex('BE'), font = myfont).pack(padx = 6, ipadx = 12)
	
	d_l['fr'] = ttk.Combobox(d_l_fr_frame, height = 20, width = 6, values = ("0", "1/16", "1/8", "3/16", "1/4", "5/16", "3/8", "7/16", "1/2", "9/16", "5/8", "11/16", "3/4", "13/16", "7/8", "15/16"), font = myfont, state = 'readonly')
	d_l['fr'].pack(padx = 6, pady=12, ipadx = 12)
	d_l['fr'].set(0)
	d_l_measurements_frame.pack(side = 'top')
	d_l_frame.pack(fill = 'x')
	
	sep = ttk.Separator(d_l_frame, orient='horizontal')
	sep.pack(fill='both', pady=12)
	
	btn = tk.Button(tab_deck, text = "GO", command = deckClicked)
	btn.pack()
	
	# sketch tab
	tab_sketch = ttk.Frame(nb, width = 750, height = 1400)
	tab_sketch.pack(fill = 'both', expand = True)
	nb.add(tab_sketch, text = 'Sketch')
	
	# canvas
	cv = tk.Canvas(tab_sketch,width=750,height=1400)
	cv.pack()

	
	root.mainloop()
	
class builder:
	"""builder drawer class"""
	def __init__(self, o):
		self.pitch = o['pitch']
		self.width = o['width']
		self.canvas = o['cv']
		self.rafter_width = 7.5
		self.run = 600
		self.run_steps = (self.run/2)/12
		self.rise = self.run_steps * self.pitch
		self.leg = getLeg(self.run/2, self.rise)
		self.rafters = {'peak': {'x': 0, 'y': 0}, 'wall': {'x': 0, 'y': 0}}
		self.rafters['tail'] = o['tail']
		self.turtle = o['t']
		self.screen = o['screen']
		self.turtle.speed(0)
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
		
	def roofdone(self, x, y):
		used = x + y
		self.screen.reset()
		del self
		return used
		
	def toPixel(self, m):
		return m * self.scale_to
		
	def rafter(self):
		self.turtle.color('brown')
		self.turtle.hideturtle()
		self.u()
		self.turtle.goto(self.turtle.xcor()+self.run/2, bounds('t') - self.toPixel(self.rafter_width))
		self.d()
		self.l(90) # bottom of ridge plum cut
		self.f(self.toPixel(self.rafter_width)) # to top of ridge plum cut
		self.rafters['peak']['x'] = self.turtle.xcor()
		self.rafters['peak']['y'] = self.turtle.ycor()
		self.l(90 + toDegrees(self.pitch))
		self.f(self.leg*2) # to top of plum wall
		self.rafters['wall']['x'] = self.turtle.xcor()
		self.rafters['wall']['y'] = self.turtle.ycor()
		self.l(supplementary(toDegrees(self.pitch)))
		self.f(self.toPixel(self.rafter_width))
		self.l(180 - supplementary(toDegrees(self.pitch)))
		self.f(self.toPixel(getLeg(self.pitch, self.rafters['tail'])))
		self.l(supplementary(toDegrees(self.pitch)))
		
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
			wt = RawTurtle(canvas=cv)
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
			rt = RawTurtle(canvas=cv)
			rt.color('red')
			rt.speed(0)
			rt.hideturtle()
			rt.penup()
			rt.goto(o.rafters['peak']['x'] - 50, o.rafters['peak']['y'])
			rt.stamp()
			top = rt.pos()
			rt.pendown()
			rt.backward((o.run-50)/2)
			info_ft, info_in, info_frac = convert(o.width/2)
			rt.write(str(info_ft) + "' " + str(info_in) + ' ' + str(info_frac) + '"')
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
			info_ft, info_in, info_frac = convert(o.rise/o.scale_to)
			rt.write(str(info_ft) + "' " + str(info_in) + ' ' + str(info_frac) + '"')
			rt.fd((o.rise*2-50)/2)
			rt.stamp()
			bottom = rt.pos()
			rt.left(90+toDegrees(o.pitch))
			rt.goto(bottom[0]+((top[0]-bottom[0])/2), bottom[1]+((abs(top[1])-abs(bottom[1]))/2))
			info_ft, info_in, info_frac = convert(o.leg/o.scale_to)
			rt.write(str(info_ft) + "' " + str(info_in) + ' ' + str(info_frac) + '"')
			leg_center = rt.pos()
			rt.goto(top[0], top[1])
			rt.pu()
			rt.goto(o.heel_corner[0]+o.toPixel(12), o.heel_corner[1])
			heel_cut_ft, heel_cut_in, heel_cut_frac = convert(o.heel_cut)
			rt.write("heel cut: " + str(heel_cut_in) + ' ' + str(heel_cut_frac) + '"')
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
		self.r(90 + supplementary(toDegrees(self.pitch)))
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

if __name__ == "__main__":
	main()
	