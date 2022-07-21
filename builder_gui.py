#pylint:disable=C0301
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Roof Helper")
window.geometry('350x200')

myfont = ('Verdana', 10)

vals={'ft': [], 'in': []}
for i in range(0, 500):
	vals['ft'].append(i)
	if i < 12:
		vals['in'].append(i)

#Building width frame
b_w_frame = tk.Frame(window)
# -- label frame
b_w_lbl_frame = tk.Frame(b_w_frame)
tk.Label(b_w_lbl_frame, text="Building width:", font=myfont).pack(side='top')
b_w_lbl_frame.pack(side='top')
# -- measurements frame
b_w_measurements_frame = tk.Frame(b_w_frame)
# -- -- ft frame
b_w_ft_frame = tk.Frame(b_w_measurements_frame).grid(column=0, row=0)
tk.Label(b_w_ft_frame, text="ft.", font=myfont).pack(side='top', padx=6, ipadx=12)
b_w_ft = ttk.Combobox(b_w_ft_frame, height=20, width=6, values=tuple(vals['ft']), font=myfont, state='readonly').pack(side='bottom', padx=6, ipadx=12)
# -- -- in frame
b_w_in_frame = tk.Frame(b_w_measurements_frame).grid(column=1, row=0)
tk.Label(b_w_in_frame, text="in.", font=myfont).pack(side='top', padx=6, ipadx=12)
b_w_in = ttk.Combobox(b_w_in_frame, height=20, width=6, values=tuple(vals['in']), font=myfont, state='readonly').pack(side='bottom', padx=6, ipadx=12)
# -- -- fraction frame
b_w_fr_frame = tk.Frame(b_w_measurements_frame).grid(column=2, row=0)
tk.Label(b_w_fr_frame, text="fraction", font=myfont).pack(side='top', padx=6, ipadx=12)
b_w_fr = ttk.Combobox(b_w_fr_frame, height=20, width=6, values=("0", "1/16", "1/8", "3/16", "1/4", "5/16", "3/8", "7/16", "1/2", "9/16", "5/8", "11/16", "3/4", "13/16", "7/8", "15/16"), font=myfont, state='readonly').pack(side='bottom', padx=6, ipadx=12)
b_w_measurements_frame.pack(fill='x')
b_w_frame.pack(expand=True, fill='x')

def clicked():
    res = float(int(b_w_ft.get())*12+int(b_w_in.get())+float(frac))
    lbl_res.configure(text= res)
    
data_frame = tk.Frame(window)

btn = tk.Button(data_frame, text="Click Me", command=clicked)
btn.grid(column=0, row=0)

lbl_res = tk.Label(data_frame, font=myfont)
lbl_res.grid(column=0, row=1)
lbl_frac = tk.Label(data_frame, font=myfont)
lbl_frac.grid(column=0, row=2)

data_frame.pack(expand=True)

window.mainloop()