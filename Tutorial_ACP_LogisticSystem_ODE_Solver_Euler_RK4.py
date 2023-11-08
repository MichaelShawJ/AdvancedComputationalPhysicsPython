'''
Author: Michael Shaw

Background: 
    This code snippet solves the scaled logistic equation using 
the Runge-Kutta 4 numerical method 
and then rescales the solution for different values of α.
 
1) The logistic_growth function defines the scaled logistic equation 
v'(t)=v(t)(1-v(t))
2) The solve_ivp function from scipy.integrate is used to solve this equation 
with an initial condition v_o over a range of τ from 0 to T, 
using the RK45 method (an adaptive Runge-Kutta method of order 4(5)).
3) The solution is plotted using matplotlib.pyplot, 
which shows the scaled population v over the scaled time τ.
4) A function u_and_t is defined to rescale v and τ 
for different α and R values, and the results are plotted in a second figure.
5) For both plots, labels, legends, and a grid have been added for clarity.
These plots display the dynamics of the scaled logistic equation 
and its rescaled versions for different values of α, 
illustrating how the population changes over time.

Usage and Test Case:
Terminal: python Tutorial_ACP_LogisticSystem_ODE_Solver_Euler_RK4.py
Spyder Console: runfile('Tutorial_ACP_LogisticSystem_ODE_Solver_Euler_RK4.py')
'''

#Import Libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def logistic_growth(t, population):
    """Scaled logistic growth function."""
    return population * (1 - population)

def plot_logistic_solution(time, solution, title, xlabel, ylabel):
    """Plot a given solution with appropriate labels and title."""
    plt.plot(time, solution, label='Scaled logistic equation')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_rescaled_solutions(time, solution, alphas, T, title, xlabel, ylabel):
    """Plot rescaled solutions for different alpha values."""
    plt.figure()
    for alpha in alphas:
        rescaled_time, rescaled_population = rescale_solution(solution, time, alpha, R=1)
        plt.plot(rescaled_time, rescaled_population, label=f'alpha={alpha}')

    plt.axis([0, T, 0, 1.1 * max(solution)])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()

def rescale_solution(population, time, alpha, R):
    """Rescale the solution for different alpha and R values."""
    return alpha * time, R * population

def main():
    # Initial conditions and parameters for the scaled logistic equation
    initial_population = 0.05
    total_time = 10
    time_points = np.linspace(0, total_time, 201)

    # Solve the scaled logistic equation using Runge-Kutta 4 method
    solution = solve_ivp(logistic_growth, [0, total_time], [initial_population], method='RK45', t_eval=time_points)

    # Plot the solution of the scaled logistic equation
    plot_logistic_solution(solution.t, solution.y[0], 'Scaled logistic equation', 'Scaled time \( \\tau \)', 'Scaled population \( v \)')

    # Plot rescaled solutions for different values of alpha
    alphas = np.linspace(0.2, 1, 5)
    plot_rescaled_solutions(solution.t, solution.y[0], alphas, total_time, 'Rescaled logistic equation for different alpha', 'Time t', 'Population u')

if __name__ == "__main__":
    main()