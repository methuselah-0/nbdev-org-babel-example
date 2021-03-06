#!/usr/bin/env python3
# exports
"""Use numpy and scipy to produce a picture"""
from ob_example.utils.libutils import export
# from ob_example.utils.libutils import export
from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt

# exports
@export
def fun(x_num):
    return (x_num-3)*(x_num-5)*(x_num-7)+85

# exports
def main():
    pass
    A, B = 1, 8 # the left and right boundaries
    INTEGRAL, ERROR = quad(fun, A, B)
    import numpy as np
    N = 5 # the number of points
    XINT = np.linspace(A, B, N)
    YINT = fun(XINT)
    print(XINT)
    print(YINT)
    INTEGRAL_TRAPEZOID = sum((XINT[1:] - XINT[:-1]) * (YINT[1:] + YINT[:-1]) / 2)
    print("The integral is:", INTEGRAL, "+/-", ERROR)
    print("The trapezoid approximation with", len(XINT), "points is:",
          INTEGRAL_TRAPEZOID)
    #%matplotlib inline
    XBAR = np.linspace(0, 10, 200)
    YBAR = fun(XBAR)
    plt.plot(XBAR, YBAR, lw=2)
    plt.axis([0, 9, 0, 140])
    plt.fill_between(XINT, 0, YINT, facecolor='gray', alpha=0.4)
    plt.text(0.5 * (A + B), 30,r"$\int_A^B fun(XBAR)dxbar$",
    	 horizontalalignment='center', fontsize=20);

# export
if __name__ == "__main__":
    main()
