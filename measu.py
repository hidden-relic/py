from tkinter import *

def updateFt():
    pass

def updateIn():
    pass

root = Tk()

input_frame = Frame(root, padx=8, pady=8)
input_frame.pack()

input_ft_frame = Frame(input_frame, padx=8, pady=8)
input_in_frame = Frame(input_frame, padx=8, pady=8)
input_fr_frame = Frame(input_frame, padx=8, pady=8)
input_ft_frame.pack()
input_in_frame.pack()
input_fr_frame.pack()

input_ft_label = Label(input_ft_frame, text='Ft')
input_ft_spinbox = Spinbox(input_ft_frame, from_=0, to=100, command=updateFt)
input_in_label = Label(input_in_frame, text='In')
input_in_spinbox = Spinbox(input_in_frame, from_=0, to=11, command=updateIn)
input_ft_label.pack()
input_ft_spinbox.pack()
input_in_label.pack()
input_in_spinbox.pack()
# input_fr_label = Label(input_fr_frame, text='Ft')

root.mainloop()