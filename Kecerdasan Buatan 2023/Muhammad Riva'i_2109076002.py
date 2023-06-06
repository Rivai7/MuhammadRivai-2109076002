import random

# Definisi batasan nilai variabel
a_min = 0
a_max = 30
b_min = 0
b_max = 10
c_min = 0
c_max = 10
d_min = 0
d_max = 10

# Definisi jumlah populasi, crossover rate, dan mutation rate
population_size = 6
crossover_rate = 0.8
mutation_rate = 0.1

# Fungsi objektif
def fitness(chromosome):
    a, b, c, d = chromosome
    return abs(a + 4*b + 2*c + 3*d - 30)

# Inisialisasi populasi
population = []
for _ in range(population_size):
    chromosome = [random.randint(a_min, a_max),
                  random.randint(b_min, b_max),
                  random.randint(c_min, c_max),
                  random.randint(d_min, d_max)]
    population.append(chromosome)

# Evaluasi populasi
fitness_values = [fitness(chromosome) for chromosome in population]
total_fitness = sum(fitness_values)

# Seleksi Chromosome
probabilities = [fitness_value / total_fitness for fitness_value in fitness_values]
cumulative_probabilities = [sum(probabilities[:i+1]) for i in range(population_size)]

# Pemilihan induk dengan roulette wheel selection
selected_population = []
for _ in range(population_size):
    r = random.random()
    for i in range(population_size):
        if cumulative_probabilities[i] > r:
            selected_population.append(population[i])
            break

# Crossover
offspring_population = []
for i in range(0, population_size-1, 2):
    parent1 = selected_population[i]
    parent2 = selected_population[i+1]
    
    if random.random() < crossover_rate:
        # One-point crossover
        crossover_point = random.randint(1, 3)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
    else:
        child1 = parent1
        child2 = parent2
    
    offspring_population.append(child1)
    offspring_population.append(child2)

# Mutasi
for i in range(population_size):
    if random.random() < mutation_rate:
        chromosome = offspring_population[i]
        gene_to_mutate = random.randint(0, 3)
        if gene_to_mutate == 0:
            chromosome[gene_to_mutate] = random.randint(a_min, a_max)
        elif gene_to_mutate == 1:
            chromosome[gene_to_mutate] = random.randint(b_min, b_max)
        elif gene_to_mutate == 2:
            chromosome[gene_to_mutate] = random.randint(c_min, c_max)
        else:
            chromosome[gene_to_mutate] = random.randint(d_min, d_max)

# Gabungkan populasi induk dan populasi anak
population = selected_population + offspring_population

# Evaluasi populasi setelah crossover dan mutasi
fitness_values = [fitness(chromosome) for chromosome in population]
best_fitness = min(fitness_values)
best_chromosome = population[fitness_values.index(best_fitness)]

# Cetak hasil
print("Best Chromosome:", best_chromosome)
print("Best Fitness:", best_fitness)
