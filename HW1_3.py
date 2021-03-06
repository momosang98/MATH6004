import numpy as np

# Q3:Please compute the LU decomposition by hand for the following matrices.


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


if __name__ == '__main__':

    A = [[2, -1, 1,3], [4, -1, 0,5], [-4, 3, -3,-5],[2,2,-3,2]]  # (a)
    B = [[2, 1, 0,0], [1, 4, 1,0], [0, 1, 4,1],[0,0,1,2]]  # (b)
    La, Ua = LU_decomposition(A)
    Lb, Ub = LU_decomposition(B)
    print("(a) answer is :",'\n',"L=  %s" % La, '\n', "U= %s" % Ua)
    print("(b) answer is :",'\n',"L=  %s" % Lb, '\n', "U= %s" % Ub)
