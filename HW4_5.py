import numpy as np
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

def QR_decomposition(A):
    r = np.shape(A)[0]
    Q = np.identity(r)
    R = A
    for i in range(r - 1):
        x = R[i:, i]
        e = np.zeros_like(x)
        e[0] = np.linalg.norm(x, ord=2)
        u = x - e
        w = u / np.linalg.norm(u, ord=2)
        H = np.identity(r)
        H[i:, i:] -= 2.0 * np.outer(w, w)
        R = np.dot(H, R)
        Q = np.dot(Q, H)
    return (Q, R)

n = 6
A = create_matrix(n)
(Q, R) = QR_decomposition(A)

def QR_Method(A):
    for i in range(0, 100):
        (Q, R) = QR_decomposition(A)
        A = np.dot(R, Q)
    return A

MA=QR_Method(A)
e = []
for i in range(0,6) :
    for j in range(0,6) :
        if i == j :
            e.append(MA[i][j])
e = np.around(e, 6)#保留6位小数
print('eigenvalues of A for n = 6 are {}'.format(e))

N = (10,20,40,80,160)
for n in N:
    A = create_matrix(n)
    inv_A = np.linalg.inv(A)
    #we can get inverse by LU decomposition method in question2,
    # or by Gauss elimination in question3,
    # so I use build-in function here.
    k = np.linalg.norm(A, ord=2) * np.linalg.norm(inv_A, ord=2)
    print('when n is ', n)
    print('k: ', k)