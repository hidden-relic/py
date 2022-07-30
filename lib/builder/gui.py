#pylint:disable=C0103
#pylint:disable=C0301
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import fractions
import roof

def main():
	root = tk.Tk()
	root.title("Builder")
	root.geometry('350x200')
	
	myfont = ('Verdana', 10)
	
	def checkNum(n):
		if n.isdigit():
			return True
		elif n == '':
			messagebox.showerror('Input', 'Please input a number')
			return False
		else :
			messagebox.showerror('Input', 'Only accepts number values')
			return False
	
	vals = {
	  'ft': [], 'in': []}
	for i in range(0, 500):
		vals['ft'].append(i)
		if i < 12:
			vals['in'].append(i)
	
	nb = ttk.Notebook(root)
	nb.pack(pady = 10, side = 'top')
	tab_roof = tk.Frame(nb, width = 400, height = 280)
	tab_deck = ttk.Frame(nb, width = 400, height = 280)
	tab_roof.pack(fill = 'both', expand = True)
	tab_deck.pack(fill = 'both', expand = True)
	nb.add(tab_roof, text = 'Roof')
	nb.add(tab_deck, text = 'Deck')
	
	# Roof tab
	# - Building width frame
	b_w_frame = tk.Frame(tab_roof)
	# - - label frame
	b_w_lbl_frame = tk.Frame(b_w_frame)
	tk.Label(b_w_lbl_frame, text = "Building width:", font = myfont).pack(side = 'top')
	b_w_lbl_frame.pack(side = 'top')
	# - - measurements frame
	b_w_measurements_frame = tk.Frame(b_w_frame)
	# - - - ft frame
	b_w_ft_frame = tk.Frame(b_w_measurements_frame)
	b_w_ft_frame.grid(column = 0, row = 0, sticky = 'w')
	tk.Label(b_w_ft_frame, text = "ft.", font = myfont).pack(padx = 6, ipadx = 12)
	b_w_ft = ttk.Combobox(b_w_ft_frame, height = 20, width = 6, values = tuple(vals['ft']), font = myfont, state = 'readonly')
	b_w_ft.pack(padx = 6, ipadx = 12)
	# - - - in frame
	b_w_in_frame = tk.Frame(b_w_measurements_frame)
	b_w_in_frame.grid(column = 1, row = 0)
	tk.Label(b_w_in_frame, text = "in.", font = myfont).pack(padx = 6, ipadx = 12)
	b_w_in = ttk.Combobox(b_w_in_frame, height = 20, width = 6, values = tuple(vals['in']), font = myfont, state = 'readonly')
	b_w_in.pack(padx = 6, ipadx = 12)
	# - - a- fraction frame
	b_w_fr_frame = tk.Frame(b_w_measurements_frame)
	b_w_fr_frame.grid(column = 2, row = 0, sticky = 'e')
	tk.Label(b_w_fr_frame, text = "fraction", font = myfont).pack(padx = 6, ipadx = 12)
	b_w_fr = ttk.Combobox(b_w_fr_frame, height = 20, width = 6, values = ("0", "1/16", "1/8", "3/16", "1/4", "5/16", "3/8", "7/16", "1/2", "9/16", "5/8", "11/16", "3/4", "13/16", "7/8", "15/16"), font = myfont, state = 'readonly')
	b_w_fr.pack(padx = 6, ipadx = 12)
	b_w_measurements_frame.pack(side = 'top')
	
	b_w_frame.pack(fill = 'x')
	
	def clicked():
		o = {}
		o['width'] = int(b_w_ft.get())*12+int(b_w_in.get())+float(fractions.Fraction(b_w_fr.get()))
		o['pitch'] = float(pitch_entry.get())
		if o['width'] and o['pitch'] > 0:
			roof.main(o)
	
	other_frame = tk.Frame(tab_roof)
	pitch_lbl = tk.Label(other_frame, text = 'Pitch:', font = myfont)
	pitch_lbl.pack(side = 'left', pady = 12)
	pitch_entry = tk.Entry(other_frame)
	pitch_entry. pack(side = 'right')
	
	other_frame.pack()
	
	reg = root.register(checkNum)
	pitch_entry.config(validate = "key", validatecommand = (reg, '%P'))
	
	data_frame = tk.Frame(tab_roof)
	
	btn = tk.Button(data_frame, text = "Click Me", command = clicked)
	btn.grid(column = 0, row = 0)
	
	lbl_res = tk.Label(data_frame, font = myfont)
	lbl_res.grid(column = 0, row = 1)
	lbl_frac = tk.Label(data_frame, font = myfont)
	lbl_frac.grid(column = 0, row = 2)
	
	data_frame.pack(expand = True)
	
	root.mainloop()
	
main()