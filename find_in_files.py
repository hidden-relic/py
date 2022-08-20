from pathlib import Path

class search:
	def __init__(self, root=None, query=None):
		self.root=root or 'C:\\'
		self.query=bytes(query, 'utf-8')
		self.dive(self.root, self.query)

	def dive(self, path, query):
		this_path=Path(path)
		for x in Path.iterdir(this_path):
			if x.is_file():
				f=Path.open(x, 'rb')
				if query in f.readlines():
					return str(f)
			else:
				self.dive(str(x), query)
		return None

new=search('C:\\giz\\', 'ratio')