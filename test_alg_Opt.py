import numpy as np
from mealpy import FloatVar, PSO

def objective_function(solution):
    return np.sum(solution**2)

problem_dict = {
    "bounds": FloatVar( lb=(-10.,) * 30, ub=(10.,) * 30, name="delta"),
    "obj_func": objective_function,
    "minmax": "min",
}

model = PSO.OriginalPSO(epoch=1000, pop_size=50, c1=2.05, c2=2.5, w=0.4)
g_best = model.solve(problem_dict)
print(f"Solution: {g_best.solution}, Fitness: {g_best.target.fitness}")
print(f"Solution: {model.g_best.solution}, Fitness: {model.g_best.target.fitness}")

#**************************Rosenbrock function PSO*************************************
def Rosenbrock (solution,a=1.0,b=100.0):
    x=solution[0]
    y=solution[1]
    return (a-x)**2+b*(y-x**2)**2

problem_dict_Rosenbrock = {
    "bounds": FloatVar( lb=[-2.0,-1.0], ub=[2.0,3.0], name="delta"),
    "obj_func": Rosenbrock,
    "minmax": "min",
}
model = PSO.OriginalPSO(epoch=1000, pop_size=50, c1=2.05, c2=2.5, w=0.4)
g_best = model.solve(problem_dict_Rosenbrock)
print(f"Solution: {g_best.solution}, Fitness: {g_best.target.fitness}")
print(f"Solution: {model.g_best.solution}, Fitness: {model.g_best.target.fitness}")