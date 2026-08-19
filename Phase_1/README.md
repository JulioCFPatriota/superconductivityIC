# First Exercise (Program)
## Verlet Method and Runge-Kutta

### The assigned exercise consists in a program that will solve the harmonic oscillator using Python as script language.<br /> <br />1. Implementing Verlet method in Python<br />2. Implementing Runge-Kutta method through solve_ivp function, from SciPy library.

### The analytic solution

Starting from Hamilton's Principle,

$$L\left(x_{i}, \dot{x_{i}}\right) \equiv T\left(\dot{x_{i}}\right) - U\left(x_{i}\right),$$

where T represents the kinetic energy, and U is the potential energy.

In the case of a harmonic oscillator, and knowing the force in a spring-mass system without damping force -- which results in a simple harmonic oscillator -- is possible to admit that:

$$U(x) \coloneqq - \int{F(x)dx},$$

from Hooke's Law

$$F(x)=-kx\Rightarrow U=\int{kxdx}$$<br />
$$\therefore U=k\cdot \frac{x^{2}}{2},$$

and, for the kinetic energy,

$$T\coloneqq m\cdot \frac{v^{2}}{2}, \hspace{1em} v^{2}\coloneqq \dot{x}$$<br />
$$\therefore T=m\cdot \frac{x^{2}}{2}.$$

In this manner,

$$L=m\cdot\frac{\dot{x^{2}}}{2}-k\cdot\frac{x^{2}}{2}.$$

From 7.3 equation (Thorton & Marion, 2011),

$$L\left( x_{i}, \dot{x_{i}}\right) , \hspace{1em} x_{i}=x_{i}(t), \hspace{1em} \dot{x_{i}}=\dot{x_{i}}(t)$$<br />
$$\therefore L \left\\{ x_{i}, \dot{x_{i}}; t \right\\} \rightarrow f \left\\{ x_{i}, \dot{x_{i}}; t \right\\}$$
$$\Rightarrow \delta \int_{t_{1}}^{t_{2}}{L\left(x_{i}, \dot{x_{i}}\right)dt}=0$$

which can be solved through Euler's equation, in this case, Euler-Lagrange. Solving through Euler-Lagrange

$$\frac{\partial L}{\partial x} - \frac{d}{dt} \frac{\partial L}{\partial \dot{x}} =0.$$

And then

$$\frac{\partial L}{\partial x} = -kx, $$<br />
$$\frac{\partial L}{\partial \dot{x}} = m\dot{x} \Rightarrow \frac{d}{dt}\frac{\partial L}{\partial \dot{x}} = m\ddot{x}$$<br />
$$\therefore \frac{\partial L}{\partial x} - \frac{\partial L}{\partial \dot{x}} = - kx - m\ddot{x} = 0$$<br />
$$\Rightarrow \ddot{x}=-\frac{k}{m}x.$$

Through EDO solving methods, in this particular case, using the ansatz $x(t)=e^{rt}$, is easy to obtain the analytic solution:

$$\boxed{x(t) = x_{0}cos(\omega_{0}t) + \frac{v_{0}}{\omega_{0}}sen(\omega_{0}t)},$$<br />

where $\omega_{0}$ is the oscillator's natural frequency defined by 

$$ \omega_{0} = \sqrt{\frac{k}{m}}. $$

### Verlet Method

For this method, in the **[Verlet program](https://github.com/JulioCFPatriota/superconductivityIC/blob/main/Phase_1/oh_verlet.py)**, a _for_ lace was created to implement the Verlet integration method
```
#Verlet
for i in range(N-1):
    x[i+1] = x[i] + v[i]*dt + 0.5*a[i]*(dt**2)
    a[i+1] = -(k/m)*x[i+1]
    v[i+1] = v[i] + 0.5*(a[i]+a[i+1])*dt
```
where every _i_ iteration had a small incremental step of $dt=0.01$.

![Verlet Preview](https://github.com/JulioCFPatriota/superconductivityIC/blob/main/Phase_1/verletMethod.png)

### Runge-Kutta (solve_ivp)

In this method, the **[Runge-Kutta program](https://github.com/JulioCFPatriota/superconductivityIC/blob/main/Phase_1/oh_rk45.py)** used the function _"solve initial value problem"_, or _solve_ivp_ function, from **SciPy**'s library. With this approximation, the method needs three more steps: defining the function containing the EDO system that will be solved;
```
#EDO system
def f(_t, y):
    x, v = y[0], y[1]
    fx = v
    fv = -(k/m) * x
    return fx, fv
```
inserting the solutions inside _solve_ivp_;
```
#EDO solutions
solution = solve_ivp(
    fun=f,
    t_span=(t_eval[0], t_eval[-1]),
    y0=[x0, v0],
    t_eval=t_eval
)
```
and finally getting the data and placing it in their respective vector.
```
#solve_ivp Data
t_sol = solution.t
x_sol = solution.y[0]
v_sol = solution.y[1]
```

![RK45 Preview](https://github.com/JulioCFPatriota/superconductivityIC/blob/main/Phase_1/solveivpRK45Method.png)
