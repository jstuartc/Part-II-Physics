from scipy import integrate
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi

def funInput(q,F):  #Returns a function which has the q and F as you desire
    def fun(t,y):
        dydt = [y[1],-np.sin(y[0])-q*y[1]+F*np.sin(2/3 * t)]
        return dydt
    return fun

def Comparison(): #Function showing the difference of the starting conditions
    
    #Plots first the two ampplitudes over time and then plots the Δθ over time
    
    tspan = [0,100*2*pi]
    q = 0.5
    F = 1.2
    f = funInput(q, F)
    
    yinitA = [0.2,0]
    solA = integrate.solve_ivp(f, tspan, yinitA, max_step=0.2)
    angleA = solA.y[0]%(2*pi)
    angleA = np.where(angleA < pi, angleA, angleA-2*pi)
    
    yinitB = [0.20001,0]
    solB = integrate.solve_ivp(f, tspan, yinitB, max_step=0.2)
    angleB = solB.y[0]%(2*pi)
    angleB = np.where(angleB < pi, angleB, angleB-2*pi)
    
    plt.plot(solA.t,angleA,label="Initial θ = 0.2")
    plt.plot(solB.t,angleB,label="Initial θ = 0.20001")
    plt.legend()
    plt.title("Plot showing amplitude vs time for different starting conditions")
    plt.ylabel("Angle")
    plt.xlabel("Time")
    plt.savefig("Displacement-time-InitalConditions.png",bbox_inches='tight')
    
    AngleDifference = angleA-angleB
    plt.figure()
    plt.plot(solA.t,AngleDifference)
    plt.title("Plot showing ΔΘ for different starting conditions")
    plt.ylabel("ΔΘ")
    plt.xlabel("Time")
    plt.savefig("ΔΘ-time-InitalConditions.png",bbox_inches='tight')
Comparison()
    