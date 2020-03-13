import matplotlib.pyplot as plt
import numpy as np
from numpy import pi

mu0 = 4*pi*10**(-7)
Current= 1/mu0

class SingleCoil:   #Class describing a single coil
    dlNumber = 30
    
    def __init__(self,position,radius): #init of object. Creates the info of the coil ie the positions of the individual line elements and the the direction they point
        self.__position = position
        self.__radius = radius
        n = np.linspace(0,2*pi,num = self.dlNumber)+pi
        dlLength = 2*pi*radius/self.dlNumber
        self.__coilInfo = np.empty((self.dlNumber,6))
        self.__coilInfo[:,0] = self.__position[0] 
        self.__coilInfo[:,1] = self.__position[1] + self.__radius*np.cos(n)
        self.__coilInfo[:,2] = self.__position[2] + self.__radius*np.sin(n)
        self.__coilInfo[:,3] = 0
        self.__coilInfo[:,4] = dlLength*(-np.sin(n))
        self.__coilInfo[:,5] = dlLength*(np.cos(n))
    
    def getCoilInfo(self):  #Returns the coil information of the line elements in a 2d array
        return self.__coilInfo
    
        
def computedB (dlInfo,B,position):
    r = position - np.split(dlInfo,2)[0]
    modr = np.sqrt(np.sum(r**2))
    dlCrossr = np.cross(np.split(dlInfo,2)[1],r)
    #dB = mu0/4π * Idl^r/r^3
    dB = (mu0/(4*pi)) * (Current/modr**3) * dlCrossr
    return dB

def FindB (position,Coil):
    B= [0,0,0]
    for dlInfo in Coil.getCoilInfo():
        B = B + computedB(dlInfo,1,position)
    return B

def CreateCoilSeriesX (Radius,Number): #Creates a series of N coils with Length of series 10x the coil radius
    coilXPosition = np.linspace((-Radius*5),(Radius*5),num = Number)
    CoilSeries = np.empty(Number,dtype = SingleCoil)
    for n in range(Number):
        CoilSeries[n] = SingleCoil([coilXPosition[n],0,0],Radius)
    return CoilSeries

def BFieldGraph (N,Radius,xlength,ylength): # Creates a plot of modB across a x and y range for N coils of radius R
    x_range = np.linspace(-xlength,xlength,num=40)
    y_range = np.linspace(-ylength,ylength,num=20)
    B = np.zeros((x_range.size,y_range.size,3))
    X = np.empty(x_range.size)
    Y = np.empty(y_range.size)
    CoilSeries = CreateCoilSeriesX(Radius, N)   #Creates list of length N of Coils
    for n in range(x_range.size):
        X[n] = x_range[n]
        for m in range(y_range.size):
            for Coil in CoilSeries:
                B[n,m] = B[n,m] + FindB([x_range[n],y_range[m],0],Coil)
            Y[m] = y_range[m]
    modB = np.sqrt(B[:,:,0]**2 + B[:,:,1]**2 + B[:,:,2]**2)
    
    plt.contourf(X,Y,np.transpose(modB))
    plt.title(f"Plot of modB against X and Y inside {N} coils of radius {Radius} with length {10*Radius}")
    plt.ylabel("Y/m")
    plt.xlabel("X/m")
    cbar = plt.colorbar()
    cbar.set_label("B")
    plt.savefig(f"modB - detail radius {Radius}, N = {N}.png",bbox_inches='tight')


BFieldGraph(10,1,4,0.2)
