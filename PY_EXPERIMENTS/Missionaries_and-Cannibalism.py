# Experiment 5: Missionaries and Cannibals Problem (BFS)

from collections import deque

def is_valid(m_left, c_left, m_right, c_right):
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if (m_left and m_left < c_left) or (m_right and m_right < c_right):
        return False
    return True

def missionaries_cannibals():
    start = (3, 3, 0, 0, 1)  # (M_left, C_left, M_right, C_right, Boat on left=1/right=0)
    goal = (0, 0, 3, 3, 0)
    
    q = deque()
    q.append((start, [start]))
    visited = set()
    
    while q:
        (m_left, c_left, m_right, c_right, boat), path = q.popleft()
        
        if (m_left, c_left, m_right, c_right, boat) == goal:
            print("Solution path:")
            for state in path:
                print(state)
            return
        
        if (m_left, c_left, m_right, c_right, boat) in visited:
            continue
        visited.add((m_left, c_left, m_right, c_right, boat))
        
        if boat == 1:  # Boat on left
            moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
            for m, c in moves:
                new_state = (m_left-m, c_left-c, m_right+m, c_right+c, 0)
                if is_valid(*new_state[:-1]):
                    q.append((new_state, path+[new_state]))
        else:  # Boat on right
            moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
            for m, c in moves:
                new_state = (m_left+m, c_left+c, m_right-m, c_right-c, 1)
                if is_valid(*new_state[:-1]):
                    q.append((new_state, path+[new_state]))

missionaries_cannibals()
