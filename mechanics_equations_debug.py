'''
Author: Michael Shaw

Background: 
    This program has had intentional bugs placed in it,
    I was tasked to remove the bugs so that it may run correctly.
    Inputs: Initial positions (x,y), Velocities(x,y), Accelerations (x,y)
    Outputs: A plot of the projectile motion of a particle/object

Usage and Test Case:
Terminal: python Tutorial_ACP_LogisticSystem_ODE_Solver_Euler_RK4.py
Spyder Console: runfile('Tutorial_ACP_LogisticSystem_ODE_Solver_Euler_RK4.py')
'''

# Import Libraries
import matplotlib.pyplot as plt
import numpy as np

def mechanics_equations(x_initial, v_initial, time, acceleration):
    """
    Calculate position from initial conditions and time using kinematic equations.

    :param x_initial: Initial position
    :param v_initial: Initial velocity
    :param time: Time elapsed
    :param acceleration: Constant acceleration
    :return: Position at given time
    """
    return x_initial + v_initial * time + 0.5 * acceleration * time ** 2

def calculate_trajectory(x_velocity_initial, y_velocity_initial, y_acceleration, timestep_dt):
    """
    Calculate the projectile motion trajectory using given initial conditions.

    :param x_velocity_initial: Initial horizontal velocity
    :param y_velocity_initial: Initial vertical velocity
    :param y_acceleration: Constant vertical acceleration (gravity)
    :param timestep_dt: Time step for simulation
    :return: Arrays of x and y positions
    """
    # Calculate total flight time until the projectile hits the ground
    flight_time = 2 * y_velocity_initial / -y_acceleration
    # Generate an array of time values from 0 to flight time
    time_values = np.arange(0, flight_time, timestep_dt)
    
    # Calculate x and y positions at each time step
    x_positions = mechanics_equations(x_position_initial, x_velocity_initial, time_values, x_acceleration)
    y_positions = mechanics_equations(y_position_initial, y_velocity_initial, time_values, y_acceleration)
    
    return x_positions, y_positions

def plot_trajectory(x_positions, y_positions, title, x_label, y_label):
    """
    Plot the projectile motion trajectory.

    :param x_positions: Horizontal positions
    :param y_positions: Vertical positions
    :param title: Chart title
    :param x_label: Label for the x-axis
    :param y_label: Label for the y-axis
    """
    plt.figure(figsize=(10, 5))
    plt.plot(x_positions, y_positions)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.ylim(bottom=0)  # Projectile cannot go below the ground
    plt.grid(True)
    plt.show()

def main():
    # Constants for the projectile motion
    global x_position_initial, x_velocity_initial, x_acceleration
    global y_position_initial, y_velocity_initial, y_acceleration
    global timestep_dt
    
    # Calculate the trajectory
    x_positions, y_positions = calculate_trajectory(x_velocity_initial, y_velocity_initial, y_acceleration, timestep_dt)
    
    # Plot the results
    plot_trajectory(x_positions, y_positions, chart_title, horizontal_axis_title, vertical_axis_title)

# Initial conditions for the projectile
x_position_initial = 0.0  # initial x position in meters
x_velocity_initial = 70.0  # initial x velocity in m/s
x_acceleration = 0.0      # x acceleration in m/s^2 (no horizontal acceleration in projectile motion)

y_position_initial = 0.0  # initial y position in meters
y_velocity_initial = 80.0  # initial y velocity in m/s
y_acceleration = -9.8     # y acceleration in m/s^2 (gravity)

timestep_dt = 0.1         # time step in seconds

chart_title = "Projectile Motion"
horizontal_axis_title = "Distance (m)"
vertical_axis_title = "Height (m)"

if __name__ == "__main__":
    main()
