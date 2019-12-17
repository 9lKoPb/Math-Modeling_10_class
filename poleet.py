import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange(0, 3000, 0.01)

def diff(z, t):
    r, v = z
    dr_dt = v
    dv_dt = - (G*m)/r**2
    return dr_dt, dv_dt

r0 = 6400000
m = 5.94*10**24
G = 6*10**(-11)
v0 = 11.1*10**3

z0 = r0, v0

solve = odeint(diff, z0, t)
plt.plot(t, solve[:, 0], 'b', label = 'AAOOAOAOAO')
plt.legend()
plt.show()