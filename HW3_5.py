import numpy as np
import math

#This is answer of HW3_5,using SD method and CG method
def create_matrixA(n):
    instance_list = []
    for i in range(n): #row
        for j in range(n): # col
            if i <= j:
                tmp = (i+1) * (n - j)
                instance_list.append(tmp)
    matrix = np.zeros((n,n))
    index = 0
    for i in range(n): #row
        for j in range(n): # col
            if i <= j:
                matrix[i][j] = instance_list[index]
                index += 1

            if i > j:
                matrix[i][j] = matrix[j][i]
    return (1/(n + 1 )**3) * matrix

def create_matrixf(n):
    matrix = np.zeros((n, 1))
    for i in range(n):
        x = i/(n+1)
        f = x*(1-x)*(math.e**(x))
        matrix[i][0] = f
    return matrix

def SD(A,b,m):
    xs = []
    rs = []
    ds = []
    alphas = []
    n = b.shape[0]
    x0 = np.zeros((n, 1))
    xs.append(x0)
    for i in range(m):
        d = b - np.dot(A,xs[i])
        alpha = np.dot(np.transpose(d),d)/np.dot(np.dot(np.transpose(d),A),d)
        x = xs[i] + alpha*d
        r = b - np.dot(A,x)
        if np.linalg.norm(r) < 1.0e-8:
            return u'The iteration number of SD method is %s ' % (i + 1)  # and x is %s'% (i+1,xs[i])
        else:
            rs.append(r)
            alphas.append(alpha)
            xs.append(x)
            ds.append(d)
    return u'Increase the iteration number !'


def CG(A,b,m):
    n = b.shape[0]
    xs = []
    rs = []
    ps = []
    alphas = []
    betas = []
    x0 =  np.zeros((n,1))
    xs.append(x0)
    r0 = b - np.dot(A,x0)
    rs.append(r0)
    p1 = r0
    ps.append(p1)
    alpha1 = np.dot(np.transpose(r0),r0)/np.dot(np.dot(np.transpose(p1),A),p1)
    alphas.append(alpha1)
    x1 = x0 + alpha1*p1
    xs.append(x1)
    r1 = r0 -  np.dot(alpha1*A,p1)
    rs.append(r1)
    beta2 = np.dot(np.transpose(r1), r1) / np.dot(np.transpose(r0), r0)
    betas.append(beta2)
    p2 = r1 + beta2*p1
    ps.append(p2)
    alpha2 = np.dot(np.transpose(r1), r1) / np.dot(np.dot(np.transpose(p2), A), p2)
    alphas.append(alpha2)

    for i in range(1,m):
        r = rs[i] - np.dot(alphas[i]* A, ps[i])
        beta = np.dot( np.transpose(rs[i]),rs[i]) / np.dot(np.transpose(rs[i-1]),rs[i-1])
        p = r + beta * ps[i]
        alpha = np.dot(np.transpose(r),r) / np.dot(np.dot(np.transpose(p), A), p)
        x = xs[i] + alpha*p

        if np.linalg.norm(r) < 1.0e-8:
            return u'The iteration number of CG method is %s '%(i+1) #and x is %s'% (i+1,xs[i])
        else:
            rs.append(r)
            alphas.append(alpha)
            xs.append(x)
            ps.append(p)
            betas.append(beta)
    return u'Increase the iteration number !'


N = [9,19,39,79,159,319]
for n in N:
    A = create_matrixA(n)
    b = create_matrixf(n)
    nc2 = CG(A,b,10000)
    nc1 = SD(A,b,200000)
    print('When n is ',n,'\n',nc1,'\n',nc2)





