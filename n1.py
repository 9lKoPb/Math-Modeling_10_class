import numpy as np
import matplotlib.pyplot as plt
def Cicloida(r=2):
    t = np.arange(-2*np.pi,2*np.pi, 0.1)
    x=r*(t-np.sin(t))
    y=r*(1-np.cos(t))
    plt.plot(x,y,label='Cicloida')
    plt.xlim(-10*np.pi,10*np.pi)
    plt.ylim(-10*np.pi,10*np.pi)
    plt.legend()
    plt.show()
Cicloida()    