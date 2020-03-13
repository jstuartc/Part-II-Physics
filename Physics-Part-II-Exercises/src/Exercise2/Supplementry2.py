from scipy import integrate
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi

def funInput(q,F):
    def fun(t,y):
        dydt = [y[1],-np.sin(y[0])-q*y[1]+F*np.sin(2/3 * t)]
        return dydt
    return fun

def PlotAngleAgainstVelocity (theta0,omega0,q,F,plotNum):
    tspan = [0,100*2*pi]
    f = funInput(q, F)
    yinit = [theta0,omega0]
    sol = integrate.solve_ivp(f, tspan, yinit, max_step=0.2)
    angle = sol.y[0]%(2*pi)
    angle = np.where(angle < pi, angle, angle-2*pi)
    
    plotNum.plot(angle,sol.y[1])
    plotNum.set_title(f" F = {F}, q = {q}, Θ = {theta0}, ω = {omega0}", fontsize = 8)
    plotNum.tick_params(axis='both', which='major', labelsize=6)
    plotNum.tick_params(axis='both', which='minor', labelsize=5)

def PlotMultipleConditions():
    fig, axs = plt.subplots(3,3)
    
    PlotAngleAgainstVelocity(2, 0, 0, 0,axs[0,0])    # Top row has q = F = 0 and has theata and omega either 2 or 0
    PlotAngleAgainstVelocity(0, 2, 0, 0,axs[0,1])
    PlotAngleAgainstVelocity(2, 2, 0, 0,axs[0,2])
    PlotAngleAgainstVelocity(2, 0, 0.5, 0,axs[1,0]) # This row investigates how different amounts of damping affects the solution of when theata = 2
    PlotAngleAgainstVelocity(2, 0, 1, 0,axs[1,1])
    PlotAngleAgainstVelocity(2, 0, 2, 0,axs[1,2])
    PlotAngleAgainstVelocity(0, 1, 1, 0,axs[2,0]) #This row sees what happens when omega is increased by a factor of 10 each time
    PlotAngleAgainstVelocity(0, 10, 1, 0,axs[2,1])
    PlotAngleAgainstVelocity(0, 100, 1, 0,axs[2,2])
    
    fig.suptitle("Velocity-Angle graphs for different starting conditions",y=1)
    fig.tight_layout()  
    plt.savefig("Velocity-Angle Graph for different starting Conditions.png",bbox_inches='tight')

PlotMultipleConditions() 
    