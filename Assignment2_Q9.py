import random
import copy
#Q1
def is_valid_expression(expression, function_symbols, terminal_symbols):
    f = function_symbols
    t = terminal_symbols
    
    if isinstance(expression, list):
        if len(expression) == 3:
            if expression[0] in function_symbols:
                if is_valid_expression(expression[1],f,t):
                    if is_valid_expression(expression[2],f,t):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    if isinstance(expression, str):
        for i in expression:
            if i in terminal_symbols:
                return True
            else:
                return False
    else:
        return isinstance(expression, int)
#Q2
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
#Q3
def depth(expression):
    if isinstance(expression, list):
        result1 = 1 + depth(expression[1])
        result2 = 1 + depth(expression[2])
        if result1 >= result2:
            return result1
        else:
            return result2
    else:
        return 0
#Q4
def make_random_expression(function_symbols, terminals, max_depth):
    random_function = random.choice(function_symbols)
 
    if max_depth == 1: probRecursion = 0
    else: probRecursion = 0.5
 
    result = [random_function]
    for i in range(2):
        if random.random() < probRecursion:
            element = make_random_expression(function_symbols, terminals, max_depth-1)
        else:
            element = random.choice(terminals)
        result.append(element)
    return result
#Q5
def mutation_points(expression, depth_limit, pos = 0):
   
    current_depth = depth_limit
 
    pos_depth_list = [(pos, current_depth)]
    if isinstance(expression,list):
        element1 = mutation_points(expression[1], current_depth-1, pos+1)
        offset = len(element1)+1
        element2 = mutation_points(expression[2], current_depth-1, pos+offset)
        pos_depth_list.extend(element1)
        pos_depth_list.extend(element2)
    return pos_depth_list
#Q6
def valid_crossover_points(parent1, parent2, depth_limit, var_p1 = 0, var_p2 = 0):
	current_depth = depth_limit
	if isinstance(parent1,list):
		valid_crossover_points(parent1[1], parent2, current_depth-1,var_p1+1)
		valid_crossover_points(parent1[2], parent2, current_depth-1,var_p1+1)
		
	if isinstance(parent2,list):
		valid_crossover_points(parent1, parent2[1], current_depth-1,var_p1, var_p2+1)
	return ((var_p1, var_p2),)
#Q7
def lenTree(expr, count=1):
    if isinstance(expr, list):
        count += lenTree(expr[1], count) + lenTree(expr[2], count)
    else: count = 1
    return count
 
def getSubtree(expr, pos, curr_pos=0):
    ''' Support function that returns the subtree at a
       given point. '''
    subtree = None
    if curr_pos == pos: subtree = expr
    elif isinstance(expr, list):
        e1 = getSubtree(expr[1], pos, curr_pos+1)
        if e1 != None: subtree = e1
        else:
            e2 = getSubtree(expr[2], pos, curr_pos+1+lenTree(expr[1]))
            if e2 != None: subtree = e2
    return subtree
 
 
def replaceChild(expr, pos, newChild, curr_pos=0):
    ''' Replaces a node at a certain point with the given newChild '''
    if curr_pos == pos:
        expr = newChild
    elif isinstance(expr, list):
        expr[1] = replaceChild(expr[1], pos, newChild, curr_pos+1)
        expr[2] = replaceChild(expr[2], pos, newChild, curr_pos+1+lenTree(expr[1]))
    return expr
       
 
def crossover(parent1, parent2, point1, point2):
    clone = parent1 if not isinstance(parent1, list) else copy.deepcopy(parent1)
    return replaceChild(clone, point1, getSubtree(parent2, point2))
#Q8
def fitness(known, generated):
    f = 0
    for i in range(len(known)):
        f += abs(known[i] - generated[i])
    return f
    
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

#Q9
def predict_rest(sequence):
    function_symbols = ['*', '+', '-']
    terminals = ['x', 'y', 'i'] + list(range(-2, 3))
    max_depth = 3
    solution_found = False
   
    #doesn't stop until a solution is found (could be a big problem!)
    while not solution_found:
        #generate a random expression, this is where you can do things like
        #crossover and mutation
        expression = make_random_expression(function_symbols, terminals, max_depth)  
        count = 0
        sequence_generated = sequence[:2]
        while count < (len(sequence) - 2):
            i = 2 + count
            x = sequence[i-2]
            y = sequence[i-1]
            bindings = {'x': x, '+': lambda x, y: x + y,
                        'y': y, '-': lambda x, y: x - y,
                        'i': i, '*': lambda x, y: x * y}
            #evaluate what the expression generates based on the first two
            #known items in the sequence
            sequence_generated.append(evaluate(expression, bindings))
            count += 1
        #if it fits perfectly it is the solution we will use
        if fitness(sequence, sequence_generated) == 0:
            solution_found = True
       
    #once the solution is found, return the next 5 numbers in the sequence
    return generate_rest(sequence, expression, 5)

print("Test case 1:")
sequence = [0, 1, 2, 3, 4, 5, 6, 7]
print(predict_rest(sequence))
print("correct: [8, 9, 10, 11, 12]")

print("Test case 2:")
sequence = [0, 2, 4, 6, 8, 10, 12, 14]
print(predict_rest(sequence))
print("correct:[16, 18, 20, 22, 24]")

print("Test case 3:")
sequence = [31, 29, 27, 25, 23, 21]
print(predict_rest(sequence))
print("correct: [19, 17, 15, 13, 11]")

print("Test case 4")
sequence = [0, 1, 4, 9, 16, 25, 36, 49]
print(predict_rest(sequence))
print("correct:[64, 81, 100, 121, 144]")

print("Test case 5")
sequence = [3, 2, 3, 6, 11, 18, 27, 38]
print(predict_rest(sequence))
print("correct:[51, 66, 83, 102, 123]")

print("Test case 6")
sequence =  [0, 1, 1, 2, 3, 5, 8, 13]
print(predict_rest(sequence))
print("correct :[21, 34, 55, 89, 144]")

print("Test case 7")
sequence = [0, -1, 1, 0, 1, -1, 2, -1]
print(predict_rest(sequence))
print("correct: [5, -4, 29, -13, 854]")

print("Test case 8")
sequence = [1, 3, -5, 13, -31, 75, -181, 437]
print(predict_rest(sequence))
print("correct: [-1055, 2547, -6149, 14845, -35839]")
