#This code is referred to Verlet Method
#Modules
import numpy as np
import matplotlib.pyplot as plt

#Initial Parameters
m, k = 1, 1
x0, v0 = 1, 0
a0 = -(k/m) * x0
T = (2*np.pi)*np.sqrt(m/k)
t0, dt, tf = 0, 0.01, 3*T

#Range vector N
N = int(tf/dt)
t = np.linspace(t0, tf, N)

#Initial Vectors
x = np.zeros(N)
v = np.zeros(N)
a = np.zeros(N)

#Initial Conditions
x[0], v[0], a[0] = x0, v0, a0

#Verlet
for i in range(N-1):
    x[i+1] = x[i] + v[i]*dt + 0.5*a[i]*(dt**2)
    a[i+1] = -(k/m)*x[i+1]
    v[i+1] = v[i] + 0.5*(a[i]+a[i+1])*dt

#Figure with Graphs
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10))

#x vs t Graph
ax1.plot(t, x, 'k')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Position (m)')
ax1.grid(True)

#p vs x Graph
p = m * v
ax2.plot(x, p, 'k')
ax2.set_xlabel('Position (m)')
ax2.set_ylabel('Momentum (kg·m/s)')
ax2.set_aspect('equal')
ax2.grid(True)

#E vs t Graph
E = 0.5*(m*(v**2)+k*(x**2))
ax3.plot(t, E, 'k')
ax3.set_xlabel('Time (s)')
ax3.set_ylabel('Energy (J)')
ax3.grid(True)

#Plot
plt.tight_layout()
plt.show()