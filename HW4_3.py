import math
import numpy as np

def GaussianElimination(A,B):
    N = len(A)
    for i in range(1,N):
        for j in range(i,N):
            delta = A[j][i-1]/A[i-1][i-1]
            for k in range(i-1,N):
                A[j][k] = A[j][k] - A[i-1][k]*delta
            B[j] = B[j]-B[i-1]*delta
        if abs(A[i][i]) < 1.0e-8:
            return 1
    # If the number on the diagonal of matrix A is 0，GaussianElimination fail
    B[N-1] = B[N-1]/A[N-1][N-1]
    for i in range(N-2,-1,-1):
        for j in range(N-1,i,-1):
            B[i] = B[i]- A[i][j]*B[j]
        B[i] = B[i]/A[i][i]
    return B #x
def create_matrix(n):
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            matrix[i][j] = 1 /(i + j + 1)
    return matrix

for n in range(4,10):
    A = create_matrix(n)
    B = np.zeros(n).reshape(-1, 1)
    j = 0
    B[j] = 1
    x = GaussianElimination(A, B)
    x = np.mat(x)
    X = x
    j += 1
    B = np.zeros(n).reshape(-1, 1)
    A = create_matrix(n)
    for i in range(1, n):
        B[j] = 1
        x = GaussianElimination(A, B)
        x = np.mat(x)
        X = np.hstack((X, x))#inverse_A
        j += 1
        B = np.zeros(n).reshape(-1, 1)
        A = create_matrix(n)
    k = np.linalg.norm(A, ord=2) * np.linalg.norm(X, ord=2)
    print('when n is ', n)
    print('k: ', k)



