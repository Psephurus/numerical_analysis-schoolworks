"""
File:   fast_power.py
Brief:  指数为255的快速幂运算。
Author: 高迎新 2023200486 材料学院
Date:   2024/05/07
"""

def fast_power(base, exponent):
    """
    Parameters
    ----------
    base : `int`
        The base of the exponentiation.
    exponent : `int`
        The exponent to which the base is raised.

    Returns
    -------
    `int`
        The result of raising `base` to the power of `exponent`.
        
    Examples
    --------
    >>> fast_power(2, 255)
    57896044618658097711785492504343953926634992332820282019728792003956564819968
    """
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent //= 2
        #print(f"base = {base}, exponent = {exponent}, result = {result}")
    return result

def main():
    """
    Explanation of Calculation:
    
        The 255th power is equivalent to summing all powers of 2 from 2^0 to 2^7,
    as demonstrated by the following sequence of operations:
    
    result = x              (result = x^1)
    x = x * x               (x      = x^2)
    result = result * x     (result = x^3)
    x = x * x               (x      = x^4)
    result = result * x     (result = x^7)
    x = x * x               (x      = x^8)
    result = result * x     (result = x^15)
    x = x * x               (x      = x^16)
    result = result * x     (result = x^63)
    x = x * x               (x      = x^64)
    result = result * x     (result = x^127)
    x = x * x               (x      = x^128)
    result = result * x     (result = x^255)
    """

    # 从键盘获取x的值
    x = int(input("Enter the value of x: "))
    exponent = 255
    result = fast_power(x, exponent)
    print(f"The value of {x}^{exponent} is {result}")

if __name__ == "__main__":
    main()
