import numpy as np
from scipy import integrate
from numpy import pi

def func (vector):  # integral of sin(x)
    return (np.sin(vector))

mvect_func = np.vectorize(func)   # Vectorisation of sin
n_values = [10]

for n in n_values:
    # m_input is the vector of size defined in n_values with each element the sum of 8 random numbers between 0 and pi/8
    mInput = np.random.uniform(0,pi/8,(n,25))+np.random.uniform(0,pi/8,(n,25))+np.random.uniform(0,pi/8,(n,25))+np.random.uniform(0,pi/8,(n,25))+np.random.uniform(0,pi/8,(n,25))+np.random.uniform(0,pi/8,(n,25))+np.random.uniform(0,pi/8,(n,25))+np.random.uniform(0,pi/8,(n,25))
    mOutput = mvect_func(mInput)* 10**6 * (pi/8)**8

# mMean is mean integrand multiplied by volume of space
    mMean = np.sum(mOutput,axis=0)/n
    mSdv_vector = np.std(mOutput,axis=0)
    print(mSdv_vector)
    print(mMean)
#    mSdv_Mean = np.std(mOutput)/np.sqrt(n) #This is the sdv of the mean
#    print("For n = ",n,", the mean is ",mMean," +/-",mSdv_Mean,end = '\n\n')





