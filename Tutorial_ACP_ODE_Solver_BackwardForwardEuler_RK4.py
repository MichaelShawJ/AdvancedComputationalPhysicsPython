
"""
Author: Michael Shaw
This is an updated ODE solver comparing Runga-Kutta 4, Backward and Forward Euler
with Newton's approximations.

This script solves the differential equation dt/du=−u 
with the initial condition u(0)=1, which has an exact solution
u(t)=e^−t. It compares the maximum error of each method against 
the exact solution over the interval[0,5]. 
The Newton function provided is a simple implementation for the 
BackwardEuler class and may need to be adapted if the actual ODE 
requires a more robust or specific approach. You would need to run this 
script in an environment where scipy is installed to use solve_ivp. 
The Newton function here is a placeholder; if you have a specific 
implementation, especially for vectorized functions or more complex ODEs, 
you should use that instead.
"""

import numpy as np
from scipy.integrate import solve_ivp

class ODESolver:
    """
    Superclass for numerical methods solving scalar and vector ODEs.
    """
    def __init__(self, f):
        if not callable(f):
            raise TypeError(f'f is {type(f)}, not a function')
        self.f = lambda u, t: np.asarray(f(u, t), float)

    def advance(self):
        raise NotImplementedError

    def set_initial_condition(self, U0):
        if isinstance(U0, (float, int)):
            self.neq = 1
            U0 = float(U0)
        else:
            U0 = np.asarray(U0)
            self.neq = U0.size
        self.U0 = U0

    def solve(self, time_points, terminate=None):
        if terminate is None:
            terminate = lambda u, t, step_no: False
        if isinstance(time_points, (float, int)):
            raise TypeError('solve: time_points is not a sequence')
        
        self.t = np.asarray(time_points)
        n = self.t.size
        self.u = np.zeros((n, self.neq)) if self.neq > 1 else np.zeros(n)
        self.u[0] = self.U0
        
        for k in range(n-1):
            self.k = k
            self.u[k+1] = self.advance()
            if terminate(self.u, self.t, self.k+1):
                break
        return self.u, self.t

class ForwardEuler(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        return u[k] + dt * f(u[k], t[k])

class RungeKutta4(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        dt2 = dt / 2.0
        K1 = dt * f(u[k], t[k])
        K2 = dt * f(u[k] + 0.5 * K1, t[k] + dt2)
        K3 = dt * f(u[k] + 0.5 * K2, t[k] + dt2)
        K4 = dt * f(u[k] + K3, t[k] + dt)
        return u[k] + (1/6.0) * (K1 + 2 * K2 + 2 * K3 + K4)

class BackwardEuler(ODESolver):
    def __init__(self, f):
        super().__init__(f)
        try:
            u = np.array([1])
            t = 1
            value = f(u, t)
        except IndexError:
            raise ValueError('f(u,t) must return float/int')

    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        
        def F(w):
            return w - dt * f(w, t[k+1]) - u[k]

        dFdw = Derivative(F)
        w_start = u[k] + dt * f(u[k], t[k])  # Forward Euler step
        unew, n, F_value = Newton(F, w_start, dFdw, 30)
        if k == 0:
            self.Newton_iter = []
        self.Newton_iter.append(n)
        if n >= 30:
            print(f"Newton's failed to converge at t={t[k+1]} ({n} iterations)")
        return unew

class Derivative:
    def __init__(self, f, h=1E-9):
        self.f = f
        self.h = float(h)

    def __call__(self, x):
        return (self.f(x+self.h) - self.f(x-self.h)) / (2*self.h)

# Simple Newton's method implementation for demonstration
def Newton(F, x0, F_derivative, tol=1e-10, max_iter=30):
    x = x0
    for i in range(max_iter):
        F_value = F(x)
        F_derivative_value = F_derivative(x)
        if abs(F_value) < tol:
            return x, i, F_value  # Converged
        if F_derivative_value == 0:
            raise RuntimeError("Newton's method failed: derivative is zero.")
        dx = F_value / F_derivative_value
        x = x - dx
    raise RuntimeError("Newton's method failed to converge.")

# Example ODE: du/dt = -u, with analytical solution u(t) = exp(-t)
def f_example(u, t):
    return -u

def u_exact(t):
    return np.exp(-t)

# Set up the problem
U0 = 1
T = 5
n = 100
t_points = np.linspace(0, T, n)

# Solve with our solvers
methods = [ForwardEuler, RungeKutta4, BackwardEuler]
solutions = {}

for method_class in methods:
    method = method_class(f_example)
    method.set_initial_condition(U0)
    u, t = method.solve(t_points)
    solutions[method_class.__name__] = u

# Solve with solve_ivp
sol = solve_ivp(f_example, [0, T], [U0], t_eval=t_points, method='RK45')

# Compare solutions
print("Method\t\tMax Error")
for method_name, u in solutions.items():
    error = np.max(np.abs(u - u_exact(t_points)))
    print(f"{method_name}\t{error:.2e}")

# For solve_ivp (using RK45, which is similar to RungeKutta4)
error_ivp = np.max(np.abs(sol.y[0] - u_exact(t_points)))
print(f"solve_ivp (RK45)\t{error_ivp:.2e}")
