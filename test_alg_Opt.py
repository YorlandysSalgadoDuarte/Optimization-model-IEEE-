import numpy as np
from mealpy import FloatVar, GA


def objective_function(solution):
    return np.sum(solution**2)

problem_dict = {
    "bounds": FloatVar( lb=(-10.0,) * 30, ub=(10.0,) * 30, name="delta"),
    "obj_func": objective_function,
    "minmax": "min",
}

model = GA.BaseGA(epoch=1000, pop_size=100, pc=0.9, pm=0.05)
g_best = model.solve(problem_dict)
print(f"Solution: {g_best.solution}, Fitness: {g_best.target.fitness}")
print(f"Solution: {model.g_best.solution}, Fitness: {model.g_best.target.fitness}")

model2 = GA.BaseGA(epoch=1000, pop_size=100, pc=0.9, pm=0.05, selection="tournament", k_way=0.4, crossover="multi_points")

# model3 = GA.BaseGA(epoch=1000, pop_size=50, pc=0.9, pm=0.05, crossover="one_point", mutation="scramble")

# model4 = GA.BaseGA(epoch=1000, pop_size=50, pc=0.9, pm=0.05, crossover="arithmetic", mutation_multipoints=True, mutation="swap")

# model5 = GA.BaseGA(epoch=1000, pop_size=50, pc=0.9, pm=0.05, selection="roulette", crossover="multi_points")

# model6 = GA.BaseGA(epoch=1000, pop_size=50, pc=0.9, pm=0.05, selection="random", mutation="inversion")

# model7 = GA.BaseGA(epoch=1000, pop_size=50, pc=0.9, pm=0.05, crossover="arithmetic", mutation="flip")