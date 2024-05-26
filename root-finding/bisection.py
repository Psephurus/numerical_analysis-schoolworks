"""
Title: bisection.py
Description: Provides a Bisection Method function.
Version: 1.0.0
Author: Psephurus
Last Modified: 07/02/2024 04:51
"""

import numpy as np

def bisect(f, a: float, b: float, tol: float) -> float:
    """
    Computes the approximate solution of f(x) = 0 using the Bisection Method.

    Parameters
    ----------
    f : `function`
        The function for which we are trying to find a root.
    a : `float`
        The left boundary of the interval.
    b : `float`
        The right boundary of the interval.
    tol : `float`
        The tolerance. The approximation will be within tol.

    Returns
    -------
    `float`
        Approximate solution xc.
        
    Examples
    --------
    >>> f = lambda x: x**2 - x - 1
    >>> bisect(f, 1, 2, 1e-10)
    1.618033988692332
    >>> f = lambda x: (2*x - 1) * (x - 3)
    >>> bisect(f, 0, 1, pow(10, -3))
    0.5
    """
    if np.sign(f(a)) * np.sign(f(b)) >= 0:
        raise ValueError("f(a) × f(b) < 0 not satisfied!") # ceases execution

    fa = f(a)
    fb = f(b)

    while (b - a) / 2 > tol:
        c = (a + b) / 2
        fc = f(c)

        if fc == 0: # c is a solution, done
            break

        if np.sign(fc) * np.sign(fa) < 0: # a and c make the new interval
            b = c
            fb = fc
        else: # c and b make the new interval
            a = c
            fa = fc

    xc = (a + b) / 2 # new midpoint is best estimate
    return xc

if __name__ == '__main__':
    res = bisect(lambda x: x**3 + x - 1, 0, 1, 5 * pow(10, -5))
    print(res)