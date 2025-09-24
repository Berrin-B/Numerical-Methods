"""
eulers_method.py

This file demonstrates the application of Euler's method to solve
an initial value problem (IVP) numerically and compares the result
with the exact analytical solution.

Example application for an undergraduate Computational Physics course.
"""

import numpy as np
import matplotlib.pyplot as plt
import math


def f(x, u):
    """
    Differential equation du/dx = f(x, u).

    Parameters
    ----------
    x : float
        Independent variable.
    u : float
        Dependent variable.

    Returns
    -------
    float
        Derivative value f(x, u).
    """
    return (x**2) * math.exp(-u - 1)


def exact_solution(x):
    """
    Exact analytical solution for the given differential equation.

    Parameters
    ----------
    x : array_like or float
        Independent variable(s).

    Returns
    -------
    array_like or float
        Exact solution u(x).
    """
    return np.log((x**3) / (3 * math.e) + math.e)


def euler_method(func, a, b, u0, N):
    """
    Apply Euler's method to approximate the solution of an IVP.

    Parameters
    ----------
    func : callable
        Function representing du/dx = f(x, u).
    a, b : float
        Interval [a, b] for the independent variable x.
    u0 : float
        Initial condition u(a) = u0.
    N : int
        Number of steps.

    Returns
    -------
    x : ndarray
        Discretized values of the independent variable.
    u : ndarray
        Approximate solution values at each x.
    """
    h = (b - a) / N
    x = np.linspace(a, b, N + 1)
    u = np.zeros(N + 1)

    u[0] = u0
    for i in range(1, N + 1):
        u[i] = u[i - 1] + h * func(x[i - 1], u[i - 1])

    return x, u


if __name__ == "__main__":
    # Problem setup
    a, b = 0.0, 3.0
    N = 10
    u0 = 1.0

    # Numerical approximation with Euler's method
    x_vals, u_approx = euler_method(f, a, b, u0, N)

    # Exact solution
    u_exact = exact_solution(x_vals)

    # Plotting
    plt.plot(x_vals, u_approx, "o-", label="Euler approximation")
    plt.plot(x_vals, u_exact, "-", label="Exact solution")
    plt.title(f"Euler's Method, N={N}")
    plt.xlabel("x")
    plt.ylabel("u(x)")
    plt.legend(loc="best")
    plt.grid(True)
    plt.show()


