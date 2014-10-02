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

print("First Test Case:")
expression = ['+', 44, ['f', 'x', 22]]
depth_limit = 2
for point, depth in mutation_points(
    expression, depth_limit):
    print("The tree substituting node {} can have a max depth of {}."
          .format(point, depth))
print()

print("Second Test Case:")
expression = ['g', 'i', ['f', ['h', 'y', 2], 0]]
depth_limit = 4
for pair in sorted(mutation_points(
        expression, depth_limit)):
    print(pair)
print()

print("Third Test Case:")
print(mutation_points(367, 10))
print()

print("Fouth Test Case:")
expression = ['f', 'i', ['g', ['h', ['f', 1, 'x'], 2],
                         ['g', ['f', 'i', -1], ['h', 1, 2]]]]
depth_limit = 4
for pair in sorted(mutation_points(
        expression, depth_limit)):
    print(pair)
