class log:
	current_pos_x = 0
	current_pos_y = 0
	step = 0
	
	def __init__(self, t):
		self.logfile = 'C:\giz\log.txt'
		if not file_exists(self.logfile):
			self.file = open(self.logfile, 'x')
		else:
			self.file = open(self.logfile, 'r')
			tst = self.file.readline(0)
			self.file.close()
			self.file = open(self.logfile, 'w')
			self.file.write('')
			self.file.close()
			self.file = open(self.logfile, 'a')
	
		
	def __call__(self, data=''):
		self.step += 1
		x = ''
		y = ''
		arrow = '□'
		self.file.write('(' + str(self.step) + ')\t')
		if self.t.xcor() > self.current_pos_x:
			x = self.t.xcor()-self.current_pos_x
			arrow = '→'
		elif self.t.xcor() < self.current_pos_x:
			x = self.t.xcor()-self.current_pos_x
			arrow = '←'
		elif self.t.ycor() > self.current_pos_y:
			y = self.t.ycor()-self.current_pos_y
			arrow = '↑'
		elif self.t.ycor() < self.current_pos_y:
			y = self.t.ycor()-self.current_pos_y
			arrow = '↓'
		if x:
			self.file.write(str(x) + '\t')
			self.file.write(str(arrow))
		if y:
			self.file.write(str(y) + '\t')
			self.file.write(str(arrow))
		self.file.write('\t[x' + str(self.t.xcor()) + ', y' + str(self.t.ycor()) + ']\n')
		self.file.write('\t>' + str(data) + '\n\n')
			
		self.current_pos_x += self.t.xcor()
		self.current_pos_y += self.t.ycor()