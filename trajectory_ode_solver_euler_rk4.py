
"""
AUTHOR: 
    Michael Shaw
Background:
    The Python code snippet provided is intended to simulate 
the trajectory of a ball using ordinary differential equations (ODEs).
The code has been rewritten using modern Python libraries and best practices. 
In the plot displayed, the red line represents the numerical solution 
of the ball's trajectory, while the blue dashed line represents 
the exact analytical solution. The plot illustrates how the ball's trajectory 
progresses over time until it hits the ground.

Usage:
    Command Line: python trajectory_ode_solver_euler_rk4.py --theta 45 --v0 10 --T 2 --dt 0.05
    Spyder: runfile('trajectory_ode_solver_euler_rk4.py', args='--theta 45 --v0 10 --T 2 --dt 0.05')
"""
import argparse
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def trajectory_ode_system(t, u):
    """
    Define the system of ODEs for the trajectory of a ball.
    
    Args:
        t (float): Current time.
        u (list): List containing the current position and velocity in x and y.

    Returns:
        list: Derivatives of the position and velocity in x and y.
    """
    x, vx, y, vy = u
    g = 9.81  # Acceleration due to gravity in m/s^2
    return [vx, 0, vy, -g]

def terminate_event(t, u):
    """
    Termination condition for the simulation when the ball hits the ground (y=0).
    
    Args:
        t (float): Current time.
        u (list): List containing the current position and velocity in x and y.

    Returns:
        float: Height above the ground, the integration stops when this is zero.
    """
    return u[2]

# Set the event to stop integration when the termination condition is met
terminate_event.terminal = True
terminate_event.direction = -1

def exact_solution(x, theta, v0):
    """
    Define the exact solution for projectile motion without air resistance.
    
    Args:
        x (array_like): Range of x positions at which to evaluate the exact solution.
        theta (float): Launch angle in radians.
        v0 (float): Initial velocity in m/s.

    Returns:
        numpy.ndarray: The exact y values at each x position.
    """
    g = 9.81  # Acceleration due to gravity in m/s^2
    y0 = 0  # Initial y position
    return x * np.tan(theta) - (g * x**2) / (2 * v0**2 * np.cos(theta)**2) + y0

def plot_trajectory(x_values, y_values, theta, v0):
    """
    Plot the numerical and exact trajectories of the ball.
    
    Args:
        x_values (array_like): X values from the numerical solution.
        y_values (array_like): Y values from the numerical solution.
        theta (float): Launch angle in radians.
        v0 (float): Initial velocity in m/s.
    """
    plt.figure()
    plt.plot(x_values, y_values, 'r', label='Numerical')
    plt.plot(x_values, exact_solution(x_values, theta, v0), 'b--', label='Exact')
    plt.title('Ball trajectory')
    plt.xlabel('Distance (m)')
    plt.ylabel('Height (m)')
    plt.legend()
    plt.grid(True)
    plt.savefig('trajectory_ode.png')
    plt.show()

def main(theta_degrees=80, v0=5, T=1.2, dt=0.01):
    """
    Main function to execute the ball trajectory simulation and plotting.

    Args:
        theta_degrees (float): Launch angle in degrees.
        v0 (float): Initial velocity in m/s.
        T (float): Total simulation time in seconds.
        dt (float): Time step for the simulation in seconds.
    """
    # Convert angle to radians
    theta = np.radians(theta_degrees)

    # Initial conditions: [x0, vx0, y0, vy0]
    U0 = [0, v0 * np.cos(theta), 0, v0 * np.sin(theta)]

    # Simulation time: from 0 to T with a time step of dt
    n = int(round(T / dt))
    t_points = np.linspace(0, T, n + 1)

    # Solve the ODE system using the RK45 method
    sol = solve_ivp(trajectory_ode_system, [0, T], U0, method='RK45', t_eval=t_points, events=terminate_event)

    # Extract the x and y values
    x_values = sol.y[0]
    y_values = sol.y[2]

    # Plot the numerical and exact trajectories
    plot_trajectory(x_values, y_values, theta, v0)

# Check if the script is being run directly (and not being imported)
if __name__ == '__main__':
    # These default arguments can be replaced by command-line arguments if needed
    parser = argparse.ArgumentParser(description='Simulate and plot the trajectory of a ball.')
    parser.add_argument('--theta', type=float, default=80, help='Launch angle in degrees.')
    parser.add_argument('--v0', type=float, default=5, help='Initial velocity in m/s.')
    parser.add_argument('--T', type=float, default=1.2, help='Total simulation time in seconds.')
    parser.add_argument('--dt', type=float, default=0.01, help='Time step for the simulation in seconds.')
   
    args = parser.parse_args()
   
    main(theta_degrees=args.theta, v0=args.v0, T=args.T, dt=args.dt)
