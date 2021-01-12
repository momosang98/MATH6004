import numpy as np
from math import *

def power_method(mat,X0,tol):
    i = 0
    x = [X0]
    error = 1
    while error > tol:
        i += 1
        y = np.dot(mat, x[i-1])
        m = np.linalg.norm(y, ord=2)
       # m = np.linalg.norm(y,ord=np.inf)
        x.append(y / m)
        error = abs(np.linalg.norm(x[i] - x[i -1]))
        '''print("第{}次迭代".format(itr_num))
                print("y = ", y)
                print("m={0}".format(m))
                print("x ：", x)'''
        if error < tol:
            print("With initial vector: ", X0)
            print("we get eigenvalue: ", m)
            print("we get eigenvector: ", x[i])

a = pow(2,0.5)
A = 0.5 * np.mat([[2,a,-2],[-a,0,-a],[-2,a,2]])
X0 = np.array([1,1,1]).reshape((-1,1))
tol = 1.0e-8
print(power_method(A,X0,tol))


