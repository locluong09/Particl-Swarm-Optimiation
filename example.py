import numpy as np
import math

from utils import Objective_function
from particle_swarm_optimization import PSO

# Define the objective function
def func(x,y):
	#Function with 2 varibel x,y
	return np.sin(x+y) + (x-y)**2 -1.5*x + 2.5*y + 1

#set contraint for varibles
lo_bounds = [-1.5,-3]
up_bounds = [4,4]

def main():
	# Define objective class
	objective_class = Objective_function(func,2,lo_bounds, up_bounds)

	#set PSO optimizer
	pso_opt = PSO(nb_generations = 10,
				nb_populations = 50,
				objective_class = objective_class,
				w = 0.5,
				c1 = 0.8,
				c2 = 0.9,
				max_velocity = 10,
				min_velocity = -10)

	pso_opt.evolve()

if __name__ == "__main__":
	main()


