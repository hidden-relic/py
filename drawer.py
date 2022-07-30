import turtle as turt

screen = {}

def rgb_to_hex(rgb):
	return '%02x%02x%02x' % rgb
	
def done(x, y):
	screen.reset()
	main()

def gradient(n):
    rgb_codes = []
    step_size = 1024 / n
    for step in range(0, n):
        red = int(max(0, 255 - (step_size*step*0.5))) # step size is half of the step size since both this item goes down and the next one goes up
        blue = int(max(0, 255 - (step_size*0.5*(n-step-1))))
        green = (255 - red) if red else (255 - blue)
        rgb_codes.append("#" + rgb_to_hex((red, green, blue)))
    return rgb_codes
    
def main():
        global screen
        t = turt.Turtle()
        turt.tracer(50, 50)
        info = turt.Turtle()
        screen = t.getscreen()
        info.speed(0)
        info.pu()
        info.ht()
        t.speed(0)
        t.ht()
        steps = int(turt.numinput("iterations", "how many lines?"))
        t.pu()
        t.goto(-steps, steps)
        t.pd()
        angle = int(turt.numinput("angle", "angle to turn after each line"))
        colors = gradient(steps)
        for i in range(0, steps):
                t.color(colors[i])
                for face in range(0, 7):
                        info.clear()
                        info.write("line: " + str(i+1) + "\nface: "+str(face+1)+"\ncolor: " + str(colors[i]))
                        t.forward(steps-i)
                        t.right(angle)
        screen.onclick(done)
        screen.mainloop()
	
main()
