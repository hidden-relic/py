#pylint:disable=W0602
#pylint:disable=C0116
#pylint:disable=C0103
#pylint:disable=E0001
import turtle as t
import math

outline = {}
trim = {}
data = {}

def toDegrees(pitch = 0):
  global data
  data["degrees"] = math.degrees(math.atan(data["pitch"]/12))
  if pitch != 0:
    return math.degrees(math.atan(pitch/12))
  return data["degrees"],

def revDegrees(degree):
  return 90 - degree

def done(x, y):
  outline.reset()
  trim.reset()
  main()
  
def main():
  global outline
  global trim
  global data
  data = {
    "pitch": t.numinput("Pitch", "Roof Pitch"),
    "run": 300,
    "trim_run": 275
  }
  data["run_steps"] = data["run"] / 12
  data["trim_run_steps"] = data["trim_run"] / 12
  data["rise"] = data["run_steps"] * data["pitch"]
  data["trim_rise"] = data["trim_run_steps"] * data["pitch"]
  data["leg"] = math.sqrt((data["run"] ** 2) + (data["rise"] ** 2))
  data["trim_leg"] = math.sqrt((data["trim_run"] ** 2) + (data["trim_rise"] ** 2))
  
  screen = t.Screen()
  outline = t.Turtle()
  trim = t.Turtle()
  outline.speed = 0
  trim.speed = 0
  outline.color("green")
  trim.color("green")
  outline.penup()
  trim.penup()
  outline.goto(outline.xcor(), (outline.ycor() + 300))
  trim.goto(trim.xcor(), (trim.ycor() + 300))
  outline.backward(300)
  trim.backward(275)
  outline.left(toDegrees(data["pitch"]))
  trim.left(toDegrees(data["pitch"]))
  outline.pendown()
  trim.pendown()
  outline.forward(data["leg"])
  data["peak"] = {"x": outline.xcor(), "y": outline.ycor()}
  outline.write(str(data["pitch"]) + " pitch / " + str(round(toDegrees(data["pitch"]), 2)) + "°")
  trim.forward(data["trim_leg"])
  outline.right((toDegrees(data["pitch"]) * 2))
  trim.right((toDegrees(data["pitch"]) * 2))
  outline.forward(data["leg"])
  trim.forward(data["trim_leg"])
  outline.right(90 + revDegrees(toDegrees(data["pitch"])))
  outline.color("black")
  outline.forward(data["run"] * 2)
  outline.left(90)
  outline.forward(300)
  outline_screen = outline.getscreen()
  outline.write(outline_screen.screensize())
  outline.left(90)
  outline.forward(600)
  outline.left(90)
  outline.forward(300)
  screen.onclick(done)
  screen.mainloop()
  #done()
  
main()