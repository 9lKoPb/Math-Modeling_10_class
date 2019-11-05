import matplotlib.pyplot as plt
import numpy as np
def grafics(a=1, b=2, c=2, k=1):
    x=np.arange(-3, 1, 0.01)
    y=a*x**2 + b*x + c
    plt.plot(x,y,label='parabola')
    x=np.arange(0.1,4,0.001)
    y=k/x
    plt.plot(x,y,label='giperbola')
    plt.legend()
    plt.show()
grafics()    