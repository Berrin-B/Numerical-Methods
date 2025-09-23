"""
bisection_method.py

This file finds the required initial velocity using the bisection method when an object 
is launched from a certain height and angle to reach a specified target distance.
It then calculates the flight time, maximum height, and launch angle from the ground.

Example application for an undergraduate Computational Physics course.
"""

import math
import numpy as np
from scipy.constants import g  # gravitational acceleration (m/s^2)


def range_equation(v0, x_target, h_initial, angle_deg):
    """
    Calculates the horizontal range equation of the projectile given the initial velocity, height, and launch angle.
    
    Parameters
    ----------
    v0 : float
        Inıtial velocity (m/s)
    x_target : float
        Targeted distance (m)
    h_initial : float
        Initial height (m)
    angle_deg : float
        Angle of launch (degrees)
        
    Returns
    -------
    float
        Difference between the range and the target (f(v0) = range − x_target)
    """
    angle_rad = np.deg2rad(angle_deg)
    sin_angle = np.sin(angle_rad)
    cos_angle = np.cos(angle_rad)
    
    return (v0 * cos_angle / g) * (v0 * sin_angle + math.sqrt((v0**2) * (sin_angle**2) + 2 * h_initial * g)) - x_target


def bisection_method(func, a, b, tol=1e-6, max_iter=1000):
    """
    Finds a root of the given function using the bisection method.

    Parameters
    ----------
    func : callable
        The function for which the root is to be found.
    a, b : float
        Initial interval [a, b].
    tol : float, optional
        Tolerans (default 1e-6)
    max_iter : int, optional
        Maximum number of iterations (default 1000)

    Returns
    -------
    float
        Approximation of the function's root
    """
    iter_count = 0
    while (b - a) >= tol and iter_count < max_iter:
        m = (a + b) / 2
        f_m = func(m)
        f_a = func(a)
        
        if abs(f_m) < 1e-10:
            return m
        elif f_m * f_a < 0:
            b = m
        else:
            a = m
        
        iter_count += 1
    
    return (a + b) / 2


if __name__ == "__main__":
    # Problem parameters
    x_target = 300       # Targeted distance (m)
    h_initial = 61       # Height (m)
    angle_deg = 45       # Launch angle (degree)

    # Find the initial velocity
    v0 = bisection_method(lambda v: range_equation(v, x_target, h_initial, angle_deg),
                          a=0, b=70)
    
    print(f"Found initial velocity: {v0:.4f} m/s")

    # Time of flight
    angle_rad = np.deg2rad(angle_deg)
    sin_angle = np.sin(angle_rad)
    cos_angle = np.cos(angle_rad)
    t_flight = (v0 * sin_angle + math.sqrt((v0**2)*(sin_angle**2) + 2*h_initial*g)) / g
    print(f"Flight time: {t_flight:.4f} s")

    # Maximum height
    h_max_rel = (v0**2)*(sin_angle**2) / (2*g)
    h_total = h_max_rel + h_initial
    print(f"Maximum height from ground: {h_total:.4f} m")

    # Ground launch velocity
    v2_sin2 = 2*g*h_total
    v2_cos2 = (v0*sin_angle)**2
    v_total = math.sqrt(v2_sin2 + v2_cos2)
    print(f"Equivalent ground launch velocity: {v_total:.4f} m/s")

    theta_ground = np.rad2deg(np.arccos(x_target / (v_total * t_flight)))
    print(f"Equivalent launch angle from ground: {theta_ground:.4f} degrees")
