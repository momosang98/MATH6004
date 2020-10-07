import numpy as np
import math
import matplotlib.pyplot as plt

'''Q5：Write a computer program to solve the linear system below 
Please print out the numerical solution with six decimal digits for n = 9,
make plots to show the datasets {(xi, ui)}n i=1 for n = 99, 199, 399, 799'''

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
    return ((n+1)**2) * matrix


def matrix_fi(n):
    matrix = np.zeros((n, 1))
    for i in range(n):

        x = (i + 1)/(n + 1)
        m = (3*x + x**2)*(math.e**x)
        matrix[i][0] = m
    return matrix

def matrix_ui(n):
    inverse_x = np.linalg.inv(create_matrix(n))
    u = np.dot(inverse_x,matrix_fi(n))
    return u

n = 9
print(create_matrix(n))
print(matrix_fi(n))
print(np.linalg.inv(create_matrix(n)))
print('The u is :','\n',matrix_ui(n))



plt.ion()
plt.show()
n = 99
a = []
for i in range(n):
    x = (i + 1) / (n + 1)
    a.append(x)
plt.plot(a, matrix_ui(n), 'b-', label='datasets')
plt.ioff()
plt.show()







