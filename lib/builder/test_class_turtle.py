import turtle as t
import math

t.tracer(8, 0)

class Circle(t.Turtle):
	def __init__(self):
		super().__init__()
		self.speed(0)

	def rgb_to_hex(self, rgb):
		return '%02x%02x%02x' % rgb

	def gradient(self, n):
		rgb_codes = []
		step_size = 1024 / n
		for step in range(0, n):
			red = int(max(0, 255 - (step_size*step*0.5))) # step size is half of the step size since both this item goes down and the next one goes up
			blue = int(max(0, 255 - (step_size*0.5*(n-step-1))))
			green = (255 - red) if red else (255 - blue)
			rgb_codes.append("#" + self.rgb_to_hex((red, green, blue)))
		return rgb_codes

	def getCircle(self, radius):
		radius_sq=radius**2
		edge = radius*math.pi
		center = self.position()
		area = {"top_left": {"x": int(center[0]-radius), "y": int(center[1]-radius)}, "bottom_right": {"x": int(center[0]+radius), "y": int(center[1]+radius)}}
		self.pu()
		colors=self.gradient(radius*4)

		for i in range(area["top_left"]["x"], area["bottom_right"]["x"]):
			self.color(colors[i])
			for j in range(area["top_left"]["y"], area["bottom_right"]["y"]):
				distance = math.floor((center[0] - i) ** 2 + (center[1] - j) ** 2)
				if (distance < radius_sq):
					self.pd()
					self.goto(i, j)


test=Circle()
test.getCircle(100)
test.mainloop()