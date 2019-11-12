import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
fig, ax=plt.subplots()
anim_object, = plt.plot([],[],marker='o')
def Cicloida_m(r, t):
    x=r*(t-np.sin(t))
    y=r*(1-np.cos(t))
    return x, y
edge=4
ax.set_xlim(-edge,edge)
ax.set_ylim(-edge,edge)
def animate(i):
    anim_object.set_data(Cicloida_m(r=1, t=i))
ani=animation.FuncAnimation(fig, animate, frames=np.arange(-4, 2*np.pi, 0.1), interval=100)

ani.save('Cicloida.gif')