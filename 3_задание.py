from PhyConst import g
import numpy as np
t=np.arange(0, 6, 0.01)
x0=1
y0=2
v0=3
a = np.ndarray(shape=(100, 3))
for i in t:
    x=x0+v0*t
    y=y0+v0*t-(g*t**2)/2
    
    print(a)