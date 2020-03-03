from scipy import integrate
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi

def funInput(q,F):
    def fun(t,y):
        dydt = [y[1],-np.sin(y[0])-q*y[1]+F*np.sin(2/3 * t)]
        return dydt
    return fun

def DampingIncreaseGraph ():
    tspan = [0,10*2*pi]
    yinit=[0.1,0]
    for q in [0,1,5,10]:
        f = funInput(q,0)
        sol = integrate.solve_ivp(f, tspan, yinit, max_step=0.1)
        plt.plot(sol.t,sol.y[0],label=(f"q =  {q}"))
    plt.title("Plot showing amplitude vs time for different damping levels")
    plt.ylabel("Angle")
    plt.xlabel("Time")
    plt.legend()
    plt.show()

DampingIncreaseGraph()