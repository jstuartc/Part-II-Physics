import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from numpy import pi

def Cfunction (x):
    return (np.cos((pi/2)*x**2))

def Sfunction (x):
    return (np.sin((pi/2)*x**2))


u_values = np.arange(-999,1000)
dt = 0.01

C_values = np.empty(2000,dtype= tuple)
S_values = np.empty(2000,dtype= tuple)
for u in u_values:
    S_values[u] = integrate.quad(Sfunction,0,u*dt,limit=100)[0]
    C_values[u] = integrate.quad(Cfunction,0,u*dt,limit=100)[0]
    
plt.plot(C_values,S_values)
plt.ylabel("y")
plt.xlabel("x")
plt.title("Cornu Spiral")
plt.ylim(bottom=-1.0,top=1.0)
plt.xlim(left=-1.0,right=1.0)
plt.show()


   