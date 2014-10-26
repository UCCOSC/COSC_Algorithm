def max_value(tree):
    if isinstance(tree,int):
        return tree
    else:
        current = -float('Inf')
        for i in tree:
            current = max(current, min_value(i))
        return current

def min_value(tree):
    if isinstance(tree,int):
        return tree
    else:
        current = float('Inf')
        for i in tree:
            current = min(current, max_value(i))
        return current

tree=[ [3, [1, 5, 2]], [2, 1, 7], [[-1,8]]]
print(min_value(tree))
