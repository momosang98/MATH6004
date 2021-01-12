import numpy as np
from math import *
import matplotlib.pyplot as plt
def Fun(x,num):
    f = np.zeros((num), dtype=float)
    h = 1 / num
    h2 = h ** 2
    f[0] =  3*x[0] - x[1] + h2*sinh(x[0]) - h2
    for i in range(1,num):
        '''if i == 0:
            f[i] = 3*x[i] - x[i+1] + h2*sinh(x[i]) - h2'''#i == 0 不代表i等于0
        if i == num-1:
            f[i] = 3 * x[i] - x[i -1] + h2 * sinh(x[i]) - h2
        else:
            f[i] = 2*x[i] - x[i-1] -x[i+1] + h2 * sinh(x[i]) -h2
    return f

def jocobi_inverse(x,num):
    df = np.zeros((num,num),dtype=float)
    dx = 0.00001
    x1 = np.copy(x)
    for i in range(0,num):
        for j in range(0,num):
            x1 = np.copy(x)
            x1[j] = x1[j]+dx
            df[i,j] = (Fun(x1,num)[i]-Fun(x,num)[i])/dx
    df_1 = np.linalg.inv(df)
    return df_1

def Newton(x,num):
    x1 = np.copy(x)
    error = np.copy(x)
    while(np.sum(abs(error))> 1.e-8):
        x1 = x-np.dot(jocobi_inverse(x,num),Fun(x,num))
        error = x1-x
        x = x1
    return x
num =6
x = np.ones(num)#初始值
a = Newton(x,num)
print('when n = 6, the computed value is ')
print(np.around(a, 6))

num =200
x = np.ones((num),dtype=float)
X = []
for i in range(1,num+1):
    X.append(i)
a = Newton(x,num)

plt.plot(X, a, c='r',linestyle='-.',  label='n = 200')
plt.title("computed vector")
plt.legend(loc='best')
plt.xlabel("num")
plt.ylabel("u")
plt.show()