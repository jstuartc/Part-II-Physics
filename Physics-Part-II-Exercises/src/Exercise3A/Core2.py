
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi

mu0 = 4*pi*10**(-7)
Current= 1/mu0

def computedB (dlInfo,B,position):
    r = position - np.split(dlInfo,2)[0]
    modr = np.sqrt(np.sum(r**2))
    dlCrossr = np.cross(np.split(dlInfo,2)[1],r)
    #dB = mu0/4π * Idl^r/r^3
    dB = (mu0/(4*pi)) * (Current/modr**3) * dlCrossr
    return dB

def FindB (position,Coil):
    B= [0,0,0]
    for dlInfo in Coil:
        B = B + computedB(dlInfo,1,position)
    return B

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

def BField2CoilsGraph ():

    x_range = np.linspace(-1,1,num=30)
    y_range = np.linspace(-1,1,num=30)
    B = np.empty((x_range.size,y_range.size,3))
    X = np.empty(x_range.size)
    Y = np.empty(y_range.size)
    Coil500 = CreateCoilX([0,0,0],1)
    Coil_500 = CreateCoilX([0,0,0],1)
    for n in range(x_range.size):
        X[n] = x_range[n]
        for m in range(y_range.size):
            B[n,m] = FindB([0,y_range[m],x_range[n]],Coil500) + FindB([0,y_range[m],x_range[n]],Coil_500)
            Y[m] = y_range[m]
    modB = np.sqrt(B[:,:,0]**2 + B[:,:,1]**2 + B[:,:,2]**2)
    plt.contourf(X,Y,modB)
    plt.show()

BField2CoilsGraph()

