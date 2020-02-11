import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation
#Задаю пространства
fig = plt.figure()
ax = p3.Axes3D(fig)
N = 100
phi = np.linspace(2 * np.pi, 0, N)
theta = np.linspace(5*np.pi, 0, N)

#Начальные данные
h = 0.5

x1 = np.outer(phi , np.cos(theta))
y1 = np.outer(phi , np.sin(theta))
z1 = h*np.outer(np.ones(np.size(theta)), theta)
ax.plot_surface(x1, y1, z1, color='w')
plt.show()

x = phi * np.cos(theta)
y = phi * np.sin(theta)
z = h * theta


ball, = ax.plot(x, y, z, 'o', color='r',ms='10')
line, = ax.plot(x, y, z, '-',color='k')

def animation_func(i):
    ball.set_data(x[i], y[i])
    ball.set_3d_properties(z[i])
    
    line.set_data(x[:i], y[:i])
    line.set_3d_properties(z[:i])
    
    
    
ax.set_xlim3d([-4.0, 4.0])
ax.set_xlabel('X')

ax.set_ylim3d([-4.0, 4.0])
ax.set_ylabel('Y')

ax.set_zlim3d([0, 6.0])
ax.set_zlabel('Z')

ani = animation.FuncAnimation(fig, animation_func, N, interval=50)

ani.save('dvizh.gif')