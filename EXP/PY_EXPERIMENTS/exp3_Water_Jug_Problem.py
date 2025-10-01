# Experiment 3: Water Jug Problem (BFS)

from collections import deque

def water_jug_solver(jug1, jug2, target):
    visited = set()
    q = deque()
    
    q.append((0, 0))  # start with both jugs empty
    
    while q:
        x, y = q.popleft()
        
        if (x, y) in visited:
            continue
        visited.add((x, y))
        
        print(f"Jug1: {x} | Jug2: {y}")
        
        if x == target or y == target:
            print("Reached the target!")
            return
        
        # Possible moves
        moves = [
            (jug1, y),  # Fill jug1
            (x, jug2),  # Fill jug2
            (0, y),     # Empty jug1
            (x, 0),     # Empty jug2
            # Pour jug1 → jug2
            (x - min(x, jug2-y), y + min(x, jug2-y)),
            # Pour jug2 → jug1
            (x + min(y, jug1-x), y - min(y, jug1-x))
        ]
        
        for move in moves:
            if move not in visited:
                q.append(move)

# Example: jug1=4L, jug2=3L, target=2L
water_jug_solver(4, 3, 2)
