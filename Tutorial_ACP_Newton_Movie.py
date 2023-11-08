"""
Author: Michael Shaw

This is a program for illustrating the convergence of Newton's method
for solving nonlinear algebraic equations of the form f(x) = 0. 
It outputs a gif of the solution into the directory

Usage:
terminal/cmd: python Newton_movie.py f_formula df_formula x0 xmin xmax
Sypder: runfile('Tutorial_ACP_Newton_Movie.py', args='f_formula df_formula x0 xmin xmax')
!Test Case: runfile('Tutorial_ACP_Newton_Movie.py', args='"x**2 - 2" "2*x" 1 -2 2')

where f_formula is a string formula for f(x); df_formula is
a string formula for the derivative f'(x), or df_formula can
be the string 'numeric', which implies that f'(x) is computed
numerically; x0 is the initial guess of the root; and the
x axis in the plot has extent [xmin, xmax].

A classic example to illustrate Newton's method is finding the roots 
of the polynomial function f(x)=x^2 −2, which has the roots ±sqrt(2)
The derivative f′(x)=2x.

Here are the corresponding formulas that you can use as command-line arguments:
f_formula: "x**2 - 2", df_formula: "2*x", For the initial guess (x0), 
you might typically start with a value of 1 or -1, depending on which root 
you are interested in finding. Since sqrt(2) is approximately 1.414, 
starting with 1 should converge to the positive root.

For the xmin and xmax, you could choose values that allow you to see the 
behavior of the function around the root, such as -2 and 2.
"""
# from Newton import Newton
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import argparse

# Define command-line argument parsing
parser = argparse.ArgumentParser(description="Illustrate Newton's method convergence.")
parser.add_argument('f_formula', type=str, help='String formula for f(x)')
parser.add_argument('df_formula', type=str, help='String formula for f\'(x) or "numeric" for numerical derivative')
parser.add_argument('x0', type=float, help='Initial guess for the root')
parser.add_argument('xmin', type=float, help='Minimum x-axis value')
parser.add_argument('xmax', type=float, help='Maximum x-axis value')
args = parser.parse_args()

# Define the function and its derivative
def f(x):
    return eval(args.f_formula)

def df(x):
    if args.df_formula == 'numeric':
        h = 1.0E-7
        return (f(x+h) - f(x-h)) / (2*h)
    else:
        return eval(args.df_formula)

# Implement Newton's method
def newton(f, df, x0, tol=1e-7, max_iter=100):
    x = x0
    for i in range(max_iter):
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < tol:
            return x_new, i + 1  # Return the root and the number of iterations
        x = x_new
    return x, max_iter

# Perform Newton's method
root, iterations = newton(f, df, args.x0)
print(f"Root: {root} found in {iterations} iterations")

# Visualization
fig, ax = plt.subplots()

# Plotting function
x_vals = np.linspace(args.xmin, args.xmax, 400)
y_vals = f(x_vals)
ax.plot(x_vals, y_vals, label='f(x)')

# Initialize the tangent line and root approximation line
tangent_line, = ax.plot([], [], 'b-', label='Tangent')
root_line, = ax.plot([], [], 'g-', label='Approximate Root')

# Update function for the animation
def update(frame):
    x = frame
    y = f(x)
    dydx = df(x)
    tangent_line.set_data([x - y/dydx, x + y/dydx], [0, 2*y])
    root_line.set_data([x, x], [0, y])
    return tangent_line, root_line

# Create the animation
ani = FuncAnimation(fig, update, frames=np.linspace(args.x0, root, 100), blit=True)
plt.legend()
plt.show()

# Save the animation
ani.save('newton_convergence.gif', writer='imagemagick', fps=10)
