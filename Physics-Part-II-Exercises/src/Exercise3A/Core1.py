import matplotlib.pyplot as plt
import numpy as np
from numpy import pi

mu0 = 4*pi*10**(-7)
Current= 1/mu0

def computedB (dlInfo,B,position): # Computes dB for the individual dl
    r = position - np.split(dlInfo,2)[0]
    modr = np.sqrt(np.sum(r**2))
    dlCrossr = np.cross(np.split(dlInfo,2)[1],r)
    #dB = mu0/4π * Idl^r/r^3
    dB = (mu0/(4*pi)) * (Current/modr**3) * dlCrossr
    return dB

def FindB (position,Coil):  # Finds the B field at a certain coordinate
    B= [0,0,0]
    for dlInfo in Coil:
        B = B + computedB(dlInfo,1,position)
    return B

def CreateCoilX(r,Radius): #Creates a coil along x axis at r with a radius producing an array of position and direction of segments 
    dlNumber = 10
    n = np.linspace(0,2*pi,num = dlNumber)
    dlLength = 2*pi*Radius/dlNumber
    coilInfo = np.empty((dlNumber,6)) # First 3 values give position r, last 3 values give dl
    coilInfo[:,0] = r[0] # set x value
    coilInfo[:,1] = r[1] + Radius*np.cos(n)
    coilInfo[:,2] = r[2] + Radius*np.sin(n)
    coilInfo[:,3] = 0
    coilInfo[:,4] = dlLength*(-np.sin(n))
    coilInfo[:,5] = dlLength*(np.cos(n))
    return coilInfo

def TestingGraph (): #Plots a graph testing the simulation against theory

    x_range = np.linspace(0,5,num=20)
    B = np.empty((x_range.size,3))
    BTheory = np.empty(x_range.size)
    Coil000 = CreateCoilX([0,0,0],1)
    for n in range(x_range.size):
        B[n] = FindB([x_range[n],0,0],Coil000)
        #Uses theory to calculate B on x axis for coil of Radius 1 and current 1/μ
        BTheory[n] = 1/(2*(1+(x_range[n])**2)**(3/2))
    plt.plot(x_range,B[:,0],label="Computation")
    plt.plot(x_range,BTheory,label="Theory")
    plt.plot(x_range,B[:,0]-BTheory,label="Difference")
    plt.legend()
    plt.show()

TestingGraph()

