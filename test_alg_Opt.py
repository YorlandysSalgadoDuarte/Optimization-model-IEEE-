import numpy as np
from mealpy import FloatVar, PSO,GA,MA,SHADE,PSS,RUN,SCA,SHIO,AOA,CEM,ASO
import time
inicio=time.time()

def objective_function(solution):
    return np.sum(solution**2)

problem_dict = {
    "bounds": FloatVar( lb=(-10.,) * 30, ub=(10.,) * 30, name="delta"),
    "obj_func": objective_function,
    "minmax": "min",
}
def Rosenbrock (solution,a=1.0,b=100.0):
    x=solution[0]
    y=solution[1]
    r=(a-x)**2+b*(y-x**2)**2
    return r

problem_dict_Rosenbrock = {
    "bounds": FloatVar( lb=[-2.0,-1.0], ub=[2.0,3.0], name="delta"),
    "obj_func": Rosenbrock,
    "minmax": "min",
}
#**************************Rosenbrock function PSO*************************************
model = PSO.OriginalPSO(epoch=1000, pop_size=50, c1=2.05, c2=2.5, w=0.4)
#******************************-GEnetic Algorithm****************************************
# model =  GA.BaseGA(epoch=10000, pop_size=50, pc=0.9, pm=0.05, crossover="arithmetic")
#***********************************************mealpy.evolutionary_based.SHADE module*******************************************
# model = SHADE.L_SHADE(epoch=1000, pop_size=50, miu_f = 0.5, miu_cr = 0.5)
#***********************************************mealpy.evolutionary_based.SHADE module¶******************************************
# model = SHADE.OriginalSHADE(epoch=1000, pop_size=50, miu_f = 0.5, miu_cr = 0.5)
#***********************************************mealpy.math_based.RUN module¶******************************************
# model = RUN.OriginalRUN(epoch=1000, pop_size=50)
#************************************mealpy.math_based.SCA module¶******************************************
# model = SCA.DevSCA(epoch=1000, pop_size=50)
#************************************mealpy.math_based.SHIO module¶******************************************
# model = SHIO.OriginalSHIO(epoch=1000, pop_size=50)
#************************************mealpy.physics_based package¶******************************************
# model = ASO.OriginalASO(epoch=1000, pop_size=100, alpha = 50, beta = 0.2)
g_best = model.solve(problem_dict)
print(f"Solution: {g_best.solution}, Fitness: {g_best.target.fitness}")
print(f"Solution: {model.g_best.solution}, Fitness: {model.g_best.target.fitness}")











#TODO *********************CALCULO DEL TIEMPO DE CORRIDA**************************************
final=time.time()
print(f'tiempo de iteracion del modelo es {final - inicio}\n')