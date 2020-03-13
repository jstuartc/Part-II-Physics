import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

def integrate (N):

    nt= 25
    # m_input is the vector of size defined in n_values with each element the sum of 8 random numbers between 0 and pi/8
    mInput = np.random.uniform(0,pi/8,(N,nt))+np.random.uniform(0,pi/8,(N,nt))+np.random.uniform(0,pi/8,(N,nt))+np.random.uniform(0,pi/8,(N,nt))+np.random.uniform(0,pi/8,(N,nt))+np.random.uniform(0,pi/8,(N,nt))+np.random.uniform(0,pi/8,(N,nt))+np.random.uniform(0,pi/8,(N,nt))
        
    mOutput = np.sum(np.sin(mInput)* 10**6 * (pi/8)**8,axis =0)/N

# mOutput is vector of size (25) each containing the sum of N sin(input) * Volume
    integration_mean = np.mean(mOutput)
    integration_sdv = np.std(mOutput)
    
    return (integration_mean,integration_sdv)
#initialising variables   
powerrange = 23
nMean = np.empty(powerrange)
nSdv = np.empty(powerrange)
x_range = np.empty(powerrange)

#loop producing y and x axis for graphs
for n in range(powerrange):
    nMean[n],nSdv[n] = integrate(2**n)
    x_range[n] = 2**n
    
#Plots creation - read titles
m, c = np.polyfit(np.log(x_range), np.log(nSdv), 1)
linear_fit = m*np.log(x_range) + c #Linear fit in log space
plt.loglog(x_range,nSdv,label= "Error for Monte Carlo Integration")
plt.loglog(x_range,np.exp(linear_fit),label= f"Linear fit with gradient {m:{3}.{3}}")
plt.legend()
plt.xlabel("N")
plt.ylabel("Error")
plt.title("Log-Log plot of average Error over 25 points against N")
plt.savefig("Error-Nloglog.png")


plt.figure()
plt.loglog(x_range,nMean,label= "Mean for Monte Carlo Integration")
plt.xlabel("N")
plt.ylabel("Mean")
plt.title("Log-Log plot of Mean over 25 points against N")
plt.savefig("Mean-Nloglog.png",bbox_inches='tight')
#printing best estimate of integral
print(nMean[-1],"+/-",nSdv[-1])