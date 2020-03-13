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

def FindB (position,Coil): # Finds the B field at a certain coordinate
    B= [0,0,0]
    for dlInfo in Coil:
        B = B + computedB(dlInfo,1,position)
    return B

def CreateCoilX(r,Radius): #Creates a coil along x axis at r with a radius producing an array of position and direction of segments 
    dlNumber = 31
    n = np.linspace(0,2*pi,num = dlNumber)+pi/2
    dlLength = 2*pi*Radius/dlNumber
    coilInfo = np.empty((dlNumber,6)) # First 3 values give position r, last 3 values give dl
    coilInfo[:,0] = r[0] # set x value
    coilInfo[:,1] = r[1] + Radius*np.cos(n)
    coilInfo[:,2] = r[2] + Radius*np.sin(n)
    coilInfo[:,3] = 0
    coilInfo[:,4] = dlLength*(-np.sin(n))
    coilInfo[:,5] = dlLength*(np.cos(n))
    return coilInfo

def BField2CoilsGraph (): #Plots a plot which shows how B changes in a small cylinder in the middle of 2 coils

    x_range = np.linspace(-0.05,0.05,num=31)
    y_range = np.linspace(-0.05,0.05,num=31)
    B = np.empty((x_range.size,y_range.size,3))
    X = np.empty(x_range.size)
    Y = np.empty(y_range.size)
    Coil500 = CreateCoilX([0.5,0,0],1)
    Coil_500 = CreateCoilX([-0.5,0,0],1)
    for n in range(x_range.size):
        X[n] = x_range[n]
        for m in range(y_range.size):
            B[n,m] = FindB([x_range[n],y_range[m],0],Coil500)  + FindB([x_range[n],y_range[m],0],Coil_500)# Finds B at a point using 2 coils
            Y[m] = y_range[m]
    modB = np.sqrt(B[:,:,0]**2 + B[:,:,1]**2 + B[:,:,2]**2)
    #Reference B-Field at Origin
    modBOrigin = np.sqrt(np.sum((FindB([0,0,0],Coil500)+FindB([0,0,0],Coil_500))**2))
    #Deviation of B field
    modBDeviation = modB/(modBOrigin)
    plt.contourf(X,Y,np.transpose(modBDeviation-1))
    plt.title("Plot of the fractional deviation of modB against X and Y inside 2 coils at +/- 0.5m")
    plt.ylabel("Y/m")
    plt.xlabel("X/m")
    plt.colorbar()
    
    print("The maximum percentage difference in this Volume is",np.amax(abs((modBDeviation-1))))
    plt.savefig("Fractional change in ModB field across an area of Y and X in the z = 0 plane.png",bbox_inches='tight')
    
    



BField2CoilsGraph()



