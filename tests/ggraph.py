import matplotlib.pyplot as pyplot
import json

data = json.load(open('/storage/emulated/0/Documents/tests/graph_data.json', 'r'))
x = [key for key, value in data.items()]
y = [value for key, value in data.items()]
pyplot.grid(True)

## LINE GRAPH ##
pyplot.plot(x, y, color='blue', marker='o')
pyplot.xlabel('server')
pyplot.ylabel('players')

## BAR GRAPH ##
fig = pyplot.figure()
pyplot.bar(x,y, color='green')
pyplot.xlabel('server')
pyplot.ylabel('players')

pyplot.show()