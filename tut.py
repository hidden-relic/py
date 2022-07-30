import turtle
# loads turtle module into this script
turt = turtle.Turtle()
# gets a new turtle drawer thing
# turt is our turtle's name
# turtle.Turtle() just means: 
# in module 'turtle', we want the Turtle() method
# (methods are like commands)
turt.speed(0)
# makegofast
i = 0
# start i out at 0
while i < 500:		# ------- start of loop --------
	turt.forward(i)  # draw a line whose length
			# is the current value of i
	turt.right(91)	 # turn right 91 degrees, so we
	 		# never fully make a square
	i += 5	  	# set i to itself plus whatever
		 	   # (5 here) for next iteration
			 # ------- end of loop --------
turtle.mainloop()
# this just keeps the script running
# when its finished instead of closing
