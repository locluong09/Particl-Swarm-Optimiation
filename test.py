import numpy as np

np.random.seed(seed = 1)

class Objective_function():
	'''
	Define an objective function as class
	---
	Atributes:
		ob_func : objective function
		n_varibales : number of variables of objective function
		up_bounds : list containing the uppper bound of  variables
		lo_bounds : list containing the lower bound of  variables
	Methods:
		set_bounds : set upper and lower bounds
		fitness : return output of objective function
	'''
	def __init__(self, ob_func, n_variables, up_bounds, lo_bounds):
		self.ob_func = ob_func
		self.n_variables = n_variables
		self.up_bounds = None
		self.lo_bounds = None

	def set_variables(self):
		self.variables = []
		for i in range(self.n_variables):
			self.variables.append(np.random.random())

	def set_bounds(self):
		if self.up_bounds is None:
			for i in range(len(n_variables)):
				self.up_bounds[i] = np.Inf

		if self.lo_bounds is None:
			for i in range(len(n_variables)):
				self.lo_bounds[i] = -np.NINF

	def fitness(self,ob_func):
		return self.ob_func(*self.variables)


def fun(x1,x2):
	return x1 + x2

up_bounds = [10,10]
lo_bounds = [0, 0]
ob_class = Objective_function(fun, 2, lo_bounds, up_bounds)
ob_class.set_variables()
print(ob_class.lo_bounds)
print(ob_class.variables)
print(ob_class.fitness(fun))

def func(x):
	f1 = x.ob_func
	return f1(1,2)

print(func(ob_class))

# class A1():
# 	def __init__(self):
# 		pass

# 	def f(self, x, y):
# 		return x+y

# class A2():
# 	def __init__(self, x, y):
# 		self.x = x
# 		self.y = y

# 	def method(self):
# 		a1 = A1()
# 		return a1.f(self.x,self.y)

# a2 = A2(1,2)
# print(a2.method())

