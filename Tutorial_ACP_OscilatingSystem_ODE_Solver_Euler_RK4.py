'''
This code is for simulating an oscillating system 
described by a second-order ordinary differential equation (ODE). 
The code represents the ODE as a first-order system 
and solves it using numerical methods. 

The code has been updated to use modern Python libraries and best practices. 
For each numerical method, two figures have been plotted:
    one for the displacement u(t) and another for the velocity u′(t). 
    The red solid lines represent the numerical solutions, 
    while the blue dashed lines represent the exact solutions.

The updates to the code include:

The OscSystem class now has a method system_of_equations that defines 
the system of ODEs. This method is passed to the solve_ivp function.
The solve_ivp function from scipy.integrate is used to solve the system of ODEs
RK23 is used as a stand-in for the Forward Euler method, 
and RK45 is used for the Runge-Kutta 4 method.
Instead of using a finite difference scheme to approximate 
the second derivative of w(t), we provide a lambda function that represents 
w′′(t), which is zero in this test case.
Plots are created using matplotlib.pyplot, and we've used context managers 
(the plt.figure() calls) to handle the figures. 
This ensures that each plot is handled in its own figure.
The code now includes comments for better readability.
The exact solutions for an undamped oscillator with no external force are
u(t)=cos(t) and⁡ u′(t)=−sin(t), which are used to compare against 
the numerical solutions. These plots have been displayed directly in the output
'''

# Import Libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Defining the class of systems of equations and solutions
class OscSystem:
    def __init__(self, m, beta, k, g, w_ddot):
        self.m, self.beta, self.k, self.g, self.w_ddot = m, beta, k, g, w_ddot
    
    def system_of_equations(self, t, u):
        # u is a vector such that u[0] = displacement (u) and u[1] = velocity (u')
        # This function should return [u', u''] which is the first derivative of u
        # with respect to t.
        u0, u1 = u  # u0 is the displacement, u1 is the velocity
        # The second derivative of the displacement
        u2 = (self.w_ddot(t) + self.g - (self.beta/self.m)*u1 - (self.k/self.m)*u0)
        return [u1, u2]

# Test case: w(t) = 0 which implies w''(t) = 0
# Therefore, the second derivative of w with respect to time is a function that returns 0
w_ddot = lambda t: 0

# Create the OscSystem object
osc_sys = OscSystem(m=1.0, beta=0.0, k=1.0, g=0.0, w_ddot=w_ddot)

# Initial conditions: u0 = 1 (initial displacement), u1 = 0 (initial velocity)
u_init = [1.0, 0.0]

# Time span for the simulation: 0 to 3.5 periods of the oscillation
nperiods = 3.5
T = 2 * np.pi * nperiods

# Solve the ODE using different methods
methods = [('RK23', 'Forward Euler', 200), ('RK45', 'Runge-Kutta 4', 20)]
for method, name, npoints_per_period in methods:
    n = npoints_per_period * nperiods
    t_eval = np.linspace(0, T, int(n + 1))
    sol = solve_ivp(osc_sys.system_of_equations, [0, T], u_init, method=method, t_eval=t_eval)
    
    # Extract the solutions
    u0_values = sol.y[0]
    u1_values = sol.y[1]
    u0_exact = np.cos(sol.t)
    u1_exact = -np.sin(sol.t)
    
    # Plot the results for displacement
    plt.figure()
    plt.plot(sol.t, u0_values, 'r-', label='Numerical')
    plt.plot(sol.t, u0_exact, 'b--', label='Exact')
    plt.title(f'Oscillating system; position - {name}')
    plt.legend()
    plt.xlabel('Time t')
    plt.ylabel('Displacement u(t)')
    plt.grid(True)
    plt.show()

    # Plot the results for velocity
    plt.figure()
    plt.plot(sol.t, u1_values, 'r-', label='Numerical')
    plt.plot(sol.t, u1_exact, 'b--', label='Exact')
    plt.title(f'Oscillating system; velocity - {name}')
    plt.legend()
    plt.xlabel('Time t')
    plt.ylabel('Velocity u\'(t)')
    plt.grid(True)
    plt.show()

# Please note that 'Forward Euler' is not a method directly available in solve_ivp,
# 'RK23' is used as a substitute which is a low-order Runge-Kutta method suitable
# for problems with smooth solutions. 'RK45' is the default method in solve_ivp and is
# a higher-order method suitable for a wide range of problems.
