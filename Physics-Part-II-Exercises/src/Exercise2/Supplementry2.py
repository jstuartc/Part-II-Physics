from scipy import integrate
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi

def funInput(q,F):
    def fun(t,y):
        dydt = [y[1],-np.sin(y[0])-q*y[1]+F*np.sin(2/3 * t)]
        return dydt
    return fun

def PlotAngleAgainstVelocity (theta0,omega0,q,F):
    tspan = [0,1000*2*pi]
    f = funInput(q, F)
    yinit = [theta0,omega0]
    sol = integrate.solve_ivp(f, tspan, yinit, max_step=0.2)
    angle = sol.y[0]%(2*pi)
    angle = np.where(angle < pi, angle, angle-2*pi)
    
    plt.plot(angle,sol.y[1])
    plt.title(f"Plot showing Velocity vs Angle for F = {F}, q = {q}, Θ = {theta0} and ω = {omega0}")
    plt.ylabel("Velocity")
    plt.xlabel("Angle")
    plt.show()

PlotAngleAgainstVelocity(0.01, 0.01, 1, 1)