# Experiment 9: Travelling Salesman Problem with State Names

import itertools

def travelling_salesman_statewise(graph, start):
    nodes = list(graph.keys())
    nodes.remove(start)
    
    min_path = None
    min_cost = float("inf")
    
    print("Exploring States (Candidate Tours):\n")
    
    for perm in itertools.permutations(nodes):
        path = [start] + list(perm) + [start]
        
        cost = 0
        for i in range(len(path)-1):
            cost += graph[path[i]][path[i+1]]
        
        # Show this state
        print(f"Path: {path}, Cost = {cost}")
        
        if cost < min_cost:
            min_cost = cost
            min_path = path
    
    print("\n✅ Optimal State Found:")
    print(f"Path: {min_path}, Cost = {min_cost}")
    return min_path, min_cost


# Example Graph (Distances between cities in km, hypothetical)
graph = {
    "Delhi":    {"Delhi":0, "Mumbai":1400, "Chennai":2200, "Kolkata":1500},
    "Mumbai":   {"Delhi":1400, "Mumbai":0, "Chennai":1030, "Kolkata":1960},
    "Chennai":  {"Delhi":2200, "Mumbai":1030, "Chennai":0, "Kolkata":1670},
    "Kolkata":  {"Delhi":1500, "Mumbai":1960, "Chennai":1670, "Kolkata":0}
}

# Start from Delhi
path, cost = travelling_salesman_statewise(graph, "Delhi")
