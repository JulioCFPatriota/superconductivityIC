#This code is referred to Runge-Kutta Method
#Modules
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

#Initial Parameters
m, k = 1, 1
x0, v0 = 1, 0
T = (2*np.pi)*np.sqrt(m/k)
t0, tf = 0, 3*T
t_eval = np.linspace(t0, tf, 1000)

#EDO system
def f(_t, y):
    x, v = y[0], y[1]
    fx = v
    fv = -(k/m) * x
    return fx, fv

#EDO solutions
solution = solve_ivp(
    fun=f,
    t_span=(t_eval[0], t_eval[-1]),
    y0=[x0, v0],
    t_eval=t_eval
)

#solve_ivp Data
t_sol = solution.t
x_sol = solution.y[0]
v_sol = solution.y[1]

#Momentum and Energy
p_sol = m * v_sol
E_sol = 0.5 * (m * (v_sol**2) + k * (x_sol**2))

#Figure with Graphs
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10))

#x vs t Graph
ax1.plot(t_sol, x_sol, 'k')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Position (m)')
ax1.grid(True)

#p vs x Graph
ax2.plot(x_sol, p_sol, 'k')
ax2.set_xlabel('Position (m)')
ax2.set_ylabel('Momentum (kg·m/s)')
ax2.set_aspect('equal')
ax2.grid(True)

#E vs t Graph
ax3.plot(t_sol, E_sol, 'k')
ax3.set_xlabel('Time (s)')
ax3.set_ylabel('Energy (J)')
ax3.grid(True)

#Plot
plt.tight_layout()
plt.show()
