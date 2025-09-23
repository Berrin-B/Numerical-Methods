"""
derivative_estimation.py

This file estimates the derivative of a function at a given point
using Richardson extrapolation (Romberg-style scheme).

Example application for an undergraduate Computational Physics course.
"""

import math


def derivative_estimation(func, x, h=0.1, N=5):
    """
    Estimate the derivative of a function f at point x using Richardson extrapolation.

    Parameters
    ----------
    func : callable
        Function to differentiate.
    x : float
        Point at which to estimate the derivative.
    h : float, optional
        Initial step size. Default is 0.1.
    N : int, optional
        Number of extrapolation levels. Default is 5.

    Returns
    -------
    float
        Estimated derivative of f at x.
    """
    # Romberg-style table initialization
    D = [[0.0 for _ in range(N + 1)] for _ in range(N + 1)]

    # First column: central difference approximations
    step = h
    for i in range(N + 1):
        D[i][0] = (func(x + step) - func(x - step)) / (2 * step)
        step /= 2  # halve step size at each iteration

    # Richardson extrapolation for higher orders
    for j in range(1, N + 1):
        for i in range(j, N + 1):
            D[i][j] = D[i][j - 1] + (D[i][j - 1] - D[i - 1][j - 1]) / (4**j - 1)

    return D[N][N]


if __name__ == "__main__":
    # Example function
    def f(x):
        return x**math.cos(x)

    x0 = 0.6
    estimate = derivative_estimation(f, x0, h=0.1, N=5)

    print(f"Estimated derivative of f at x={x0}: {estimate:.6f}")
