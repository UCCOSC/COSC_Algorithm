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
                
def generate_rest(init_seq, expr, n):
    seq = list(init_seq)
    seq_len = len(init_seq)
    count = 0
    while count < n:
        i = seq_len + count
        x = seq[i-2]
        y = seq[i-1]
        bindings = {'x': x, '+': lambda x, y: x + y,
                    'y': y, '-': lambda x, y: x - y,
                    'i': i, '*': lambda x, y: x * y}
        seq.append(evaluate(expr, bindings))
        count += 1
    return seq[seq_len:]

initial_sequence = [0, 1, 2]
expression = -1 
length_to_generate = 5
print(generate_rest(initial_sequence, 
                                       expression, 
                                       length_to_generate))
initial_sequence = [0, 1, 2]
expression = 'i'
length_to_generate = 0
print(generate_rest(initial_sequence, 
                                       expression, 
                                       length_to_generate))
