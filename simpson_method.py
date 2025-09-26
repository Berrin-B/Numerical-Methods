"""
simpson_method.py

This file demonstrates the use of Simpson's method to numerically integrate
a given function, specifically a Gaussian-like distribution.

Example application for an undergraduate Computational Physics course.
"""

import math


def f(x):
    """
    Function to integrate: Gaussian-like function
    f(x) = (1 / (2.8 * sqrt(2 * pi))) * exp(-((x - 69)^2) / 5.6)
    """
    return (1 / (2.8 * math.sqrt(2 * math.pi))) * math.exp(-((x - 69) ** 2) / 5.6)


def simpson_rule(func, a, b, n):
    """
    Compute the integral of a function using Simpson's rule.

    Parameters
    ----------
    func : callable
        Function to integrate.
    a, b : float
        Integration interval [a, b].
    n : int
        Number of subintervals (must be even).

    Returns
    -------
    float
        Approximate integral of func over [a, b].
    """
    if n % 2 != 0:
        raise ValueError("Number of subintervals n must be even for Simpson's rule.")

    dx = abs(b - a) / n
    s = func(a) + func(b)
    x = a + dx

    for i in range(1, n):
        if i % 2 == 0:
            s += 2 * func(x)
        else:
            s += 4 * func(x)
        x += dx

    integral = dx / 3 * s
    return integral


if __name__ == "__main__":
    a, b = 59.06, 71.65
    n = 4  # number of subintervals

    result = simpson_rule(f, a, b, n)
    print(f"Approximate integral using Simpson's method: {result:.6f}")
