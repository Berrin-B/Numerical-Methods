"""
second_order_runge_kutta.py

This file demonstrates solving an initial value problem (IVP) using
the second-order Runge-Kutta method and compares the approximate solution.

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


def runge_kutta_2(func, a, b, u0, N, alpha=1.0):
    """
    Solve an IVP using the second-order Runge-Kutta method.

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
    alpha : float, optional
        Parameter for the method (default 1.0).

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
        k1 = h * func(x[i - 1], u[i - 1])
        k2 = h * func(x[i - 1] + alpha * h, u[i - 1] + alpha * k1)
        u[i] = u[i - 1] + (1 - 1 / (2 * alpha)) * k1 + (k2 / (2 * alpha))

    return x, u


if __name__ == "__main__":
    # Problem setup
    a, b = 0.0, 3.0
    N = 300
    u0 = 1.0
    alpha = 1.0

    # RK2 approximation
    x_vals, u_approx = runge_kutta_2(f, a, b, u0, N, alpha)

    # Plotting
    plt.plot(x_vals, u_approx, label="Second-order Runge-Kutta approximation")
    plt.title(f"Second Order Runge-Kutta Method, h={(b-a)/N:.5f}, alpha={alpha}")
    plt.xlabel("x")
    plt.ylabel("u(x)")
    plt.legend(loc="best")
    plt.grid(True)
    plt.show()
