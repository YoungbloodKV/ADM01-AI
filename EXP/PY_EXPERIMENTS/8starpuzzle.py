import heapq

# Define goal state
goal_state = [[1,2,3],
              [4,5,6],
              [7,8,0]]   # 0 denotes the empty tile

# Utility to flatten 2D list
def flatten(state):
    return [num for row in state for num in row]

# Heuristic: Manhattan distance
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

# Find the position of the empty tile (0)
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate neighbors by moving empty tile
def get_neighbors(state):
    x, y = find_zero(state)
    moves = [(0,1),(1,0),(0,-1),(-1,0)]  # Right, Down, Left, Up
    neighbors = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# A* Search algorithm
def solve_puzzle(start_state):
    open_set = []
    heapq.heappush(open_set, (manhattan_distance(start_state), start_state, []))  # (f, state, path)
    visited = set()

    while open_set:
        f, state, path = heapq.heappop(open_set)
        if state == goal_state:
            return path + [state]
        state_tuple = tuple(flatten(state))
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        for neighbor in get_neighbors(state):
            new_path = path + [state]
            g = len(new_path)
            h = manhattan_distance(neighbor)
            heapq.heappush(open_set, (g + h, neighbor, new_path))
    return None

# Pretty print
def print_state(state):
    for row in state:
        print(row)
    print()

# Example usage
if __name__ == "__main__":
    # Initial configuration (change to test)
    start_state = [[1,2,3],
                   [4,0,6],
                   [7,5,8]]

    solution = solve_puzzle(start_state)
    if solution:
        print("Solution found in", len(solution)-1, "moves:")
        for step in solution:
            print_state(step)
    else:
        print("No solution found.")
