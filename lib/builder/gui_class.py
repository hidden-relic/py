import tkinter as tk
from tkinter import ttk, messagebox
from turtle import Canvas, RawTurtle, TurtleScreen
import fractions
import math

class Framing:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.myfont = ("Verdana", 10)
		self.infofont = ("Verdana", 8)
		self.root = tk.Tk()
		# self.root.geometry(str(self.root.winfo_screenwidth())+'x'+str(self.root.winfo_screenheight())+'+0+0')
		self.vals = {"ft": [], "in": []}
		for i in range(0, 500):
			self.vals["ft"].append(i)
			if i < 12:
				self.vals["in"].append(i)
		self.myStyle=ttk.Style()
		self.myStyle.configure('Main.TNotebook.Tab', padding=[52, 8], font=self.myfont)
		self.myStyle.configure('Sub.TNotebook.Tab', padding=[27, 4], font=self.myfont)
		# self.myStyle.configure('TNotebook', tabposition='wn')
		self.offset=16
		self.roof_data=[]
		self.deck_data=[]
		self.resetData()

		self.buildNotebooks()
		self.buildRoofTab()
		self.buildDeckTab()

	def applyOffset(self, t):
		return (t[0]+self.offset, t[1]-self.offset)
	def applyScale(self, t):
		return (t[0]*self.scale, t[1]*self.scale)
	def fix(self, t):
		return self.applyScale(t)



	def buildMeasurementInput(self, parent, text, ft=True, inch=True, fr=True, defFt=0, defIn=0):
		o = {"ft": False, "in": False, "fr": False}
		base_frame=tk.Frame(parent)
		base_frame.pack(ipady=6)
		lbl_frame=tk.Frame(base_frame)
		tk.Label(lbl_frame, text=text, font=self.myfont).pack(side='top', padx=6, pady=1)
		lbl_frame.pack(side='top', ipady=6)
		main_frame = tk.Frame(base_frame)

		def buildMFt(self):
			ft_frame = tk.Frame(main_frame)
			ft_frame.grid(column=0, row=0, sticky="w")

			tk.Label(ft_frame, text="ft.", font=self.myfont).pack(padx=6, ipadx=6)
			ft = ttk.Combobox(ft_frame, height=20, width=6, values=tuple(self.vals["ft"]), font=self.myfont, state="readonly")
			ft.pack(padx=6, pady=6, ipadx=6)
			ft.set(defFt)
			return ft

		def buildMIn(self):
			in_frame = tk.Frame(main_frame)
			in_frame.grid(column=1, row=0)

			tk.Label(in_frame, text="in.", font=self.myfont).pack(padx=6, ipadx=6)
			inch = ttk.Combobox(in_frame, height=20, width=6, values=tuple(self.vals["in"]), font=self.myfont, state="readonly")
			inch.pack(padx=6, pady=6, ipadx=6)
			inch.set(defIn)
			return inch

		def buildMFr(self):
			fr_frame = tk.Frame(main_frame)
			fr_frame.grid(column=2, row=0, sticky="e")

			tk.Label(fr_frame, text=bytes.fromhex("BE"), font=self.myfont).pack(padx=6, ipadx=6)
			fr = ttk.Combobox(fr_frame, height=20, width=6, values=("0", "1/16", "1/8", "3/16", "1/4", "5/16", "3/8", "7/16", "1/2", "9/16", "5/8", "11/16", "3/4", "13/16", "7/8", "15/16"), font=self.myfont, state="readonly")
			fr.pack(padx=6, pady=6, ipadx=6)
			fr.set(0)
			return fr

		if ft is True:
			o["ft"] = buildMFt(self)
		if inch is True:
			o["in"] = buildMIn(self)
		if fr is True:
			o["fr"] = buildMFr(self)
		base_frame.pack(side = 'top')
		main_frame.pack(fill="x")
		return o

	def buildSep(self, parent):
		ttk.Separator(parent, orient="horizontal").pack(fill="both", pady=12)

	def resetRoofData(self):
		if bool(self.roof_data):
			del self.roof_data
		self.roof_data=[]

	def resetDeckData(self):
		if bool(self.deck_data):
			del self.deck_data
		self.deck_data=[]

	def resetData(self):
		self.resetRoofData()
		self.resetDeckData()

	def addRoofData(self, var):
		row=0 if not bool(self.roof_data) else len(self.roof_data)
		data=tk.StringVar()
		lbl_name=tk.Label(self.roof_data_frame, text=var, font=self.myfont).grid(column=0, row=row)
		lbl_data=tk.Label(self.roof_data_frame, textvariable=data, font=self.myfont).grid(column=1, row=row)
		self.roof_data.append([lbl_name, lbl_data])
		return data

	def addDeckData(self, var):
		col=0 if bool(self.deck_data) else len(self.deck_data)
		data=tk.StringVar()
		lbl_name=tk.Label(self.deck_data_frame, text=var, font=self.myfont).grid(column=col, row=0)
		lbl_data=tk.Label(self.deck_data_frame, textvariable=data, font=self.myfont).grid(column=col, row=1)
		self.deck_data.append([lbl_name, lbl_data])
		return data

	def toInch(self, o):
		ret = (float(o["ft"].get())*12) if bool(o["ft"]) else 0.0
		ret += (float(o["in"].get())) if bool(o["in"]) else 0.0
		ret += (float(fractions.Fraction(o["fr"].get()))) if bool(o["fr"]) else 0.0
		return ret

	def fromInch(self, i):
		string=''
		i_int = int(i)
		string+=str(math.floor(i_int/12))+"' " if math.floor(i_int/12) > 0 else ''
		string+=str(round(i_int % 12))+' '
		string+=str(fractions.Fraction(i-i_int).limit_denominator(16))+' "' if fractions.Fraction(i-i_int).limit_denominator(16) != (0, 1) else ' "'
		return string

	def toDegree(self, pitch):
		return math.degrees(math.atan(pitch/12))

	def supplementary(self, degree):
		return 90 - degree
	
	def getLeg(self, a, b):
		return math.sqrt((a**2)+(b**2))

	def f(self, n):
		self.t.forward(n)
	def b(self, n):
		self.t.backward(n)
			
	def l(self, d):
		self.t.left(d)
	def r(self, d):
		self.t.right(d)
	
	def g(self, x, y):
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

	def north(self):
		self.t.seth(90)
	def south(self):
		self.t.seth(270)
	def east(self):
		self.t.seth(0)
	def west(self):
		self.t.seth(180)

	def drawRect(self, orient, width, length):
		self.east()
		_=self.f(width) if orient=='v' else self.f(length)
		self.south()
		_=self.f(length) if orient=='v' else self.f(width)
		self.west()
		_=self.f(width) if orient=='v' else self.f(length)
		self.north()
		_=self.f(length) if orient=='v' else self.f(width)


	def buildNotebooks(self):
		def mainNotebook(self):
			self.main_notebook=ttk.Notebook(self.root, style='Main.TNotebook')
			self.main_notebook.pack(fill='both')
			self.roof_tab=tk.Frame(self.main_notebook)
			self.roof_tab.pack(pady=6, ipady=6, fill='x')
			self.main_notebook.add(self.roof_tab, text='Roof')
			self.deck_tab=tk.Frame(self.main_notebook)
			self.deck_tab.pack(pady=6, ipady=6, fill='x')
			self.main_notebook.add(self.deck_tab, text='Deck')
   
		def subNotebook(self):
			def subRoofTab(self):
				self.sub_notebook_roof=ttk.Notebook(self.roof_tab, style='Sub.TNotebook')
				self.sub_notebook_roof.pack(fill='both')
				self.roof_input_tab=tk.Frame(self.sub_notebook_roof)
				self.roof_input_tab.pack()
				self.sub_notebook_roof.add(self.roof_input_tab, text='Input')
				self.roof_data_tab=tk.Frame(self.sub_notebook_roof)
				self.roof_data_tab.pack()
				self.sub_notebook_roof.add(self.roof_data_tab, text='Data')
				self.roof_draw_tab=tk.Frame(self.sub_notebook_roof)
				self.roof_draw_tab.pack(fill='both', expand=True)
				self.sub_notebook_roof.add(self.roof_draw_tab, text='Draw')
			def subDeckTab(self):
				self.sub_notebook_deck=ttk.Notebook(self.deck_tab, style='Sub.TNotebook')
				self.sub_notebook_deck.pack(fill='both')
				self.deck_input_tab=tk.Frame(self.sub_notebook_deck)
				self.deck_input_tab.pack()
				self.sub_notebook_deck.add(self.deck_input_tab, text='Input')
				self.deck_data_tab=tk.Frame(self.sub_notebook_deck)
				self.deck_data_tab.pack()
				self.sub_notebook_deck.add(self.deck_data_tab, text='Data')
				self.deck_draw_tab=tk.Frame(self.sub_notebook_deck)
				self.deck_draw_tab.pack()
				self.sub_notebook_deck.add(self.deck_draw_tab, text='Draw')

			subRoofTab(self)
			subDeckTab(self)

		mainNotebook(self)
		subNotebook(self)

#########################################

	def buildRoofTab(self):
		def buildRoofInput(self):
			self.roof_input_frame=tk.Frame(self.roof_input_tab)
			self.roof_input_frame.pack(side='left')
			self.roof_width=self.buildMeasurementInput(self.roof_input_frame, "Width of Building", defFt=8)
			self.buildSep(self.roof_input_frame)
			self.roof_depth=self.buildMeasurementInput(self.roof_input_frame, "Depth of Building", defFt=10)
			self.buildSep(self.roof_input_frame)
			self.roof_ridge=self.buildMeasurementInput(self.roof_input_frame, "Ridge Thickness", ft=False, defIn=1)
			self.buildSep(self.roof_input_frame)
			self.roof_pitch=self.buildMeasurementInput(self.roof_input_frame, 'Roof Pitch [Rise over 12" Run]', defFt=1)
			self.buildSep(self.roof_input_frame)
			self.roof_soffit=self.buildMeasurementInput(self.roof_input_frame, 'Horizontal Soffit [Off Building]', defFt=1)
			self.buildSep(self.roof_input_frame)

			self.roof_go_btn = tk.Button(self.roof_input_frame, text = "GO", command = self.roofClicked)
			self.roof_go_btn.pack()

		def buildRoofData(self):
			self.roof_data_frame=tk.Frame(self.roof_data_tab)
			self.roof_data_frame.pack(fill='both', expand=True)

		def buildRoofDraw(self):
			self.roof_draw_frame=tk.Frame(self.roof_draw_tab)
			self.roof_draw_frame.pack(fill='both', expand=True)
			self.roof_canvas=tk.Canvas(self.roof_draw_frame, width=1.0, height=1.0)
			self.roof_canvas.pack(fill='both', expand=True)
			self.roof_t=RawTurtle(self.roof_canvas)
			self.roof_screen=self.roof_t.getscreen()
			self.cv=self.roof_screen.getcanvas()

			self.roof_screen.reset()
			self.roof_t.reset()
		buildRoofInput(self)
		buildRoofData(self)
		buildRoofDraw(self)

	def roofClicked(self):
		
		self.roof_width_inches=self.toInch(self.roof_width)
		self.roof_depth_inches=self.toInch(self.roof_depth)
		self.roof_ridge_inches=self.toInch(self.roof_ridge)
		self.roof_pitch_inches=self.toInch(self.roof_pitch)
		self.roof_soffit_inches=self.toInch(self.roof_soffit)

		self.run=(self.roof_width_inches/2)-(self.roof_ridge_inches/2)
		self.rise=(self.run/12)*self.roof_pitch_inches
		self.leg=self.getLeg(self.run, self.rise)
		
		self.wall=9*12
		self.axis_ratio=self.root.winfo_screenwidth()/self.root.winfo_screenheight()
		self.cv_width=self.root.winfo_screenwidth()/self.roof_width_inches
		self.cv_height=self.root.winfo_screenheight()/(self.wall+self.rise)
		self.scale=self.cv_width if self.cv_width/self.cv_height >= self.axis_ratio else self.cv_height

		self.roof_data_run=self.addRoofData("Pitch")
		self.roof_data_run.set(str(self.fromInch(self.roof_pitch_inches)))
		self.roof_data_run=self.addRoofData("Degrees")
		self.roof_data_run.set(str(round(self.toDegree(self.roof_pitch_inches), 2)))
		self.roof_data_run=self.addRoofData("Run")
		self.roof_data_run.set(str(self.fromInch(self.run)))
		self.roof_data_rise=self.addRoofData("Rise")
		self.roof_data_rise.set(str(self.fromInch(self.rise)))
		self.roof_data_leg=self.addRoofData("Leg")
		self.roof_data_leg.set(str(self.fromInch(self.leg)))

	def roofDraw(self):
		self.t.x((self.root.winfo_screenwidth/2)-self.toScale(self.roof_ridge_inches))
		self.drawRect(orient='v', width=self.toScale(self.roof_ridge_inches), length=self.toScale(12*12))

	################

	def buildDeckTab(self):
		def buildDeckInput(self):
			self.deck_input_frame=tk.Frame(self.deck_input_tab)
			self.deck_input_frame.pack(side='left')
			self.buildSep(self.deck_input_frame)
			self.deck_width=self.buildMeasurementInput(self.deck_input_frame, "Width of Deck [across building]")
			self.buildSep(self.deck_input_frame)
			self.deck_length=self.buildMeasurementInput(self.deck_input_frame, "Length of Deck [from building]")
			self.buildSep(self.deck_input_frame)
			self.decking=self.buildMeasurementInput(self.deck_input_frame, "Material width:", False, True, True)
			self.buildSep(self.deck_input_frame)
			self.overhang=self.buildMeasurementInput(self.deck_input_frame, "Overhang:", False, True, True)
			self.buildSep(self.deck_input_frame)
			self.gap=self.buildMeasurementInput(self.deck_input_frame, "Gap:", False, False, True)
			self.buildSep(self.deck_input_frame)
		
			self.deck_go_btn = tk.Button(self.deck_input_frame, text = "GO", command = self.deckClicked)
			self.deck_go_btn.pack()

		def buildDeckData(self):
			pass
		
		def buildDeckDraw(self):
			self.deck_draw_frame=tk.Frame(self.deck_draw_tab)
			self.deck_draw_frame.pack(fill='both', expand=True)
			self.deck_canvas=tk.Canvas(self.deck_draw_frame, width=1.0, height=1.0)
			self.deck_canvas.pack(fill='both', expand=True)
			self.t=RawTurtle(self.deck_canvas)
			self.screen=self.t.getscreen()
			self.screen.reset()
			self.t.reset()
		
		buildDeckInput(self)
		buildDeckData(self)
		buildDeckDraw(self)

	def deckClicked(self):
		pass

	################

	def onClick(self, x, y):
		self.x+=8
		self.y-=8
		self.t.goto(self.x, self.y)
		self.t.write(str(self.x)+' '+str(self.y), align='left', font=('Verdana', 6))

f = Framing()
f.screen.onclick(f.onClick)
f.root.mainloop()