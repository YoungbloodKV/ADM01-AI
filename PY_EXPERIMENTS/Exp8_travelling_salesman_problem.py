# Experiment 9: Travelling Salesman Problem (Brute Force)

import itertools

def travelling_salesman(graph, start):
    nodes = list(graph.keys())
    nodes.remove(start)
    
    min_path = None
    min_cost = float("inf")
    
    for perm in itertools.permutations(nodes):
        path = [start] + list(perm) + [start]
        
        cost = 0
        for i in range(len(path)-1):
            cost += graph[path[i]][path[i+1]]
        
        if cost < min_cost:
            min_cost = cost
            min_path = path
    
    return min_path, min_cost

# Example Graph (Weighted)
graph = {
    'A': {'A':0, 'B':10, 'C':15, 'D':20},
    'B': {'A':10, 'B':0, 'C':35, 'D':25},
    'C': {'A':15, 'B':35, 'C':0, 'D':30},
    'D': {'A':20, 'B':25, 'C':30, 'D':0}
}

path, cost = travelling_salesman(graph, 'A')
print("Optimal Path:", path)
print("Minimum Cost:", cost)
