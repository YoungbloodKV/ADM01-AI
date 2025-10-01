# Experiment 13: Genetic Algorithm (maximize f(x) = x^2)

import random

# Parameters
POP_SIZE = 6
CHROM_LENGTH = 5   # 5 bits → 0–31
GENERATIONS = 10
MUTATION_RATE = 0.1

# Fitness function: f(x) = x^2
def fitness(chromosome):
    x = int("".join(str(bit) for bit in chromosome), 2)
    return x**2

# Generate random chromosome
def random_chromosome():
    return [random.randint(0,1) for _ in range(CHROM_LENGTH)]

# Selection: roulette wheel
def select(population):
    total_fitness = sum(fitness(ch) for ch in population)
    pick = random.uniform(0, total_fitness)
    current = 0
    for ch in population:
        current += fitness(ch)
        if current > pick:
            return ch

# Crossover: single point
def crossover(parent1, parent2):
    point = random.randint(1, CHROM_LENGTH-1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# Mutation: flip a bit
def mutate(chromosome):
    for i in range(CHROM_LENGTH):
        if random.random() < MUTATION_RATE:
            chromosome[i] = 1 - chromosome[i]
    return chromosome

# GA main loop
def genetic_algorithm():
    population = [random_chromosome() for _ in range(POP_SIZE)]
    
    for gen in range(GENERATIONS):
        print(f"\nGeneration {gen+1}:")
        for ch in population:
            x = int("".join(str(bit) for bit in ch), 2)
            print(f"Chromosome: {ch}, x={x}, Fitness={fitness(ch)}")
        
        new_population = []
        while len(new_population) < POP_SIZE:
            p1, p2 = select(population), select(population)
            c1, c2 = crossover(p1, p2)
            new_population.append(mutate(c1))
            if len(new_population) < POP_SIZE:
                new_population.append(mutate(c2))
        
        population = new_population
    
    # Best solution
    best = max(population, key=fitness)
    best_x = int("".join(str(bit) for bit in best), 2)
    print("\n✅ Best solution found:")
    print(f"Chromosome: {best}, x={best_x}, Fitness={fitness(best)}")

# Run GA
genetic_algorithm()
