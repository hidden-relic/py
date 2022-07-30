import tkinter as tk
from turtle import RawTurtle, TurtleScreen
from time import sleep
import tkcap

class App:
    def __init__(self, master, width, height):
        self.master = master
        self.cap=tkcap.CAP(self.master)
        self.canvas = tk.Canvas(self.master)
        self.canvas.config(width=(width*0.8)*0.8, height=(height*0.8)*0.8)
        self.canvas.pack(side=tk.LEFT)
        self.screen = TurtleScreen(self.canvas)
        self.screen.bgcolor("black")
        # self.button = tk.Button(self.master, text="Press me", command=self.press)
        # self.button.pack()
        self.turt = RawTurtle(self.screen, shape="turtle")
        self.turt.color("cyan")
        self.turt.speed(0)
        self.turt.color("cyan")
        
    def star(self, size):
        if size <= 10:
            return
        else:
            self.turt.write(self.turt.pos())
            for i in range(8):
                sleep(1)
                self.turt.forward(size)
                self.star(size/3)
                self.turt.left(45)
    def do_stuff(self):
        for i in range(0, 1000, 100):
            print(i)
            self.turt.penup()
            self.turt.sety(self.turt.ycor()-200)
            self.turt.pendown()
            self.star(i)
            # sleep(1)
            self.cap.capture('C:\giz\SS'+str(i)+'.jpg')
            self.turt.reset()


if __name__ == '__main__':
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.title("Raw Turtle")
    winfo_width=root.winfo_width()
    winfo_height=root.winfo_height()
    print(winfo_width)
    print(winfo_height)
    app = App(root, winfo_width, winfo_height)
    app.do_stuff()
    root.mainloop()
