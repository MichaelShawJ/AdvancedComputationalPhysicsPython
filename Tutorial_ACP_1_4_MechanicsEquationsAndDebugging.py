#--------------------------------------------------------------------------------
# G e n e r a l   I n f o r m a t i o n
#--------------------------------------------------------------------------------
# Name: Michael J Shaw
# Usage: Learning to Debug using Newton's Mechanics Equations
#
# Description: This program has had intentional bugs placed in it,
#               I was tasked to remove the bugs so that it may run correctly.
#
# Inputs:      Initial positions (x,y), Velocities(x,y), Accelerations (x,y)
# Outputs:     A plot of the projectile motion of a particle/object
#
# Auxiliary Files: 
# Special Instructions: 
#
#--------------------------------------------------------------------------------
# CODE INFORMATION
#--------------------------------------------------------------------------------
#
# Author(s): Michael Shaw
# Modifications: Updated to Python 3
#
#--------------------------------------------------------------------------------

# Import Libraries
import matplotlib.pyplot as plt
import numpy as np

# Define the kinematic equation for one-dimensional motion
def mechanics_equations(x_initial, v_initial, time, acceleration):
    """Calculate position from initial conditions and time."""
    return x_initial + v_initial * time + 0.5 * acceleration * time**2

# Initialize variables for projectile motion
chart_title = "Projectile Motion"
horizontal_axis_title = "Distance (m)"
vertical_axis_title = "Height (m)"

# Initial conditions for the projectile
x_position_initial = 1.0  # initial x position in meters
x_velocity_initial = 70.0  # initial x velocity in m/s
x_acceleration = 0.0  # x acceleration in m/s^2 (assumed to be 0 for projectile motion)

y_position_initial = 0.0  # initial y position in meters
y_velocity_initial = 80.0  # initial y velocity in m/s
y_acceleration = -9.8  # y acceleration in m/s^2 (gravity)

# Time step for simulation
timestep_dt = 0.1  # time step in seconds
time_t = 0.0  # start time

# Lists to store position data at each time step
x_positions = []
y_positions = []

# Run the simulation until the projectile hits the ground
while True:
    x = mechanics_equations(x_position_initial, x_velocity_initial, time_t, x_acceleration)
    y = mechanics_equations(y_position_initial, y_velocity_initial, time_t, y_acceleration)
    
    if y < 0.0:
        break  # Stop the loop if the projectile hits the ground
    
    x_positions.append(x)
    y_positions.append(y)
    time_t += timestep_dt  # Increment time

# Define a function to plot the results
def plot_function(x_data, y_data, title, x_label, y_label):
    """Plot the projectile motion trajectory."""
    plt.plot(x_data, y_data)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.ylim(bottom=0.0, top=max(y_data) + 0.25 * max(y_data))  # Set y-axis limits
    plt.show()

# Call the plotting function with the simulation results
plot_function(x_positions, y_positions, chart_title, horizontal_axis_title, vertical_axis_title)