import matplotlib.pyplot as pyplot
import json

data = json.load(open('C:\\giz\\tests\\graph_data.json', 'r'))
print(data.items())
x = [key for key, value in data.items()]
y = [value for key, value in data.items()]
y.append([value for key, value in info.items()])
print(x, y, sep='\n')
pyplot.grid(True)

## LINE GRAPH ##
pyplot.plot(x, y, color='blue')
pyplot.xlabel('server')
pyplot.ylabel('players')

## BAR GRAPH ##
fig = pyplot.figure()
pyplot.bar(x, y, color='green')
pyplot.xlabel('server')
pyplot.ylabel('players')

pyplot.show()
