# Experiment: Wumpus World Problem
# Name: Yash | Reg No: 19255

import random

# Wumpus World environment setup (4x4 grid)
GRID_SIZE = 4
wumpus = (2, 2)
pit = (1, 3)
gold = (3, 1)
agent = (0, 0)

# Percept generator
def get_percepts(position):
    percepts = []
    x, y = position

    # Check adjacent cells for hazards
    if abs(x - wumpus[0]) + abs(y - wumpus[1]) == 1:
        percepts.append("Stench")
    if abs(x - pit[0]) + abs(y - pit[1]) == 1:
        percepts.append("Breeze")
    if position == gold:
        percepts.append("Glitter")
    return percepts

# Agent logic (simplified)
def wumpus_agent():
    global agent
    visited = set()
    has_gold = False

    while True:
        percepts = get_percepts(agent)
        print(f"Agent at {agent}, Percepts: {percepts}")

        if "Glitter" in percepts and not has_gold:
            print("Action: Grab Gold!")
            has_gold = True

        if has_gold and agent == (0, 0):
            print("Action: Climb out → SUCCESS! Gold collected ✅")
            break

        # Mark visited
        visited.add(agent)

        # Decide next move (safe random for simplicity)
        x, y = agent
        possible_moves = [(x+1,y), (x,y+1), (x-1,y), (x,y-1)]
        safe_moves = [m for m in possible_moves 
                      if 0 <= m[0] < GRID_SIZE and 0 <= m[1] < GRID_SIZE and m not in visited]

        if safe_moves:
            agent = random.choice(safe_moves)
            print(f"Action: Move to {agent}")
        else:
            if has_gold:
                print("No safe moves left → Returning to start...")
                agent = (0,0)   # Let the success condition trigger next loop
            else:
                print("No safe moves available → Agent failed ❌")
                break

# Run simulation
wumpus_agent()
