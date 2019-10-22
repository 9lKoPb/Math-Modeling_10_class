from PhyConst import g, k, e, h
from math import cos, tan, sqrt, pi
v = sqrt((g*100*tan((30*pi)/180)**2)/(2*cos(pi/3)**2*(1-tan((30*pi)/180)*tan(pi/3))))
print(v)
N=(2/sqrt(pi))*(h/(k*200)**(3/2))*(e**(-300/k*200))*(300**(200/2))
print(N)