import turtle
turtle.tracer(10, 0)
class draw:
    """base drawing class"""
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.hideturtle()
        self.s = self.t.getscreen()
        self.s.setup(0.8, 0.8)
        self.drawing_area = {'left': -((self.s.window_width*0.9)/2), 'right': ((self.s.window_width*0.9)/2), 'top': ((self.s.window_height*0.9)/2), 'bottom': ((self.s.window_height*0.9)/2)}
    
    def 
