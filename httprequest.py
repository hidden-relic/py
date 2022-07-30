import requests

x = requests.get('https://www.homedepot.com/b/Lumber-Composites-Dimensional-Lumber-Framing-Lumber/2x12/N-5yc1vZc55wZ1z0ywx6')

print(x.text)