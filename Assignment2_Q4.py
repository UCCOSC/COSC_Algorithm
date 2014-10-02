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

# All the generated expressions must be valid

function_symbols = ['f', 'g', 'h']
terminals = ['x', 'y', 'i'] + list(range(-2, 3))
max_depth = 4

for _ in range(10000):
    expression = make_random_expression(function_symbols,
                                                       terminals,
                                                       max_depth)

    if not is_valid_expression(expression, function_symbols, terminals):
        print("The following expression is not valid:\n", expression)
        break
else:
    print("OK")

# Out of 10000 expressions, at least 1000 must be distinct
#~ 
#~ function_symbols = ['f', 'g', 'h']
#~ terminals = ['x', 'y', 'i'] + list(range(-2, 3))
#~ max_depth = 4
#~ 
#~ distinct_expressions = set(make_hashable(make_random_expression(
            #~ function_symbols, terminals, max_depth)) for _ in range(10000))
#~ 
#~ if len(distinct_expressions) < 1000:
    #~ print("Out of 10000 generated expressions, only {} are distinct.".
          #~ format(len(distinct_expressions)))
#~ else:
    #~ print("OK")
    #~ 
# Out of 10000 expressions, there must be at least 100 expressions
# of depth 0, 100 of depth 1, ..., and 100 of depth 4.

from collections import Counter

function_symbols = ['f', 'g', 'h']
terminals = ['x', 'y', 'i'] + list(range(-2, 3))
max_depth = 4

counter = Counter(depth(make_random_expression(
            function_symbols, terminals, max_depth)) for _ in range(10000))

if all(count > 100 for count in counter.values()):
    print("OK")
else:
    print("Failed:")
    print(counter)
