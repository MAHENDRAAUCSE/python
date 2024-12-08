import numpy as np
import math

def mahi_karl(X, Y):
    x_mean = sum(X) / len(X)
    y_mean = sum(Y) / len(Y)
    x_diff = X - x_mean
    y_diff = Y - y_mean
    x_squared = x_diff ** 2
    y_squared = y_diff ** 2
    Ex = sum(x_squared)
    Ey = sum(y_squared)
    xy_product = x_diff * y_diff
    E = sum(xy_product)
    coeff = E / math.sqrt(Ex * Ey)
    print("X differences squared:", x_squared)
    print("Y differences squared:", y_squared)
    print("XY products:", xy_product)
    print("Sum of XY products:", E)
    print("Correlation coefficient:", coeff)
    return coeff


X_input = input("Enter the elements of array X separated by spaces: ")
Y_input = input("Enter the elements of array Y separated by spaces: ")
X = np.array(list(map(float, X_input.split())))
Y = np.array(list(map(float, Y_input.split())))

if len(X) != len(Y):
    print("Error: Arrays X and Y must have the same length!")
else:
    correlation_coefficient = mahi_karl(X, Y)
    print("Final Correlation Coefficient:", correlation_coefficient)
