import time
import numpy as np

#Q4:Write a computer program to find the inverse of the matrix A.

#Define matrix A
def create_matrix(n):
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

    return (1/(n + 1 )) * matrix

#Define inverse matrix
def inverse_matrix(n):
    A = create_matrix(n)
    return np.linalg.inv(A)

if __name__ == '__main__':
    n = 4
    print('When n =4, the inverse matrix A−1 is:', '\n', inverse_matrix(n))
    n = 8
    print('When n =8, the inverse matrix A−1 is:', '\n', inverse_matrix(n))

    time_start = time.time()
    n = 100
    print('When n =100, the inverse matrix A−1 is:', '\n', inverse_matrix(n))
    time_end = time.time()
    print('cost time:', '\n', time_end - time_start)

    time_start = time.time()
    n = 200
    print('When n =200, the inverse matrix A−1 is:', '\n', inverse_matrix(n))
    time_end = time.time()
    print('cost time:', '\n', time_end - time_start)

    time_start = time.time()
    n = 400
    print('When n =400, the inverse matrix A−1 is:', '\n', inverse_matrix(n))
    time_end = time.time()
    print('cost time:', '\n', time_end - time_start)

    time_start = time.time()
    n = 800
    print('When n =800, the inverse matrix A−1 is:', '\n', inverse_matrix(n))
    time_end = time.time()
    print('cost time:', '\n', time_end - time_start)


