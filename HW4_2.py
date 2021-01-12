import numpy as np
def LU_decomposition(A):
    n = len(A[0])
    L = np.zeros([n, n])
    U = np.zeros([n, n])
    for i in range(n):
        L[i][i] = 1
        if i == 0:
            U[0][0] = A[0][0]
            for j in range(1, n):
                U[0][j] = A[0][j]
                L[j][0] = A[j][0] / U[0][0]
        else:
            for j in range(i, n):  # U
                temp = 0
                for k in range(0, i):
                    temp = temp + L[i][k] * U[k][j]
                U[i][j] = A[i][j] - temp
            for j in range(i + 1, n):  # L
                temp = 0
                for k in range(0, i):
                    temp = temp + L[j][k] * U[k][i]
                L[j][i] = (A[j][i] - temp) / U[i][i]
    return L, U

def Inverse(matA):
    W = matA.shape[1]
    matL = matA.copy()
    matInv = np.zeros((W,W))
    for row in np.arange(0,W):
        matInv[row,row] = 1/matL[row,row]
        for k in np.arange(row-1,-1,-1):
            matInv[row,k] = -(np.dot(matInv[row,k+1:row+1],matL[k+1:row+1,k]))/matL[k,k]
    return matInv

def inverse_A(A):
    L, U = LU_decomposition(A)
    L_inv = Inverse(L)
    U_inv = Inverse(U.T).T
    e= np.dot(U_inv, L_inv)
    return e

def shifted_power(A,s,X0,tol):
    i =0
    x = [X0]
    error =1
    B = A - s * np.identity(6)
    while error > tol:
        i += 1
        y = np.dot(inverse_A(B),x[i-1])
        x.append(y / np.linalg.norm(y, ord=2))
        m = np.dot(np.dot(x[i].T,A),x[i])
        B = A - m * np.identity(6)
        error = abs(np.linalg.norm(m*x[i] - np.dot(A,x[i])))
        if error < tol:
            print("With initial vector: ", X0)
            print("iteration times",i)
            print("we get eigenvalue: ", m)
            print("we get eigenvector: ", x[i])

def create_matrix(n):
    matrix = np.zeros((n, n))
    #instance_list = []
    for i in range(n):
        if i == 0:
            matrix[i][i] = 2
            matrix[i][i + 1] = -1
        if i < n-1 and i > 0:
            matrix[i][i - 1] = -1
            matrix[i][i] = 2
            matrix[i][i + 1] = -1
        if i == n-1:
            matrix[i][i-1] = -1
            matrix[i][i] = 2
    return matrix

A = create_matrix(6)
s = 1.5
tol = 1.0e-8
X0 = np.array([1,1,1,1,1,1]).reshape((-1,1))
shifted_power(A,s,X0,tol)
