# Experiment 6: Vacuum Cleaner Problem

def vacuum_cleaner(world, start):
    location = start
    steps = []
    
    while "Dirty" in world.values():
        if world[location] == "Dirty":
            steps.append(f"Location {location} is dirty. Cleaned!")
            world[location] = "Clean"
        else:
            steps.append(f"Location {location} is already clean.")
        
        # Move to other room
        location = "B" if location == "A" else "A"
    
    steps.append("Both rooms are clean now!")
    return steps

# Example world state
world = {"A": "Dirty", "B": "Dirty"}
steps = vacuum_cleaner(world, "A")

for s in steps:
    print(s)
