import tkinter as tk


class deck_gui:

    root = tk.Tk()

    def __init__(self):
        self.w_ft=0
        self.w_in=0
        self.w_fr=0
        self.input_frame=tk.Frame(self.root).pack(expand=True)
        self.w_frame=tk.Frame(self.input_frame).pack(fill='x')
        self.ft_label=tk.Label(self.w_frame, text=str(self.w_ft)).pack(side='left')
        self.ft_btn_frame=tk.Frame(self.w_frame).pack(side='left')
        self.plus_btn=tk.Button(self.ft_btn_frame, text='+', command=self.incFt).pack()
        self.minus_btn=tk.Button(self.ft_btn_frame, text='-', command=self.decFt).pack()
        self.in_label=tk.Label(self.w_frame, text=str(self.w_in)).pack(side='left')
        self.in_btn_frame=tk.Frame(self.w_frame).pack(side='left')
        self.plus_btn=tk.Button(self.in_btn_frame, text='+', command=self.incIn).pack()
        self.minus_btn=tk.Button(self.in_btn_frame, text='+', command=self.decIn).pack()
        self.fr_label=tk.Label(self.root, text=str(self.w_fr)).pack(side='left')
        self.fr_btn_frame=tk.Frame(self.w_frame).pack(side='left')
        self.plus_btn=tk.Button(self.fr_btn_frame, text='+', command=self.incFr).pack()
        self.minus_btn=tk.Button(self.fr_btn_frame, text='+', command=self.decFr).pack()
        
    def incFt(self):
        self.w_ft+=1
        self.ft_label.set(str(self.w_ft))
    def decFt(self):
        self.w_ft-=1
        self.ft_label.set(str(self.w_ft))
    
    def incIn(self):
        self.w_in+=1
        self.in_label.set(str(self.w_in))
    def decIn(self):
        self.w_in-=1
        self.in_label.set(str(self.w_in))
    
    def incFr(self):
        self.w_fr+=1
        self.fr_label.set(str(self.w_fr))
    def decFr(self):
        self.w_fr-=1
        self.ft_label.set(str(self.w_fr))


t = deck_gui()

t.root.mainloop()