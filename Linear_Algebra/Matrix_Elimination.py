import numpy as np
import scipy
from time import time


def eliminate(A, b):
    # Create augmented matrix Ab
    A_aug = np.append(A, b, 1)

    # Create the identity matrix of the dimensions of the function input A
    I = np.zeros(A.shape)
    n = A_aug.shape[0]
    for i in range(0, n):
        I[i, i] = 1
    # Create empty elimination matrix, E, and permutation matrix, P
    E = I
    P = I

    # Create each appropriate elementary operation matrix for each elimination step and multiply to A_aug
    for j in range(0, A.shape[1] - 1):

        if A_aug[j, j] == 0:
            k = 1
            while A_aug[j, j] == 0:
                if A_aug[j + k, j] != 0:
                    # Create appropriate permutation matrix to swap rows
                    P[j, j] = 0
                    P[j, j + k] = 1
                    P[j + k, j] = 1
                    P[j + k, j + k] = 0

                    # Multiply A_aug by permuation matrix P to swap rows
                    A_aug = np.matmul(P, A_aug)

                    # Restore P to the identity matrix
                    P[j, j] = 1
                    P[j, j + k] = 0
                    P[j + k, j] = 0
                    P[j + k, j + k] = 1

                k = k + 1

        for i in range(1, A_aug.shape[0] - j):
            # Find multiplier l
            l = A_aug[i + j, j] / A_aug[j, j]

            # Create elimination matrix with -l in the appropriate position
            E[i + j, j] = -l

            # Mulitply A_aug by elimination matrix E
            A_aug = np.matmul(E, A_aug)
            print A_aug

            # Restore elimination matrix to the identity matrix
            E[i + j, j] = 0

    return A_aug


# Create a function that performs back substitution
def back_sub(M):
    n = M.shape[0] - 1

    # Separate out b vector from augmented matrix M
    b = scipy.delete(M, np.s_[0:n + 1], 1)

    # Create empty solution vector
    x = np.zeros(b.shape)

    # Compute last element in the solution vector, x
    if M[n, n] == 0:
        print "There was an error"
    else:
        x[n] = M[n, n + 1] / M[n, n]

        # Create non-augmented upper triangular coefficient matrix (delete the farthest right column)
        U = scipy.delete(M, n + 1, 1)

        # Calculate remaining values in the solution vector, x using dot product
        for i in range(n - 1, -1, -1):
            x[i] = (b[i] - np.dot(U[i, i + 1:n + 1], x[i + 1:n + 1])) / U[i, i]

        return x


