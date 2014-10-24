import copy
import random

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
#-----------------------------------------------------------------
def valid_crossover_points(parent1, parent2, depth_limit, var_p1 = 0, var_p2 = 0):
	current_depth = depth_limit
	if isinstance(parent1,list):
		valid_crossover_points(parent1[1], parent2, current_depth-1,var_p1+1)
		valid_crossover_points(parent1[2], parent2, current_depth-1,var_p1+1)
		
	if isinstance(parent2,list):
		valid_crossover_points(parent1, parent2[1], current_depth-1,var_p1, var_p2+1)
	return ((var_p1, var_p2),)
#-----------------------------------------------------------------
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

function_symbols = ['f', 'g', 'h']
terminals = ['x', 'y', 'i'] + list(range(-2, 3))
max_depth = 4

for _ in range(500):
    parent1 = make_random_expression(function_symbols, terminals, max_depth)
    parent1_copy = copy.deepcopy(parent1)
    parent2 = make_random_expression(function_symbols, terminals, max_depth)
    parent2_copy = copy.deepcopy(parent2)
    point1, point2 = random.choice(list(valid_crossover_points(
                parent1, parent2, max_depth)))
    child = crossover(parent1, parent2, point1, point2)
    if not is_valid_expression(child, function_symbols, terminals):
        print("The following returned child is not a valid expression.")
        print(child)
        break
    if not is_valid_crossover(parent1, parent2, point1, point2, child):
        print("The following case failed:")
        print("Parent 1:\n", parent1)
        print("Parent 2:\n", parent2)
        print("Point1:", point1, "Point2:", point2)
        print("Returned child:\n", child)
        break
    if parent1 != parent1_copy or parent2 != parent2_copy:
        print("Parents have changed.")
        print("Original parent1:", parent1_copy)
        print("Original parent2:", parent2_copy)
        print("Current parent1:", parent1)
        print("Current parent2:", parent2)
        break
else:
    print("OK")
