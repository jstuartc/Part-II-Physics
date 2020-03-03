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

def findPeriod (y,t,yStart,N): #Finds period of a cos wave (ie starts at y(0) = maximum)
    #where 2**N is the number of oscillations we look over
    #yStart = 1 for 1st calling
    x=yStart
    maxFound = False
    while (maxFound==False):
        if ((y[x]>y[x+1]) and (y[x-1]<y[x])):
            maxFound = True
        else:
            x = x+1
    if N == 0:
        return x
    if N == 1: 
        return sol.t[x]/2
    else:        
        return (findPeriod(y,t,(x-1)*2,N-1)/2)
    
def TheoryTest():
    tspanTest = [0,10*2*pi]
    yinitTest = [0.01,0]   
    
    solTest = integrate.solve_ivp(f, tspanTest, yinitTest,max_step=0.1)
    yTheory = 0.01* np.cos(solTest.t)

    plt.plot(solTest.t,solTest.y[0], label = 'RK method')
    plt.plot(solTest.t,yTheory,label = 'Small angle approximation')
    plt.legend()
    plt.title("Angle of Oscillations over 10 oscillations")
    plt.ylabel("Angle")
    plt.xlabel("Time")
    plt.show()

def EnergyGraph():
    #Finding the energy of the system E = KE + GPE where g = l = m = 1
    tspanEnergy = [0,1000*2*pi]
    yinitEnergy = [0.01,0]
    solEnergy = integrate.solve_ivp(f, tspanEnergy, yinitEnergy)
    Energy = (1-np.cos(solEnergy.y[0])) + 1/2 * (solEnergy.y[1])**2
    plt.plot(solEnergy.t,Energy)
    plt.title("Energy Change over 10000 oscillations")
    plt.ylabel("Energy")
    plt.xlabel("Time")
    plt.show()

EnergyGraph()
#print(findPeriod(sol.y[0],sol.t,1,7))


theta0 = 0.01
omega0 = 0

tspan = [0,1000*2*pi]
yinitTest = [theta0,omega0]

#sol = integrate.solve_ivp(f, tspan, yinit,max_step=0.1)

