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
		self.infofont = ("Verdana", 6)
		self.root = tk.Tk()
		# self.root.geometry(str(self.root.winfo_screenwidth())+'x'+str(self.root.winfo_screenheight())+'+0+0')
		self.vals = {"ft": [], "in": []}
		for i in range(0, 500):
			self.vals["ft"].append(i)
			if i < 12:
				self.vals["in"].append(i)
		self.myStyle=ttk.Style()
		self.myStyle.theme_use('clam')
		self.myStyle.configure('Main.TNotebook', font=self.myfont)
		self.myStyle.configure('Sub.TNotebook', font=self.myfont)
		self.myStyle.configure('Main.TNotebook.Tab', padding=[16, 4], font=self.myfont)
		self.myStyle.configure('Sub.TNotebook.Tab', padding=[16, 4], font=self.myfont)
		# self.myStyle.configure('TNotebook', tabposition='wn')
		self.roof_data=[]
		self.deck_data=[]
		self.resetData()

		self.buildNotebooks()
		self.buildRoofTab()
		self.buildDeckTab()

	def buildMeasurementInput(self, parent, text, ft=True, inch=True, fr=True, defFt=0, defIn=0):
		o = {"ft": False, "in": False, "fr": False}
		base_frame=tk.Frame(parent)
		base_frame.pack()
		lbl_frame=tk.Frame(base_frame)
		tk.Label(lbl_frame, text=text, font=self.myfont).pack(side='top', padx=6)
		lbl_frame.pack(side='top')
		main_frame = tk.Frame(base_frame)

		def buildMFt(self):
			ft_frame = tk.Frame(main_frame)
			ft_frame.grid(column=0, row=0, sticky="w")

			tk.Label(ft_frame, text="ft.", font=self.infofont, fg='#0088ff').pack(padx=6)
			ft = ttk.Combobox(ft_frame, height=20, width=6, values=tuple(self.vals["ft"]), font=self.myfont, state="readonly")
			ft.pack(padx=6)
			ft.set(defFt)
			return ft

		def buildMIn(self):
			in_frame = tk.Frame(main_frame)
			in_frame.grid(column=1, row=0)

			tk.Label(in_frame, text="in.", font=self.infofont, fg='#0088ff').pack(padx=6)
			inch = ttk.Combobox(in_frame, height=20, width=6, values=tuple(self.vals["in"]), font=self.myfont, state="readonly")
			inch.pack(padx=6)
			inch.set(defIn)
			return inch

		def buildMFr(self):
			fr_frame = tk.Frame(main_frame)
			fr_frame.grid(column=2, row=0, sticky="e")

			tk.Label(fr_frame, text=bytes.fromhex("BE"), font=self.infofont, fg='#0088ff').pack(padx=6)
			fr = ttk.Combobox(fr_frame, height=20, width=6, values=("0", "1/16", "1/8", "3/16", "1/4", "5/16", "3/8", "7/16", "1/2", "9/16", "5/8", "11/16", "3/4", "13/16", "7/8", "15/16"), font=self.myfont, state="readonly")
			fr.pack(padx=6)
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

	def buildNotebooks(self):
		def mainNotebook(self):
			self.main_notebook=ttk.Notebook(self.root, style='Main.TNotebook')
			self.main_notebook.pack(anchor='center', fill='x', expand=True)
			self.roof_tab=tk.Frame(self.main_notebook)
			self.roof_tab.pack(anchor='center', expand=True, fill='x')
			self.main_notebook.add(self.roof_tab, text='Roof')
			self.deck_tab=tk.Frame(self.main_notebook)
			self.deck_tab.pack(anchor='center', fill='x', expand=True)
			self.main_notebook.add(self.deck_tab, text='Deck')
   
		def subNotebook(self):
			def subRoofTab(self):
				self.sub_notebook_roof=ttk.Notebook(self.roof_tab, style='Sub.TNotebook')
				self.sub_notebook_roof.pack(anchor='n', fill='x', expand=True)
				self.roof_input_tab=tk.Frame(self.sub_notebook_roof)
				self.roof_input_tab.pack(anchor='center', fill='x')
				self.sub_notebook_roof.add(self.roof_input_tab, text='Input')
				self.roof_data_tab=tk.Frame(self.sub_notebook_roof)
				self.roof_data_tab.pack(anchor='center', fill='x')
				self.sub_notebook_roof.add(self.roof_data_tab, text='Data')
				self.roof_draw_tab=tk.Frame(self.sub_notebook_roof)
				self.roof_draw_tab.pack(anchor='center', fill='x', expand=True)
				self.sub_notebook_roof.add(self.roof_draw_tab, text='Draw')
			def subDeckTab(self):
				self.sub_notebook_deck=ttk.Notebook(self.deck_tab, style='Sub.TNotebook')
				self.sub_notebook_deck.pack(anchor='center', fill='x')
				self.deck_input_tab=tk.Frame(self.sub_notebook_deck)
				self.deck_input_tab.pack(anchor='center')
				self.sub_notebook_deck.add(self.deck_input_tab, text='Input')
				self.deck_data_tab=tk.Frame(self.sub_notebook_deck)
				self.deck_data_tab.pack(anchor='center')
				self.sub_notebook_deck.add(self.deck_data_tab, text='Data')
				self.deck_draw_tab=tk.Frame(self.sub_notebook_deck)
				self.deck_draw_tab.pack(anchor='center')
				self.sub_notebook_deck.add(self.deck_draw_tab, text='Draw')

			subRoofTab(self)
			subDeckTab(self)

		mainNotebook(self)
		subNotebook(self)

#########################################

	def buildRoofTab(self):
		def buildRoofInput(self):
			self.roof_input_frame=tk.Frame(self.roof_input_tab)
			self.roof_input_frame.pack(side='top', fill='both', expand=True)
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

			self.roof_go_btn = tk.Button(self.roof_input_frame, text = "GO", command = self.goRoof)
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

	def goRoof(self):
		
		self.roof_data_obj={
			't': self.roof_t,
			'cv': self.roof_screen.getcanvas(),
			'roof_width_inches': self.roof_width,
			'roof_depth_inches': self.roof_depth,
			'roof_ridge_inches': self.roof_ridge,
			'roof_pitch_inches': self.roof_pitch,
			'roof_soffit_inches': self.roof_soffit,
			'wall': 9*12
		}

		self.roof=roof(self.roof_data_obj)

		self.roof_data_pitch=self.addRoofData("Pitch")
		self.roof_data_pitch.set(str(self.fromInch(self.roof.roof_pitch_inches)))
		self.roof_data_degrees=self.addRoofData("Degrees")
		self.roof_data_degrees.set(str(round(self.toDegree(self.roof.roof_pitch_inches), 2)))
		self.roof_data_run=self.addRoofData("Run")
		self.roof_data_run.set(str(self.fromInch(self.roof.run)))
		self.roof_data_rise=self.addRoofData("Rise")
		self.roof_data_rise.set(str(self.fromInch(self.roof.rise)))
		self.roof_data_leg=self.addRoofData("Leg")
		self.roof_data_leg.set(str(self.fromInch(self.roof.hyp)))

	################

	def buildDeckTab(self):
		def buildDeckInput(self):
			self.deck_input_frame=tk.Frame(self.deck_input_tab)
			self.deck_input_frame.pack(side='top', fill='both', expand=True)
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

class hatch:
	def __init__(self, t):
		self.t=t

	def f(self, n):
		self.t.forward(self.fix(n))
	def b(self, n):
		self.t.backward(self.fix(n))
			
	def l(self, d):
		self.t.left(d)
	def r(self,  d):
		self.t.right(d)

	def u(self):
		self.t.penup()
	def d(self):
		self.t.pendown()
	
	def g(self, x, y):
		self.u()
		self.t.goto(self.fix(x), self.fix(y))
		self.d()
	
	def x(self, n):
		self.g(self.unfix(self.t.xcor())+n, self.unfix(self.t.ycor()))
	def y(self, n):
		self.g(self.unfix(self.t.xcor()), self.unfix(self.t.ycor())+n)

	def north(self):
		self.t.seth(90)
	def south(self):
		self.t.seth(270)
	def east(self):
		self.t.seth(0)
	def west(self):
		self.t.seth(180)

	def drawRect(self, x, y):
		self.east()
		self.f(self.fix(x))
		self.south()
		self.f(self.fix(y))
		self.west()
		self.f(self.fix(x))
		self.north()
		self.f(self.fix(y))


class roof(hatch):
	def __init__(self, obj):
		super().__init__(obj['t'])
		self.roof_width_inches=self.toInch(obj['roof_width_inches'])
		self.roof_depth_inches=self.toInch(obj['roof_depth_inches'])
		self.roof_ridge_inches=self.toInch(obj['roof_ridge_inches'])
		self.roof_pitch_inches=self.toInch(obj['roof_pitch_inches'])
		self.roof_soffit_inches=self.toInch(obj['roof_soffit_inches'])
		self.wall=obj['wall']
		self.run=(self.roof_width_inches/2)-(self.roof_ridge_inches/2)
		self.rise=(self.run/12)*self.roof_pitch_inches
		self.hyp=self.hypotenuse(self.run, self.rise)
		self.roof_width_total=self.roof_width_inches+(self.roof_soffit_inches*2)
		self.roof_height_total=self.rise+self.wall
		self.cv=obj['cv']
		self.axis_ratio=self.cv.winfo_width()/self.cv.winfo_height()
		self.cv_width=self.cv.winfo_width()/self.roof_width_total
		self.cv_height=self.cv.winfo_height()/self.roof_height_total
		self.scale=self.cv_width if self.cv_width/self.cv_height >= self.axis_ratio else self.cv_height

		self.__main__()

	def __main__(self):
		self.drawWalls()
		self.drawRidge()
		self.drawRafterLeft()

	def toDegree(self, pitch):
		return math.degrees(math.atan(pitch/12))
	
	def supplementary(self, degree):
		return 90 - degree
	
	def hypotenuse(self, a, b):
		return math.sqrt((a**2)+(b**2))

	def applyScale(self, n):
		return n*self.scale
	def unapplyScale(self, n):
		return n/self.scale
	def fix(self, x, y=False):
		if y==False:
			return self.applyScale(x)
		else:
			return self.applyScale(x), self.applyScale(y)
	def unfix(self, x, y=False):
		if y==False:
			return self.unapplyScale(x)
		else:
			return self.unapplyScale(x), self.unapplyScale(y)

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

	def drawWalls(self):
		self.g(self.roof_soffit_inches, -self.rise)
		self.drawWall()
		self.x(self.roof_width_inches-5.5)
		self.drawWall()

	def drawWall(self):
		self.t.color('#88FF88')
		self.drawRect(5.5, 1.5)
		self.y(-1.5)
		self.drawRect(5.5, 1.5)
		self.y(-1.5)
		self.drawRect(5.5, self.wall-4.5)
		self.y(-(self.wall-4.5))
		self.drawRect(5.5, 1.5)
		self.y(self.wall-1.5)

	def drawRidge(self):
		self.g((self.roof_width_total/2)-(self.roof_ridge_inches/2), 0)
		self.drawRect(self.roof_ridge_inches, 12)

	def drawRafterLeft(self):
		self.west()
		self.l(self.toDegree(self.roof_pitch_inches))
		self.f(self.hyp+self.roof_soffit_inches)
		self.l(self.supplementary(self.toDegree(self.roof_pitch_inches)))
		self.f(math.sqrt((7.5**2)/2))

f = Framing()
f.screen.onclick(f.onClick)
f.root.mainloop()