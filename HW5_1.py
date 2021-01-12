import numpy as np
from math import *

def Fun(x,num):
    i = num
    f = np.zeros((i),dtype=float)
    f[0] = x[0] + x[1]*tan(x[0])
    f[1] = x[0]**2+x[1]**2 - pi**2
    return f

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

def jocobi_inverse(x,num):
    df = np.zeros((num,num),dtype=float)
    dx = 0.00001
    #x1 = np.copy(x)
    for i in range(0,num):
        for j in range(0,num):
            x1 = np.copy(x)
            x1[j] = x1[j]+dx
            df[i,j] = (Fun(x1,num)[i]-Fun(x,num)[i])/dx   #f(x+dx)-f（x）/dx
    df_1 = inverse_A(df)
    return df_1

def Newton(x,num):
    x1 = np.copy(x)
    delta = np.copy(x)
    while(np.sum(abs(delta))> 1.e-8):
        x1 = x-np.dot(jocobi_inverse(x,num),Fun(x,num))
        delta = x1-x
        x = x1
    return x

num = 2
x = np.ones((num),dtype=float) #初始值
a = Newton(x,num)
print(a)