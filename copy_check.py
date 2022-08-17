from pathlib import Path
import webbrowser as wb
import json


class compare():
	def __init__(self, root):
		self.out=open('C:\\giz\\file3.json','w').close()
		self.out=Path('C:\\giz\\file3.json').open("a")
		self.root=Path(root)
		self.__main__()

	def __main__(self):
		self.file_list=self.gather_files(self.root)
		# print(self.file_list)
		self.match_list=self.gather_filename_matches(self.file_list)
		# print(self.match_list)
		self.kept_copies=self.gather_copies(self.match_list.l.l.)
		print(self.kept_copies)
		# self.compare()
		# self.open()

	def gather_files(self, dir, recurse_list=[]):
		[recurse_list.append(str(file)) for file in dir.iterdir() if file.is_file()]
		[self.gather_files(folder, recurse_list) for folder in dir.iterdir() if folder.is_dir()]
		return recurse_list

	def gather_filename_matches(self, file_list):
		matches=[]
		while len(file_list) > 0:
			print("len", len(file_list))
			check_against=Path(file_list.pop(0))
			# print("checking", str(check_against))
			for item in iter(file_list):
				item=Path(item)
				# print("item", str(item))
				# print("parts", item.parts[-2]+item.name)
				if item.parts[-2]+"/"+item.name == check_against.parts[-2]+"/"+check_against.name:
					matches.append((str(check_against), str(item)))
		return matches

	def gather_copies(self, file_list):
		matches=[]
		while len(file_list > 0):
			print("copies len", len(file_list))
			file=file_list.pop(0)
			with Path(file[0]) as check_against:
				with Path(file[1]) as item:
					if check_against.open().read_text() == item.open().read_text():
						if "github" in check_against.parts:
							del item
							matches.append(str(check_against))
						elif "github" in item.parts:
							del check_against
							matches.append(str(item))
		return matches


 

	def gather_matches(self, matches=[]):
			
		return matches

	def compare(self):
		for match in iter(self.matches):
			with self.root.open(match[0],'r') as f:
				a=Path.resolve(f)
				c=set(f.readlines())
			with self.root.open(match[1],'r') as f:
				b=Path.resolve(f)
				d=set(f.readlines())
			self.out.write(str(a)+" :: "+str(b))
			
			for line in list(c-d):
				self.out.write(line)

	def open(self):
		import subprocess
		subprocess.call("notepad.exe", self.out)

def info(dir):
	l=[]
	for item in dir.iterdir():
		if item.is_file():
			print(item)

test = compare("C:\\giz\\")
# print(str(info(p)))