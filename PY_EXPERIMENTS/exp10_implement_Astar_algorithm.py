# Experiment 10: A* Algorithm

import heapq

def a_star(graph, start, goal, heuristic):
    # Priority queue stores (f, g, node, path)
    open_set = []
    heapq.heappush(open_set, (0, 0, start, [start]))
    
    visited = set()
    
    while open_set:
        f, g, node, path = heapq.heappop(open_set)
        
        if node == goal:
            return path, g
        
        if node in visited:
            continue
        visited.add(node)
        
        for neighbor, cost in graph[node].items():
            if neighbor not in visited:
                g_new = g + cost
                h = heuristic[neighbor]
                f_new = g_new + h
                heapq.heappush(open_set, (f_new, g_new, neighbor, path+[neighbor]))
    
    return None, float("inf")

# Example Graph (with weights)
graph = {
    'A': {'B':1, 'C':4},
    'B': {'A':1, 'C':2, 'D':5},
    'C': {'A':4, 'B':2, 'D':1},
    'D': {'B':5, 'C':1, 'E':3},
    'E': {'D':3}
}

# Heuristic values (straight-line estimates to goal 'E')
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 0
}

path, cost = a_star(graph, 'A', 'E', heuristic)
print("Optimal Path:", path)
print("Total Cost:", cost)
