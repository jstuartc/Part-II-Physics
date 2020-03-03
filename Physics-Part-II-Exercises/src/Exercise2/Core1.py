from scipy import integrate
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi

#Re-written diferential equations
#y1 = d/dt(y0),  d/dt(y1) = -sin(y0) -q*y1 + Fsin(2/3 t)
# at t= 0 y1=0 y0 = 0.01

def f(t,y):
    F=0
    q=0
    dydt = [y[1],-np.sin(y[0])-q*y[1]+F*np.sin(2/3 * t)]
    return dydt

def findRoot:
    

theta0 = 0.01
omega0 = 0

tspan = [0,10000*2*pi]
yinit = [theta0,omega0]


sol = integrate.solve_ivp(f, tspan, yinit)

yTheory = theta0* np.cos(sol.t)
'''
plt.plot(sol.t,sol.y[0], label = 'RK method')
plt.plot(sol.t,yTheory,label = 'Small angle approximation')
plt.legend()
plt.title("Angle of Oscillations over 10 oscillations")
plt.ylabel("Angle")
plt.xlabel("Time")
plt.show()
'''
#Finding the energy of the system E = KE + GPE where g = l = m = 1
Energy = (1-np.cos(sol.y[0])) + 1/2 * (sol.y[1])**2
plt.plot(sol.t,Energy)
plt.show()

