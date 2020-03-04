import matplotlib.pyplot as plt
import numpy as np
from numpy import pi

def computedB ():
    mu0 = 4*pi*10**(-7)
    #dB = mu0/4π * Idl^r/r^3
    return dB

def FindB (Position,Coil):
    
    return B(x,y,z)

def CreateCoilX(r,Radius): #Creates a coil along x axis at r with a radius producing an array of position and direction of segments 
    dlNumber = 50
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

Coil000 = CreateCoilX([0,2,2], 1)

plt.plot(Coil000[:,1],Coil000[:,2])
plt.show()
