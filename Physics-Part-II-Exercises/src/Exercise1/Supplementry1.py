import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

def integrateError (N):

    nt= 25
    # m_input is the vector of size defined in n_values with each element the sum of 8 random numbers between 0 and pi/8
    mInput = np.random.uniform(0,pi/8,(N,nt))+np.random.uniform(0,pi/8,(N,nt))+np.random.uniform(0,pi/8,(N,nt))+np.random.uniform(0,pi/8,(N,nt))+np.random.uniform(0,pi/8,(N,nt))+np.random.uniform(0,pi/8,(N,nt))+np.random.uniform(0,pi/8,(N,nt))+np.random.uniform(0,pi/8,(N,nt))
        
    meanF = np.sum(np.sin(mInput),axis =0)/N
    meanF2 = np.sum((np.sin(mInput))**2,axis =0)/N
    
    #Error from taking sdv of nt estimates of the integral
    integration_sdv = np.std(meanF * 10**6 * (pi/8)**8)
    #Error from taking the mean of nt theoretical error estimates from theory
    theory_Error = np.mean( (10**6 * (pi/8)**8) * ((meanF2 - meanF**2)/N)**(1/2))
    
    return (integration_sdv,theory_Error)

powerrange = 15
TheoryError = np.empty(powerrange)
MCError = np.empty(powerrange)
x_range = np.empty(powerrange)

#loop producing y and x axis for graphs
for n in range(powerrange):
    MCError[n],TheoryError[n] = integrateError(2**n)
    x_range[n] = 2**n
    
plt.plot(x_range,TheoryError,label = "Theoretical Error")
plt.plot(x_range,MCError,label = "Simulation Error")
plt.xscale('log')
plt.legend()
plt.ylabel("Error")
plt.xlabel("N")
plt.title("Plot of Errors against Value of N")
plt.savefig("T&S-Errors-N.png",bbox_inches='tight')

    
