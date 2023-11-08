'''
Author: Michael Shaw

Background:This python script implements the Newton-Raphson method 
for finding the root of a function, 
with a specific test function and its derivative. 
The _test function also provides a simple command-line interface 
and visualization of the function and the root-finding process.

Usage and Test Case: 
    Terminal: python Tutorial_ACP_Newton.py arg
    Spyder Console: runfile('Tutorial_ACP_Newton.py', args='1.9')
'''

# Import Libraries
import numpy as np
import matplotlib.pyplot as plt
import argparse

def Newton(f, x, dfdx, epsilon=1.0E-7, N=100, store=False):
    """
    Perform the Newton-Raphson method for finding the root of a function.

    :param f: The function for which the root is to be found.
    :param x: The initial guess for the root.
    :param dfdx: The derivative of the function f.
    :param epsilon: The tolerance for the root's accuracy.
    :param N: The maximum number of iterations to perform.
    :param store: Boolean indicating whether to store the intermediate results.
    :return: The root of the function, and optionally the intermediate results.
    """
    f_value = f(x)
    n = 0
    info = [(x, f_value)] if store else None
    while abs(f_value) > epsilon and n <= N:
        dfdx_value = float(dfdx(x))
        if abs(dfdx_value) < 1E-14:
            raise ValueError(f"Newton: f'({x:g}) is too close to zero")

        x = x - f_value / dfdx_value
        f_value = f(x)
        n += 1
        if store:
            info.append((x, f_value))

    return (x, info) if store else (x, n, f_value)

def test_function(x):
    return np.exp(-0.1 * x**2) * np.sin(np.pi / 2 * x)

def derivative_test_function(x):
    return -0.1 * 2 * x * np.exp(-0.1 * x**2) * np.sin(np.pi / 2 * x) + \
           np.pi / 2 * np.exp(-0.1 * x**2) * np.cos(np.pi / 2 * x)

def test_Newton_method(initial_guess):
    root, info = Newton(test_function, initial_guess, derivative_test_function, store=True)
    print(f'Root: {root:.16g}')
    for i, (xi, fi) in enumerate(info):
        print(f'Iteration {i:2d}: f({xi:g})={fi:g}')

    # Plot the function and its root
    x = np.linspace(-7, 7, 401)
    y = test_function(x)
    plt.plot(x, y, label='g(x)')
    plt.plot(root, test_function(root), 'ro', label='Root')
    plt.grid(True)
    plt.title("Function and its root found by Newton's method")
    plt.xlabel('x')
    plt.ylabel('g(x)')
    plt.legend()
    plt.show()

# Set up command-line argument parsing
parser = argparse.ArgumentParser(description="Find the root of a function using Newton's method.")
parser.add_argument('initial_guess', type=float, help='Initial guess for the root of the function')
args = parser.parse_args()

if __name__ == '__main__':
    test_Newton_method(args.initial_guess)
