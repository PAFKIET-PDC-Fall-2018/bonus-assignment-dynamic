import scipy.sparse as ss
import numpy as np

def coo(matrixA,matrixB):
    A=matrixA
    B=matrixB
    AA=ss.coo_matrix(matrixA)
    BB=ss.coo_matrix(matrixB)
    print(A)
    print(AA)

    print(B)
    print(BB)

    result = [[0 for x in range(len(A))] for y in range(len(B[0]))]

    # iterate through rows of X
    for i in range(len(A)):
        # iterate through columns of Y
        # result.append([0])
        for j in range(len(B[0])):
            # iterate through rows of Y
            for k in range(len(B)):
                result[i][j] +=( A[i][k] * B[k][j])
                
    # return A.multiply(B)
    return np.array(result)

def csr(matrixA,matrixB):
    A=ss.csr_matrix(matrixA)
    B=ss.csr_matrix(matrixB)
    # print(A)
    # print(B)
    return A.multiply(B)
def csc(matrixA,matrixB):
    A=ss.csc_matrix(matrixA)
    B=ss.csc_matrix(matrixB)
    # print(A)
    # print(B)
    return A.multiply(B)
