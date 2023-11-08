'''
Author: 
    Michael Shaw

Background: 
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

Usage:
    terminal/cmd: python Tutorial_ACP_OscilatingSystem_ODE_Solver_Euler_RK4.py
    Sypder: runfile('Tutorial_ACP_OscilatingSystem_ODE_Solver_Euler_RK4.py')
'''

# Import Libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

class OscSystem:
    def __init__(self, m, beta, k, g, w_ddot):
        self.m = m
        self.beta = beta
        self.k = k
        self.g = g
        self.w_ddot = w_ddot
    
    def system_of_equations(self, t, u):
        u0, u1 = u
        u2 = (self.w_ddot(t) + self.g - (self.beta / self.m) * u1 - (self.k / self.m) * u0)
        return [u1, u2]

def plot_results(time, numerical, exact, title, ylabel):
    plt.figure()
    plt.plot(time, numerical, 'r-', label='Numerical')
    plt.plot(time, exact, 'b--', label='Exact')
    plt.title(title)
    plt.legend()
    plt.xlabel('Time t')
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

def run_simulation(osc_system, initial_state, method, name, npoints_per_period, total_time):
    n_points = int(npoints_per_period * total_time / (2 * np.pi) + 1)
    t_eval = np.linspace(0, total_time, n_points)
    solution = solve_ivp(osc_system.system_of_equations, [0, total_time], initial_state, method=method, t_eval=t_eval)
    
    # Exact solutions
    exact_displacement = np.cos(solution.t)
    exact_velocity = -np.sin(solution.t)
    
    # Plot the results for displacement
    plot_results(solution.t, solution.y[0], exact_displacement, f'Displacement - {name}', 'Displacement u(t)')
    
    # Plot the results for velocity
    plot_results(solution.t, solution.y[1], exact_velocity, f'Velocity - {name}', 'Velocity u\'(t)')

def main():
    m = 1.0
    beta = 0.0
    k = 1.0
    g = 0.0
    w_ddot = lambda t: 0

    osc_system = OscSystem(m, beta, k, g, w_ddot)
    initial_state = [1.0, 0.0]  # [initial displacement, initial velocity]
    nperiods = 3.5
    total_time = 2 * np.pi * nperiods

    methods = [('RK23', 'Forward Euler', 200), ('RK45', 'Runge-Kutta 4', 20)]
    for method, name, npoints_per_period in methods:
        run_simulation(osc_system, initial_state, method, name, npoints_per_period, total_time)

if __name__ == '__main__':
    main()