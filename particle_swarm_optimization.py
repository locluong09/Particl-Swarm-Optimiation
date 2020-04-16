import numpy as np
import math
import copy

from utils import Particle

class PSO(object):
	'''
	Particle swarm optimization class
	---
	Attribues
		nb_generations : number of generations of swarm. It means the number of iterations
		nb_populations : the size of swarm (number of particle in swarm)
		objective_class : the objective function defined as class
		w : the inertia weight, range: (0,1)
		c1 : the cognitive weight, range (0,1)
		c2 : the social weight, range (0,1)
		max_velocity : the maximum value of velocity, use to set constraints of veloctity
		min_velocity : the mininum value of velocity, use to set constraints of veloctity
		gbest : the global best swarm so far during training process.
	'''
	def __init__(self, nb_generations, nb_populations, objective_class, w, c1, c2, max_velocity, min_velocity):
		self.nb_generations = nb_generations
		self.nb_populations = nb_populations
		self.objective_class = objective_class
		self.w = w
		self.c1 = c1
		self.c2 = c2
		self.max_velocity = max_velocity
		self.min_velocity = min_velocity
		self.swarm = []
		self.gbest = None

	def set_bounds(self):
		self.lower = self.objective_class.lo_bounds
		self.upper = self.objective_class.up_bounds

	def set_swarm(self, dimensions):
		self.set_bounds()
		for i in range(self.nb_populations):
			particle = Particle(dimensions)

			if hasattr(particle, 'set_position'):
				particle.set_position(self.lower, self.upper)

			if hasattr(particle, 'set_velocity'):
				particle.set_velocity(self.max_velocity, self.min_velocity)

			self.swarm.append(particle)

	def evolve(self):
		#initial the swarm
		self.set_swarm(self.objective_class.n_variables)

		#set objective function
		ob_class = self.objective_class


		#initialize gbest in swarm
		self.gbest = copy.copy(self.swarm[0])
		

		for i in range(self.nb_generations):
			for particle in self.swarm:
				particle.update_velocity(self.w, self.c1, self.c2, self.gbest.position)
				particle.update_position(self.lower, self.upper)
				particle.calculate_fitness(ob_class)

				if particle.fitness < particle.best_fitness:
					particle.best_fitness = particle.fitness
					particle.pbest = particle.position

				if particle.fitness < self.gbest.fitness:
					self.gbest = particle
			print("At iteration : {}, best position is : {}, with best fitness : {}".format(i, self.gbest.position, self.gbest.fitness))

		return self.gbest