"""
Description: Nested Multiplication (秦九韶算法).
Author: 高迎新 (Yingxin Gao)
"""

import numpy as np

def nest(degree: int, coeff, x, basis=None):
    """
    Evaluates polynomial from nested form using Horner’s Method.
    
    Parameters
    ----------
    degree: `int`
        degree of the polynomial
        
    coeff: `array_like`
        array of d+1 coefficients (constant term first)
        
    x:
        x-coordinate at which to evaluate
        
    basis (optional): `array_like`
        array of d base points, if needed.
        Defaults to an array of zeros if not provided.

    Returns
    --------
    `float`: value of the polynomial at x
    """
    if basis is None:
        basis = np.zeros(degree)
    y = coeff[degree]
    for i in reversed(range(degree)):
        y = y * (x - basis[i]) + coeff[i]
    return y

if __name__ == "__main__":
    # base points are 0
    degree = 4  # Degree of the polynomial
    coeff = np.array([-1, 5, -3, 3, 2])  # Coefficients (constant term first)
    x = 1/2  # Point at which to evaluate the polynomial
    # Call the function
    result = nest(degree, coeff, x)
    print("The value of the polynomial at x =", x, "is", result)
    
    # evaluate an array of x
    x_2 = np.array([-2, -1, 0, 1, 2])
    # Call the function
    result_2 = nest(degree, coeff, x_2)    
    print("The value of the polynomial at array", x_2, "is", result_2)
    
    # base points are not 0
    degree_3 = 3 
    coeff_3 = np.array([1, 1/2, 1/2, -1/2])
    x_3 = 1
    basis_3 = np.array([0, 2, 3])
    # Call the function
    result_3 = nest(degree_3, coeff_3, x_3, basis_3)
    print("The value of the polynomial at x =", x_3, "is", result_3)

