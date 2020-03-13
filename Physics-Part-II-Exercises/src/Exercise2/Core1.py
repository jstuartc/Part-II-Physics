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

def findPeriod (y,t,yStart): #Finds period of a cos wave (ie starts at y(0) = maximum)
    #yStart = 1 for 1st calling
    x=yStart
    maxFound = False
    while (maxFound==False):
        if ((y[x]>y[x+1]) and (y[x-1]<y[x])):
            maxFound = True
        else:
            x = x+1
    if  (x>y.size/2): 
        return t[x]/2
    else:        
        return (findPeriod(y,t,(x-2)*2)/2)  #Looks for another maximum twice as far down the line for better accuracy


def TheoryTest():#Funtion which shows that the integration method matches the small angle approximation    
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
    plt.savefig("Angle-Time-RK-Small-Angle.png",bbox_inches='tight')



def EnergyGraph():	#Function which produces a graph showing how energy changes over time
    #Finding the energy of the system E = KE + GPE where g = l = m = 1
    tspanEnergy = [0,1000*2*pi]
    yinitEnergy = [0.01,0]
    solEnergy = integrate.solve_ivp(f, tspanEnergy, yinitEnergy)
    Energy = (1-np.cos(solEnergy.y[0])) + 1/2 * (solEnergy.y[1])**2
    plt.plot(solEnergy.t,Energy)
    plt.title("Energy Change over 10000 oscillations")
    plt.ylabel("Energy")
    plt.xlabel("Time")
    plt.savefig("Energy-time.png",bbox_inches='tight')

def StartingAnglevsPeriod(): #Produces a graph showing how the period changes for changing starting angle
    length = 100
    tspan = [0,100*2*pi]
    angle = np.linspace(0.01,pi,num=length)
    period = np.empty(length)
    for n in range(length):
        yinit=[angle[n],0]
        sol = integrate.solve_ivp(f, tspan, yinit, max_step=0.2)
        period[n] = findPeriod(sol.y[0],sol.t,1)
        
    plt.plot(angle,period/period[0])
    plt.ylabel("Period T/T0")
    plt.xlabel("Starting angle")
    plt.title("Time Period against starting angle")
    plt.savefig("Period-against-Angle.png",bbox_inches='tight')

def FindPeriodforpi2 ():
    tspan = [0,100*2*pi]
    yinit=[pi/2,0]
    sol = integrate.solve_ivp(f, tspan, yinit, max_step=0.1)
    Period = findPeriod(sol.y[0],sol.t,1)
    print("The period for a starting angle of π/2 is",Period)
TheoryTest()
EnergyGraph()
StartingAnglevsPeriod()    
FindPeriodforpi2()

