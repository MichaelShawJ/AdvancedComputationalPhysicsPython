
"""
AUTHOR: Michael Shaw
The Python code snippet provided is intended to simulate 
the trajectory of a ball using ordinary differential equations (ODEs).
The code has been successfully rewritten using modern 
Python libraries and best practices. 
In the plot displayed, the red line represents the numerical solution 
of the ball's trajectory, while the blue dashed line represents 
the exact analytical solution. The plot illustrates how the ball's trajectory 
progresses over time until it hits the ground.

Here are the changes made to the original code:

Replaced the ODESolver with scipy.integrate.solve_ivp, using the RK45 method 
which is more accurate and adaptable than the Forward Euler method.
Implemented numpy for array and mathematical operations and for generating 
the range of time points. Used matplotlib.pyplot to create the plot, which 
is the standard plotting library in modern Python. Added a termination event 
to the ODE solver that stops the integration once the ball hits the ground 
(when y≤0). Defined the exact solution for projectile motion without 
air resistance to compare with the numerical solution.
"""

#Import Libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the system of ODEs for the trajectory of a ball
def f(t, u):
    x, vx, y, vy = u
    g = 9.81  # Acceleration due to gravity
    return [vx, 0, vy, -g]

# Convert angle to radians
theta = np.radians(80)
v0 = 5

# Initial conditions: [x0, vx0, y0, vy0]
U0 = [0, v0*np.cos(theta), 0, v0*np.sin(theta)]

# Simulation time: from 0 to T with a time step of dt
T = 1.2
dt = 0.01
n = int(round(T/dt))
t_points = np.linspace(0, T, n+1)

# Termination condition for the simulation when the ball hits the ground (y=0)
def terminate(t, u):
    return u[2] >= 0

# Event that defines when the termination condition is True
terminate.terminal = True  # Stop the integration when the event is triggered
terminate.direction = -1   # The zero is approached from positive to negative

# Solve the ODE system using the RK45 method
sol = solve_ivp(f, [0, T], U0, method='RK45', t_eval=t_points, events=terminate)

# Extract the x and y values
x_values = sol.y[0]
y_values = sol.y[2]

# Define the exact solution for comparison (projectile motion without air resistance)
def exact(x):
    g = 9.81
    y0 = U0[2]  # Initial y position
    return x * np.tan(theta) - (g * x**2) / (2 * v0**2 * np.cos(theta)**2) + y0

# Plot the numerical and exact trajectories
plt.figure()
plt.plot(x_values, y_values, 'r', label='Numerical')
plt.plot(x_values, exact(x_values), 'b--', label='Exact')
plt.title(f'Ball trajectory (dt={dt})')
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.legend()
plt.grid(True)
plt.show()

# Save the plot to a file
plt.savefig('/mnt/data/tmp_ball.png')
