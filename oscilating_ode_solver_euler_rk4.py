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
import argparse
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Exact solution based on the damping case
def exact_solution(t, m, beta, k, damping_case):
    omega_n = np.sqrt(k / m)
    zeta = beta / (2 * m * omega_n)

    if damping_case == "undamped":
        return np.cos(omega_n * t), -omega_n * np.sin(omega_n * t)
    elif damping_case == "underdamped":
        omega_d = omega_n * np.sqrt(1 - zeta ** 2)
        A = np.exp(-zeta * omega_n * t)
        return np.exp(-zeta * omega_n * t) * (np.cos(omega_d * t) + (omega_n * zeta / omega_d) * np.sin(omega_d * t)), -(omega_d**2 + omega_n**2 * zeta**2) * np.exp(-zeta * omega_n * t) * np.sin(omega_d * t) / omega_d
    elif damping_case == "critically_damped":
        A = np.exp(-omega_n * t)
        return (1 + omega_n * t) * A, -omega_n * (1 + omega_n * t) * A + omega_n * A
    elif damping_case == "overdamped":
        r1 = -omega_n * (zeta + np.sqrt(zeta ** 2 - 1))
        r2 = -omega_n * (zeta - np.sqrt(zeta ** 2 - 1))
        C1 = (r2 * 1) / (r2 - r1)
        C2 = (1 - C1)
        return C1 * np.exp(r1 * t) + C2 * np.exp(r2 * t), r1 * C1 * np.exp(r1 * t) + r2 * C2 * np.exp(r2 * t)
    else:
        raise ValueError("Invalid damping case. Choose 'undamped', 'underdamped', 'critically_damped', or 'overdamped'.")

class OscSystem:
    def __init__(self, m, beta, k, w_ddot):
        self.m = m
        self.beta = beta
        self.k = k
        self.w_ddot = w_ddot
    
    def system_of_equations(self, t, u):
        u0, u1 = u
        u2 = (self.w_ddot(t) - (self.beta / self.m) * u1 - (self.k / self.m) * u0)
        return [u1, u2]

def plot_results(time, numerical, exact, title, ylabel, damping_case):
    plt.figure()
    plt.plot(time, numerical, 'r-', label='Numerical')
    plt.plot(time, exact, 'b--', label='Exact')
    full_title = f"{title} - {damping_case.capitalize()}"
    plt.title(full_title)
    plt.legend()
    plt.xlabel('Time t')
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

def run_simulation(osc_system, initial_state, method, name, npoints_per_period, total_time, damping_case):
    n_points = int(npoints_per_period * total_time / (2 * np.pi) + 1)
    t_eval = np.linspace(0, total_time, n_points)
    solution = solve_ivp(osc_system.system_of_equations, [0, total_time], initial_state, method=method, t_eval=t_eval)

    # Calculate the exact solutions based on damping case
    exact_displacement, exact_velocity = exact_solution(solution.t, osc_system.m, osc_system.beta, osc_system.k, damping_case)
    
    # Plot the results for displacement
    plot_results(solution.t, solution.y[0], exact_displacement, f'Displacement - {name}', 'Displacement u(t)', damping_case)

    # Plot the results for velocity
    plot_results(solution.t, solution.y[1], exact_velocity, f'Velocity - {name}', 'Velocity u\'(t)', damping_case)

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description='Simulate an oscillating system using numerical methods.')
    parser.add_argument('--mass', type=float, default=1.0, help='Mass of the oscillator (default: 1.0)')
    parser.add_argument('--damping_case', type=str, default='undamped', choices=['undamped', 'underdamped', 'critically_damped', 'overdamped'], help='Damping case of the system (default: "undamped")')
    parser.add_argument('--spring_constant', type=float, default=1.0, help='Spring constant (default: 1.0)')
    parser.add_argument('--periods', type=float, default=3.5, help='Number of periods to simulate (default: 3.5)')
    
    # Parse arguments
    args = parser.parse_args()

    # Define beta values for each case
    beta_values = {
        "undamped": 0,
        "underdamped": 0.1,
        "critically_damped": 2,
        "overdamped": 3
    }
    
    # Define other Parameters
    beta = beta_values[args.damping_case]
    k = args.spring_constant
    m = args.mass
    w_ddot = lambda t: 0
    
    # Initialize the OscSystem instance
    osc_system = OscSystem(m, beta, k, w_ddot)
    initial_state = [1.0, 0.0]  # [initial displacement, initial velocity]
    total_time = 2 * np.pi * args.periods

     # Run the simulation for each specified numerical method
    methods = [('RK23', 'Forward Euler', 200), ('RK45', 'Runge-Kutta 4', 20)]
    for method, name, npoints_per_period in methods:
        run_simulation(osc_system, initial_state, method, name, npoints_per_period, total_time, args.damping_case)

if __name__ == '__main__':
    main()