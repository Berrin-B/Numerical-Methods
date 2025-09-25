"""
fourth_order_runge_kutta.py

This file demonstrates solving an initial value problem (IVP) using
the fourth-order Runge-Kutta method and compares the result with
the exact analytical solution.

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
    Exact analytical solution for the differential equation.

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


def runge_kutta_4(func, a, b, u0, N):
    """
    Solve an IVP using the fourth-order Runge-Kutta method.

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
        k1 = func(x[i - 1], u[i - 1])
        k2 = func(x[i - 1] + 0.5 * h, u[i - 1] + 0.5 * k1 * h)
        k3 = func(x[i - 1] + 0.5 * h, u[i - 1] + 0.5 * k2 * h)
        k4 = func(x[i - 1] + h, u[i - 1] + k3 * h)
        u[i] = u[i - 1] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

    return x, u


if __name__ == "__main__":
    # Problem setup
    a, b = 0.0, 3.0
    N = 10
    u0 = 1.0

    # Runge-Kutta approximation
    x_vals, u_approx = runge_kutta_4(f, a, b, u0, N)

    # Exact solution
    u_exact = exact_solution(x_vals)

    # Plotting
    plt.plot(x_vals, u_approx, "o-", label="Runge-Kutta 4th order approximation")
    plt.plot(x_vals, u_exact, "-", label="Exact solution")
    plt.title("Fourth Order Runge-Kutta Method, h={:.3f}".format((b - a) / N))
    plt.xlabel("x")
    plt.ylabel("u(x)")
    plt.legend(loc="best")
    plt.grid(True)
    plt.show()
