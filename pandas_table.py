import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize

table_MN = pd.read_html('https://lua-api.factorio.com/latest/LuaGuiElement.html')
print(f'Total tables: {len(table_MN)}')
for x in iter(table_MN):
	print(x)