# First Exercise (Program)
## Verlet Method and Runge-Kutta

### The assigned exercise consists in a program that will solve the harmonic oscillator using Python as script language.<br /> <br />1. Implementing Verlet method in Python<br />2. Implementing Runge-Kutta method through solve_ivp function, from SciPy library.

### Solution

Starting from Hamilton's Principle,

$L\left(x_{i}, \dot{x_{i}}\right) \equiv T\left(\dot{x_{i}}\right) - U\left(x_{i}\right),$

where T represents the kinetic energy, and U is the potential energy.

In the case of a harmonic oscillator, and knowing the force in a spring-mass system without damping force -- which results in a simple harmonic oscillator -- is possible to admit that:

$U(x) \coloneqq - \int{F(x)dx},$

from Hooke's Law

$F(x)=-kx\Rightarrow U=\int{kxdx}$<br />
$\therefore U=k\cdot \frac{x^{2}}{2},$

and, for the kinetic energy,

$T\coloneqq m\cdot \frac{v^{2}}{2}, \hspace{1em} v^{2}\coloneqq \dot{x}$<br />
$\therefore T=m\cdot \frac{x^{2}}{2}.$

In this manner,

$L=m\cdot\frac{\dot{x^{2}}}{2}-k\cdot\frac{x^{2}}{2}.$

From 7.3 equation (Thorton & Marion, 2011),

$L\left( x_{i}, \dot{x_{i}}\right) , \hspace{1em} x_{i}=x_{i}(t), \hspace{1em} \dot{x_{i}}=\dot{x_{i}}(t)$<br />
$\therefore L \left\{ x_{i}, \dot{x_{i}}; t \right\} \rightarrow f \left\{ x_{i}, \dot{x_{i}}; t \right\}$
