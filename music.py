from re import A
import winsound as ws


class notes():
	def __init__(self):
		self.by_name={'D': [38.89, 77.78, 155.56, 311.12, 622.24, 1244.48, 2488.96, 4977.92, 9955.84, 19911.68], 'D#': [41.2, 82.4, 164.8, 329.6, 659.2, 1318.4, 2636.8, 5273.6, 10547.2, 21094.4], 'E': [43.65, 87.3, 174.6, 349.2, 698.4, 1396.8, 2793.6, 5587.2, 11174.4, 22348.8], 'F': [46.25, 92.5, 185.0, 370.0, 740.0, 1480.0, 2960.0, 5920.0, 11840.0, 23680.0], 'F#': [49.0, 98.0, 196.0, 392.0, 784.0, 1568.0, 3136.0, 6272.0, 12544.0, 25088.0], 'G': [51.91, 103.82, 207.64, 415.28, 830.56, 1661.12, 3322.24, 6644.48, 13288.96, 26577.92], 'G#': [55.0, 110.0, 220.0, 440.0, 880.0, 1760.0, 3520.0, 7040.0, 14080.0, 28160.0], 'A': [58.27, 116.54, 233.08, 466.16, 932.32, 1864.64, 3729.28, 7458.56, 14917.12, 29834.24], 'A#': [61.74, 123.48, 246.96, 493.92, 987.84, 1975.68, 3951.36, 7902.72, 15805.44, 31610.88], 'B': [65.41, 130.82, 261.64, 523.28, 1046.56, 2093.12, 4186.24, 8372.48, 16744.96], 'C': [69.3, 138.6, 277.2, 554.4, 1108.8, 2217.6, 4435.2, 8870.4, 17740.8], 'C#': [73.42, 146.84, 293.68, 587.36, 1174.72, 2349.44, 4698.88, 9397.76, 18795.52]}
		self.hertz=[38.89, 41.2, 43.65, 46.25, 49.0, 51.91, 55.0, 58.27, 61.74, 65.41, 69.3, 73.42, 77.78, 82.4, 87.3, 92.5, 98.0, 103.82, 110.0, 116.54, 123.48, 130.82, 138.6, 146.84, 155.56, 164.8, 174.6, 185.0, 196.0, 207.64, 220.0, 233.08, 246.96, 261.64, 277.2, 293.68, 311.12, 329.6, 349.2, 370.0, 392.0, 415.28, 440.0, 466.16, 493.92, 523.28, 554.4, 587.36, 622.24, 659.2, 698.4, 740.0, 784.0, 830.56, 880.0, 932.32, 987.84, 1046.56, 1108.8, 1174.72, 1244.48, 1318.4, 1396.8, 1480.0, 1568.0, 1661.12, 1760.0, 1864.64, 1975.68, 2093.12, 2217.6, 2349.44, 2488.96, 2636.8, 2793.6, 2960.0, 3136.0, 3322.24, 3520.0, 3729.28, 3951.36, 4186.24, 4435.2, 4698.88, 4977.92, 5273.6, 5587.2, 5920.0, 6272.0, 6644.48, 7040.0, 7458.56, 7902.72, 8372.48, 8870.4, 9397.76, 9955.84, 10547.2, 11174.4, 11840.0, 12544.0, 13288.96, 14080.0, 14917.12, 15805.44, 16744.96, 17740.8, 18795.52, 19911.68, 21094.4, 22348.8, 23680.0, 25088.0, 26577.92, 28160.0, 29834.24, 31610.88] 

class scale(notes):
	def __init__(self):
		super().__init__()
		self.major_steps=[2, 2, 1, 2, 2, 2, 1]
		self.minor_steps=[2, 1, 2, 2, 1, 2, 2]

	def major(self, key, index=3, tempo=500):
		self.scale=[]
		self.root_list=self.by_name[key]
		self.root = self.root_list[index-1]
		self.root_index = self.hertz.index(self.root)
		# self.scale.append(self.root)

		step_indexes=[self.root_index]
		for x in self.major_steps:
			step_indexes.append(step_indexes[len(step_indexes)-1]+x)
		# step_indexes.pop(1)
		for x in step_indexes:
			self.scale.append(self.hertz[x])
		for note in self.scale:
			ws.Beep(int(note), tempo)
		
	def minor(self, key, index=3, tempo=500):
		self.scale=[]
		self.root_list=self.by_name[key]
		self.root = self.root_list[index-1]
		self.root_index = self.hertz.index(self.root)
		self.scale.append(self.root)

		step_indexes=[self.root_index]
		for x in self.minor_steps:
			step_indexes.append(step_indexes[len(step_indexes)-1]+x)
		for x in step_indexes:
			self.scale.append(self.hertz[x])
		for note in self.scale:
			ws.Beep(int(note), tempo)

class chord(scale):
	def __init__(self):
		super().__init__()
		
	def major(self, root, index=3, tempo=500):
		self.chord=[]
		self.root_list=self.by_name[root]
		self.root = self.root_list[index-1]
		self.root_index = self.hertz.index(self.root)
		self.chord.append(self.root)
		
		step_indexes=[self.root_index]
		step_indexes.append(self.major_steps[step_indexes[len(step_indexes)-1]+2])
		step_indexes.append(self.major_steps[step_indexes[len(step_indexes)-1]+2])

		for x in step_indexes:
			self.chord.append(self.hertz[x])
		print(self.chord)
		for note in self.scale:
			ws.Beep(int(self.hertz[note]), tempo)
		
	def minor(self, root, index=3, tempo=500):
		self.chord=[]
		self.root_list=self.by_name[root]
		self.root = self.root_list[index-1]
		self.root_index = self.hertz.index(self.root)
		self.chord.append(self.root)
		
		step_indexes=[self.root_index]
		step_indexes.append(step_indexes[len(step_indexes)-1]+2)
		step_indexes.append(step_indexes[len(step_indexes)-1]+4)
		for x in step_indexes:
			self.chord.append(self.hertz[x])
		print(self.chord)
		for note in self.scale:
			ws.Beep(int(self.hertz[note]), tempo)

class song(notes):
	def __init__(self):
		super().__init__()
		self.beats_per_minute=90
		self.ms_per_minute=1000*60
		self.ms_per_beat=self.ms_per_minute/self.beats_per_minute
		self.subdivisions=[0]

	def __call__(self, notes):
		for i in range(1, 8):
			self.subdivisions.append(self.ms_per_beat*i)
		for note in notes:
			ws.Beep(int(self.by_name[note[0]][int(note[1])]), self.subdivisions[note][2])
	
	def bpm(self, b):
		self.beats_per_minute=b
		self.ms_per_beat=self.ms_per_minute/self.beats_per_minute



tempo=255

# test=song()
# s=[
# 	("E", 3, 1),
# 	("E", 4, 8),
# 	("D", 4, 8),
# 	("B", 4, 6),
# 	("D", 4, 6),
# 	("E", 4, 6),
# 	("G", 4, 6),
# 	("E", 4, 6)
# 	]
# test(s)
test=scale()
for root in iter(test.by_name):
	for i in range(4, 6):
		test.major(root, 4, tempo)
for root in iter(test.by_name):
	for i in range(4, 6):
		test.minor(root, 4, tempo)

# test = chord()
# for root in iter(test.by_name):
# 	test.major(root, 4, tempo)