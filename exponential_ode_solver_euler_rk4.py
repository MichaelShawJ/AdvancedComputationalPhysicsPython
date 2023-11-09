"""
Author: Michael Shaw

Background:
 The script solves the ODE u' = u (exponential growth) using numerical methods.
 It compares the Forward Euler method (mimicked by RK23) and the classical 
 Runge-Kutta 4 method (RK45) at various time steps and plots the solutions.

Usage:
    command line:
        python exponential_ode_solver_euler_rk4.py --T 3 --dt 0.1
    Spyder: 
        runfile('exponential_ode_solver_euler_rk4.py', args='--T 3 --dt 0.1')
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import argparse

def f(t, u):
    """Differential equation f(u, t) = u."""
    return u

def plot_solution(method, name, t_span, u0, t_eval):
    """Solves the ODE and plots the solution for a given method."""
    sol = solve_ivp(f, t_span, u0, method=method, t_eval=t_eval)
    plt.plot(sol.t, sol.y[0], label=name)

def main(T, dt):
    """Main function to run the simulations and create plots."""
    t_span = (0, T)
    u0 = [1.0]
    t_exact = np.linspace(0, T, 400)
    u_exact = np.exp(t_exact)
    
    # Plot the exact solution
    plt.figure()
    plt.plot(t_exact, u_exact, label='Exact Solution', linestyle='--')
    
    # Solve the ODE using Forward Euler method at different time steps
    for dt in [0.1, 0.5, 1.0]:
        n = int(round(T/dt))
        t_eval = np.linspace(0, T, n+1)
        plot_solution('RK23', f'Forward Euler, dt={dt}', t_span, u0, t_eval)

    # Adding title, legend, and labels for Forward Euler plot
    plt.title("Solution of u'=u with Forward Euler method")
    plt.xlabel('Time t')
    plt.ylabel('Solution u')
    plt.legend()
    plt.show()

    # Now for a comparison between Forward Euler and Runge-Kutta 4 (RK45)
    plt.figure()
    t_eval = np.linspace(0, T, int(round(T/dt)) + 1)
    
    # Solve and plot for both methods
    plot_solution('RK23', 'Forward Euler', t_span, u0, t_eval)
    plot_solution('RK45', 'Runge-Kutta 4', t_span, u0, t_eval)
    
    # Plot the exact solution
    plt.plot(t_exact, u_exact, label='Exact Solution', linestyle='--')

    # Adding title, legend, and labels for comparison plot
    plt.title("Comparison of Numerical Methods for u'=u")
    plt.xlabel('Time t')
    plt.ylabel('Solution u')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solve ODE u\'=u using numerical methods and plot the solutions.')
    parser.add_argument('--T', type=float, default=3, help='End time for the ODE solution.')
    parser.add_argument('--dt', type=float, default=0.1, help='Time step for the numerical solution.')
    
    args = parser.parse_args()
    
    main(args.T, args.dt)
