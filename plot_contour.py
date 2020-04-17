import numpy as np
import matplotlib.pyplot as plt


def func(x,y):
	#Function with 2 varibel x,y
	return np.sin(x+y) + (x-y)**2 -1.5*x + 2.5*y + 1

x = np.linspace(-1.5,4,100)
y = np.linspace(-3,4,100)

X,Y = np.meshgrid(x,y)
# Z = np.sin(X+Y) + np.power((X-Y),2) - 1.5*X + 2.5*Y + 1
Z = func(X,Y)
# levels = [-2, -1, 0, 1, 2, 3, 4]

fig = plt.figure(figsize=(6,5))
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax = fig.add_axes([left, bottom, width, height]) 

mycmap = plt.get_cmap('gist_earth')
cp = plt.contourf(X,Y,Z, cmap = 'gist_earth', extent = (-10,10,-20,20))
#plt.clabel(cp, inline = True, fontsize = 10)
#plt.clabel(cp, colors = 'k', fmt = '%2.1f', fontsize=12)
plt.colorbar(cp)
plt.scatter(0,2,color = 'k')
ax.set_title('Contour Plot')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()
