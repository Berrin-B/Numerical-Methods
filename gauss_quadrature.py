"""
gauss_quadrature.py

This file demonstrates the application of the 2-point Gauss Quadrature
method to approximate the integral of a given function.

Example application for an undergraduate Computational Physics course.
"""

import math


def f(x):
    """
    Function to integrate: f(x) = exp(x) * cos(x)
    """
    return math.exp(x) * math.cos(x)


def gauss_quadrature_2pt(func, a, b):
    """
    Compute the integral of a function using 2-point Gauss Quadrature.

    Parameters
    ----------
    func : callable
        Function to integrate.
    a, b : float
        Integration interval [a, b].

    Returns
    -------
    float
        Approximate integral of func over [a, b].
    """
    c = (b - a) / 2
    x1 = c * (-1 / math.sqrt(3)) + (a + b) / 2
    x2 = c * (1 / math.sqrt(3)) + (a + b) / 2

    integral = c * func(x1) + c * func(x2)
    return integral


if __name__ == "__main__":
    a, b = 0.5, 1.5
    result = gauss_quadrature_2pt(f, a, b)
    print(f"Approximate integral using 2-point Gauss Quadrature: {result:.6f}")
