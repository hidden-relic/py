import asyncio
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
OUTPUT_FILE = OUTPUT_DIR / "all.html"
print()
OUTPUT_FILE.write_text(html_data.decode())
