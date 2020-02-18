import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation
N = 200


t = np.linspace(0, 4.3, N)
#Дифф уравнение
def func(s, t):
   x, vx, y, vy, z, vz = s
   
   dxdt = vx
   dvxdt = (x/a**2)*(g - vx**2/a**2 - vy**2/b**2 - vz**2/c**2)/(x**2/a**4 + y**2/b**4 + z**2/c**4)
   dydt = vy
   dvydt = (y/b**2)*(g - vx**2/a**2 - vy**2/b**2 - vz**2/c**2)/(x**2/a**4 + y**2/b**4 + z**2/c**4)
   dzdt = vz
   dvzdt = -g + (x/a**2)*(g - vx**2/a**2 - vy**2/b**2 - vz**2/c**2)/(x**2/a**4 + y**2/b**4 + z**2/c**4)
   
   return dxdt, dvxdt, dydt, dvydt, dzdt, dvzdt
#Начальные параметры
x0 = 11.2
vx0 = 0

y0 = 3.5
vy0 = 0

z0 = 4
vz0 = 0

s0 = x0, vx0, y0, vy0, z0, vz0

g = 9.8

a = 15
b = 7
c = 8

sol = odeint(func, s0, t)

fig = plt.figure()
ax = p3.Axes3D(fig)



    
#3д объект
    
phi = np.linspace(0, 2*np.pi, 100)
theta = np.linspace(0, np.pi, 100)

x1 = a * np.outer(np.cos(phi), np.sin(theta))
y1 = b * np.outer(np.sin(phi), np.sin(theta))
z1 = c * np.outer(np.ones(np.size(phi), np.cos(theta)))


ball, = ax.plot(x1, y1, z1, 'o', color='r',ms='10')
line, = ax.plot(x1, y1, z1, '-',color='k')

def animation_func(i):
    ball.set_data(x1[i], y1[i])
    ball.set_3d_properties(z1[i])
    
    line.set_data(x1[:i], y1[:i])
    line.set_3d_properties(z1[:i])
    
    
    
ax.set_xlim3d([-4.0, 4.0])
ax.set_xlabel('X')

ax.set_ylim3d([-4.0, 4.0])
ax.set_ylabel('Y')

ax.set_zlim3d([0, 6.0])
ax.set_zlabel('Z')

ani = animation.FuncAnimation(fig, animation_func, N, interval=50)

ani.save('ponyal.gif')