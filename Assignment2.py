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





function_symbols = ['f', '+']
terminal_symbols = ['x', 'y']
expression = 1
d = "Correct"
e = "Error"
if (is_valid_expression(expression, function_symbols, terminal_symbols)) == True:
	print(d)
else:
	print(e)
function_symbols = ['f', '+']
terminal_symbols = ['x', 'y']
expression = 'y'

if (is_valid_expression(
        expression, function_symbols, terminal_symbols)) == True:
			print(d)
else:
	print(e)
	
function_symbols = ['f', '+']
terminal_symbols = ['x', 'y']
expression = 2.0

if (is_valid_expression(
        expression, function_symbols, terminal_symbols)) == False:
			print(d)
else:
	print(e)
	
function_symbols = ['f', '+']
terminal_symbols = ['x', 'y']
expression = ['f', 123, 'x']

if (is_valid_expression(
        expression, function_symbols, terminal_symbols)) == True:
			print(d)
else:
	print(e)
	
function_symbols = ['f', '+']
terminal_symbols = ['x', 'y']
expression = ['f', ['+', 0, -1], ['f', 1, 'x']]

if (is_valid_expression(
        expression, function_symbols, terminal_symbols)) == True:
			print(d)
else:
	print(e)
	
function_symbols = ['f', '+']
terminal_symbols = ['x', 'y']
expression = ['+', ['f', 1, 'x'], -1]

if (is_valid_expression(
        expression, function_symbols, terminal_symbols)) == True:
			print(d)
else:
	print(e)
	
function_symbols = ['f', '+']
terminal_symbols = ['x', 'y', -1, 0, 1]
expression = ['f', 0, ['f', 0, ['f', 0, ['f', 0, 'x']]]]

if (is_valid_expression(
        expression, function_symbols, terminal_symbols)) == True:
			print(d)
else:
	print(e)

function_symbols = ['f', '+']
terminal_symbols = ['x', 'y']
expression = 'f'

if (is_valid_expression(
        expression, function_symbols, terminal_symbols)) == False:
			print(d)
else:
	print(e)
	
function_symbols = ['f', '+']
terminal_symbols = ['x', 'y']
expression = ['f', 1, 0, -1]

if (is_valid_expression(
        expression, function_symbols, terminal_symbols)) == False:
			print (d)
else:
	print(e)
	
function_symbols = ['f', '+']
terminal_symbols = ['x', 'y']
expression = ['x', 0, 1]

if (is_valid_expression(
        expression, function_symbols, terminal_symbols)) == False:
			print(d)
else:
	print(e)
	
function_symbols = ['f', '+']
terminal_symbols = ['x', 'y']
expression = ['g', 0, 'y']

if (is_valid_expression(
        expression, function_symbols, terminal_symbols)) == False:
			print (d)
else:
	print(e)
