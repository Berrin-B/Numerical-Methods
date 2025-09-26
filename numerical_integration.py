"""
numerical_integration.py

This file demonstrates numerical integration of a given function using
the Trapezoidal and Simpson's methods.

Example application for an undergraduate Computational Physics course.
"""

import math


def f(x):
    """
    Function to integrate: f(x) = x^3 / (exp(x) - 1)
    """
    return x**3 / (math.exp(x) - 1)


def trapezoidal_rule(func, a, b, n):
    """
    Compute the integral of a function using the trapezoidal rule.

    Parameters
    ----------
    func : callable
        Function to integrate.
    a, b : float
        Integration interval [a, b].
    n : int
        Number of subintervals (trapezoids).

    Returns
    -------
    float
        Approximate integral of func over [a, b].
    """
    dx = abs(b - a) / n
    x1 = a
    x2 = x1 + dx
    integral = 0.0

    for _ in range(n):
        integral += dx * (func(x1) + func(x2)) / 2
        x1 += dx
        x2 += dx

    return integral


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
    a, b = 0.001, 100
    n = 200  # number of subintervals

    result_simpson = simpson_rule(f, a, b, n)
    result_trapezoidal = trapezoidal_rule(f, a, b, n)

    print(f"Result by Simpson's method: {result_simpson:.6f}")
    print(f"Result by Trapezoidal method: {result_trapezoidal:.6f}")
