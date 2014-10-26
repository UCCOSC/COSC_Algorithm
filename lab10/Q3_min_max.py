def max_value(tree, alpha=float('-inf'), beta=float('inf')):
    if isinstance(tree, int):
        return tree
    else:
        current = -float('inf')
        for i in range(len(tree)):
            current = max(current, min_value(tree[i], alpha, beta))
            if current >= beta:
                if tree[i+1:]:
                    print("Pruning:", ", ".join(map(str, tree[i+1:])))                 
                return current
            alpha = max(alpha, current)
        return current

def min_value(tree, alpha=float('-inf'), beta=float('inf')):
    if isinstance(tree, int):
        return tree
    else:
        current = float('inf')
        for i in range(len(tree)):
            current = min(current, max_value(tree[i], alpha, beta))
            if current <= alpha:
                if tree[i+1:]:
                    print("Pruning:", ", ".join(map(str, tree[i+1:])))            
                return current
            beta = min(beta, current)
        return beta

tree=[[3,[1,5,2]],[2,1,7],[[-1,8]]]
print(max_value(tree))
