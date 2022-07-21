import tkinter as tki
import math
import fractions

def doIt():
  width_in_inches = (width_of_building_ft_spinbox.get() * 12) + width_of_building_in_spinbox.get()
  for i in width_of_building_frac_listbox.curselection():
    if width_of_building_frac_listbox.get(i) and width_of_building_frac_listbox.get(i) != "---":
      width_in_inches += fractions.Fraction(width_of_building_frac_listbox.get(i))
  result.config(text = str(width_in_inches))
  return width_in_inches

root = tki.Tk()
width_of_building_label = tki.Label(root, text = "Width of building:")
width_of_building_label.pack()

mainframe = tki.Frame(root)
mainframe.pack()

result_label = tki.Label(root, text = "Width of building in inches:")
result_label.pack(side = 'bottom')

result = tki.Label(root)
result.pack(side = 'bottom')

inch_fractions = ["---", "1/16", "1/8", "3/16", "1/4", "5/16", "3/8", "7/16", "1/2", " 9/16", "5/8", "11/16", "3/4", "13/16", "7/8", "15/16"]
count = 0

width_of_building_ft_spinbox = tki.Spinbox(mainframe, from_=0, to=100, wrap=True)
width_of_building_ft_spinbox.pack(side = 'left')

width_of_building_in_spinbox = tki.Spinbox(mainframe, from_=0, to=11, wrap=True)
width_of_building_in_spinbox.pack(side = 'top')

width_of_building_frac_listbox = tki.Listbox(mainframe, height = 1)
width_of_building_frac_listbox.pack(side = 'right')

for v in inch_fractions:
	count += 1
	width_of_building_frac_listbox.insert(count, v)
	
do_it_button = tki.Button(root, text = "Do it", command = doIt())
do_it_button.pack(side = "bottom")
root.mainloop()