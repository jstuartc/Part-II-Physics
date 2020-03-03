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
    plt.savefig("Angle-time-Damped.png",bbox_inches='tight')
    plt.show()
    
def DrivingForceIncreaseGraph ():
    tspan = [0,10*2*pi]
    yinit=[0,0]
    q = 0.5
    for F in [0.5,1.2,1.44,1.465]:
        f = funInput(q,F)
        sol = integrate.solve_ivp(f, tspan, yinit, max_step=0.1)
        angle = sol.y[0]%(2*pi)
        angle = np.where(angle < pi, angle, angle-2*pi)
        plt.figure("Angle")
        plt.plot(sol.t,angle,label=(f"F =  {F}"))
        plt.figure("Velocity")
        plt.plot(sol.t,sol.y[1],label=(f"F =  {F}"))
    
    plt.figure("Angle")
    plt.title("Plot showing amplitude vs time for different Driving Forces with q = 0.5")
    plt.ylabel("Angle")
    plt.xlabel("Time")
    plt.legend()
    plt.savefig("Angle-time-Forced.png",bbox_inches='tight')
    
    plt.figure("Velocity")
    plt.title("Plot showing velocity vs time for different Driving Forces with q = 0.5")
    plt.ylabel("Velocity")
    plt.xlabel("Time")
    plt.legend()
    plt.savefig("Velocity-Time-Forced.png",bbox_inches='tight')
    plt.show()

DampingIncreaseGraph()    
DrivingForceIncreaseGraph()