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
    
expression = 12
print(depth(expression))

expression = 'weight'
print(depth(expression))

expression = ['add', 12, 'x']
print(depth(expression))

expression = ['add', ['add', 22, 'y'], 'x']
print(depth(expression))

expression = ['add', ['add', ['add', ['add', 2, 5], 5], 'y'], ['add', ['add', ['add', ['add', ['add', ['add', 2, 5], 5], 5], 5], 5], 5]]
print(depth(expression))
