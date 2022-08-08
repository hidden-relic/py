import asyncio
import json
import tkinter as tk
from tkinter import ttk
import pathlib

from aiohttp import ClientSession


async def main():
    url = 'https://lua-api.factorio.com/latest/runtime-api.json'
    async with ClientSession() as session:
        async with session.get(url) as response:
            html_body = await response.read()
            return html_body

html_data = asyncio.run(main())
OUTPUT_DIR = pathlib.Path().resolve() / "pyfiles"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_FILE = OUTPUT_DIR / "api.json"
print()
OUTPUT_FILE.write_text(html_data.decode())
o=dict(json.load(open('C:\\giz\\github\\py\\lib\\builder\\pyfiles\\all.json', 'r')))
root = tk.Tk()

count = 0
layer=[]
def buildNotebooks(parent, o, count):
	layer.append(ttk.Notebook(parent))
	for a in o:
		for b in a:
			for c in b:
				for d in c:
					for e in d:
		# =ttk.Notebook(root, style='Main.TNotebook')
		# main_notebook.pack(fill='both')
						print(type(a), a, ', ', type(b), b, ', ', type(c), c, ', ', type(d), d, ', ', type(e), e)

buildNotebooks(root, o, count)
	