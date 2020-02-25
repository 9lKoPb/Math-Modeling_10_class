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
   dvxdt = 3*g*z*x/(z**2 + x**2)
   dydt = vy
   dvydt = 0
   dzdt = vz
   dvzdt = -g + 3*g*z/(z**2 + x**2)*z
   
   return dxdt, dvxdt, dydt, dvydt, dzdt, dvzdt

#Нач.данные

g = 9.8
R = 1


x0 = 1
vx0 = 0

y0 = 0
vy0 = 1

z0 = 0
vz0 = 0



s0 = x0, vx0, y0, vy0, z0, vz0

sol = odeint(func, s0, t)

#3д_Объект

fig = plt.figure()
ax = p3.Axes3D(fig)


ball, = ax.plot(sol[:,0], sol[:,2], sol[:,4], 'o', color='k',ms='7')
line, = ax.plot(sol[:,0], sol[:,2], sol[:,4], '-',color='k')

def animation_func(i):
    ball.set_data(sol[i,0], sol[i,2])
    ball.set_3d_properties(sol[i,4])
    
    line.set_data(sol[:i,0], sol[:i,2])
    line.set_3d_properties(sol[:i,4])
    
    
yota = np.linspace(0, 10, 100)
theta = np.linspace(-np.pi,0 , 100)

x1 = R * np.outer(np.ones(np.size(yota)), np.cos(theta))
y1 = np.outer(yota, np.ones(np.size(theta)))
z1 = R * np.outer(np.ones(np.size(yota)), np.sin(theta))



ax.plot_surface(x1, y1, z1, color='r')


ax.set_xlim3d([-4.0, 4.0])
ax.set_xlabel('X')

ax.set_ylim3d([-4.0, 4.0])
ax.set_ylabel('Y')

ax.set_zlim3d([-4.0, 4.0])
ax.set_zlabel('Z')

ani = animation.FuncAnimation(fig, animation_func, N, interval=50)

ani.save('otsilka.gif')    
    