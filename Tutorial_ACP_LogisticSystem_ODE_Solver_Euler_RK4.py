'''
Author: Michael Shaw

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
'''

#Import Libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the logistic growth function
def logistic_growth(tau, v):
    return v * (1 - v)

# Initial conditions and parameters
v0 = 0.05
dtau = 0.05
T = 10
n = int(round(T / dtau))
t_points = np.linspace(0, T, n + 1)

# Solve the scaled logistic equation using Runge-Kutta 4 method (RK45 in solve_ivp)
sol = solve_ivp(logistic_growth, [0, T], [v0], method='RK45', t_eval=t_points)

# Plot the solution of the scaled logistic equation
plt.figure()
plt.plot(sol.t, sol.y[0], label='Scaled logistic equation')
plt.title('Scaled logistic equation')
plt.xlabel('Scaled time \( \\tau \)')
plt.ylabel('Scaled population \( v \)')
plt.legend()
plt.grid(True)
plt.show()

# Function to rescale v and tau for different alpha and R values
def u_and_t(v, tau, alpha, R):
    return alpha * tau, R * v

# Create a new figure for the rescaled solutions
plt.figure()

# Plot rescaled solutions for different values of alpha
alphas = np.linspace(0.2, 1, 5)
for alpha in alphas:
    t, u = u_and_t(sol.y[0], sol.t, alpha, R=1)
    plt.plot(t, u, label=f'alpha={alpha}')

# Set plot limits and labels
plt.axis([0, T, 0, 1.1])
plt.title('Rescaled logistic equation for different alpha')
plt.xlabel('Time t')
plt.ylabel('Population u')
plt.legend()
plt.grid(True)
plt.show()
