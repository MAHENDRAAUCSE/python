import numpy as np
import math

def Mahi_ranks(arr):

    ranks = np.zeros_like(arr, dtype=float)
    for i, value in enumerate(arr):
        rank = 1 + sum(arr < value)
        ranks[i] = rank
    return ranks

X_input = input("Enter the elements of array X separated by spaces: ")
Y_input = input("Enter the elements of array Y separated by spaces: ")
X = np.array(list(map(float, X_input.split())))
Y = np.array(list(map(float, Y_input.split())))

rank_x = Mahi_ranks(X)
rank_y = Mahi_ranks(Y)

def spearman_rank_correlation(X ,Y):
    if len(X) != len(Y):
        raise ValueError("Both lists must have the same length.")

    n = len(X)
    d = [(rank_x[i] - rank_y[i]) for i in range(n)]
    d_squared = [diff ** 2 for diff in d]

    # Compute Spearman's rank correlation coefficient
    rho = 1 - (6 * sum(d_squared)) / (n * (n ** 2 - 1))
    return rho

rho = spearman_rank_correlation(X, Y)
print(f"Spearman's Rank Correlation Coefficient: {rho}")
