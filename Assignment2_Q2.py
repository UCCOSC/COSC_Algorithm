def evaluate(expression, bindings):
	b = bindings
	if isinstance(expression, int):
		return expression
	if isinstance(expression, str):
		for i in expression:
			if i in bindings.keys():
				return bindings[i]
	if isinstance(expression, list):
		if len(expression) == 3:
			if expression[0] in bindings.keys():
				return (bindings[expression[0]](evaluate(expression[1],b), evaluate(expression[2],b)))
						
bindings = {}
expression = 12
print(evaluate(expression, bindings))

bindings = {'x':5, 'y':10, 'time':15}
expression = 'y'
print(evaluate(expression, bindings))

bindings = {'x': 5, 'y': 10, 'time': 15, 'add': lambda x, y: x + y}
expression = ['add', 12, 'x']
print(evaluate(expression, bindings))

import operator
bindings = dict(x = 5, y = 10, blah = 15, add = operator.add)
expression = ['add', ['add', 22, 'y'], 'x']
print(evaluate(expression, bindings))
