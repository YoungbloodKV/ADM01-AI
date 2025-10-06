# Experiment: Alpha-Beta Pruning Algorithm
# Name: Yash | Reg No: 19255

import math

# Alpha-Beta Pruning function
def alpha_beta(depth, nodeIndex, isMax, values, alpha, beta, maxDepth):
    # If at leaf node, return its value
    if depth == maxDepth:
        return values[nodeIndex]

    if isMax:
        best = -math.inf
        for i in range(2):  # Two children for each node
            val = alpha_beta(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta, maxDepth)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:  # Prune
                break
        return best
    else:
        best = math.inf
        for i in range(2):
            val = alpha_beta(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta, maxDepth)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:  # Prune
                break
        return best

# Example: Game tree with 8 leaf nodes
values = [3, 5, 6, 9, 1, 2, 0, -1]
maxDepth = int(math.log(len(values), 2))

print("Leaf node values:", values)
optimal = alpha_beta(0, 0, True, values, -math.inf, math.inf, maxDepth)
print("Optimal value found using Alpha-Beta Pruning:", optimal)
