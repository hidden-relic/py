import asyncio
import pathlib
import h

from aiohttp import ClientSession

/html/body/div[2]/div/div/div[2]/div[1]/div[2]/ul
async def main():
    url = 'https://docs.python.org/3/library/tk.htmlrc'
    async with ClientSession() as session:
        async with session.get(url) as response:
            html_body = await response.read()
            return html_body

html_data = asyncio.run(main())
OUTPUT_DIR = pathlib.Path().resolve() / "pydocs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=False)
OUTPUT_FILE = OUTPUT_DIR / "all.html"
OUTPUT_FILE.write_text(html_data.decode())
