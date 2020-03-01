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

C_values = np.empty(2000)
S_values = np.empty(2000)
for u in u_values:
    S_values[u] = integrate.quad(Sfunction,0,u*dt,limit=100)[0]
    C_values[u] = integrate.quad(Cfunction,0,u*dt,limit=100)[0]

v_range = np.arange(-500,499)
#Slit width 0.1m, λ=0.01m
#Phase of the graph
phase = np.empty(1000)
#Distance = 0.3m, therefore Δu = 2.58, therefore list umax - umin = 258
intensity_30 = np.empty(1000)
#Distance = 0.5m, therefore Δu = 2, therefore list umax - umin = 200
intensity_50 = np.empty(1000)
#Distance = 1m, therefore Δu = 1.414, therefore list umax - umin = 141.4 ~142
intensity_100 = np.empty(1000)

for v in v_range:
    phase[v]=v/100
    intensity_30[v]= ((C_values[v+129]-C_values[v-129])**2+(S_values[v+129]-S_values[v-129])**2)/2
    intensity_50[v]= ((C_values[v+100]-C_values[v-100])**2+(S_values[v+100]-S_values[v-100])**2)/2
    intensity_100[v]= ((C_values[v+71]-C_values[v-71])**2+(S_values[v+71]-S_values[v-71])**2)/2


plt.plot(phase,intensity_30,label="0.3m")
plt.plot(phase,intensity_50,label="0.5m")
plt.plot(phase,intensity_100,label="1m")
plt.legend()
plt.xlabel("Phase")
plt.ylabel("Intensity")
plt.ylim(bottom=0)
plt.title("Relative Intensity against Phase")
plt.savefig("Intensity-Phase.png",bbox_inches='tight')
