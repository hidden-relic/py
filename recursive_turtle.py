import turtle
import math
t=turtle.Turtle()

t.speed(0)
i=500

def recurse(length):
	if length > 0:
		for _ in range(27):
			t.forward(length)
			t.left(165)
		t.forward(length)
		t.left(165)
		length=(length//3)*2
		t.forward(length)
		recurse(length)

recurse(i)