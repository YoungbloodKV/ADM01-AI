# Experiment 14: Simulated Annealing (Minimize f(x) = x^2)

import math, random

# Objective function
def f(x):
    return x**2

def simulated_annealing():
    # Initial solution
    current_x = random.uniform(-100, 100)
    current_cost = f(current_x)
    
    # Parameters
    T = 1000        # initial temperature
    T_min = 1e-3    # stopping temperature
    alpha = 0.95    # cooling rate
    
    best_x, best_cost = current_x, current_cost
    
    while T > T_min:
        # Generate neighbor
        new_x = current_x + random.uniform(-1, 1)
        new_cost = f(new_x)
        
        # Energy difference
        delta = new_cost - current_cost
        
        # Accept better or probabilistically accept worse
        if delta < 0 or random.random() < math.exp(-delta/T):
            current_x, current_cost = new_x, new_cost
        
        # Track best solution
        if current_cost < best_cost:
            best_x, best_cost = current_x, current_cost
        
        # Cool down
        T *= alpha
    
    return best_x, best_cost

# Run SA
solution, cost = simulated_annealing()
print("✅ Simulated Annealing Result:")
print(f"x = {solution:.4f}, f(x) = {cost:.4f}")
