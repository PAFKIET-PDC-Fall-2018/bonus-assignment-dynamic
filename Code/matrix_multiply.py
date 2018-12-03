
import numpy as np
from matplotlib import pyplot as plt
import time
import os
import multiprocessing as mp
import pattern
# from scipy.sparse import isspmatrix_csc,csr_matrix,isspmatrix_csr, isspmatrix, isspmatrix_bsr
import scipy.sparse as ss
datafile = ''


def matmul(name, A, B):
    # print("A is ",isspmatrix((A)))
    # print("B is ",isspmatrix((B)))
    # A=ss.csr_matrix(A)
    # B=ss.csr_matrix(B)
    # return A.dot(B)
    # print(A)
    # print(B)
    # return np.matmul(A,B)

    return pattern.coo(A,B)
# def mmmm(datafile):
    # return np.genfromtxt(datafile,delimiter=',')

def plot_matmul_performance(sizes):
    print(sizes)
    for s in sizes:
        print('Loading matrices %d ...' % s)
        start = time.time()
        datafile = 'data' + str(s) + 'A.csv'
        # a_matrix=[]
        # with mp.Pool(processes=1) as pool:
        #     a_matrix =pool.apply(mmmm,args=(datafile))
        a_matrix = np.genfromtxt(datafile,delimiter=',')
        datafile = 'data' + str(s) + 'B.csv'
        b_matrix = np.genfromtxt(datafile, delimiter=',')
        # end = time.time()
        # ttime = (end-start) * 1000.0
        # # benchmarks.append(ttime)
        # print('Matrces Loading Time %.2f' % ttime)
        C = matmul(str(s)+"array",a_matrix, b_matrix)
        print(C)
        # datafile = 'result' + str(s) + 'C.csv'
        # np.savetxt(datafile, C, fmt='%.2f', delimiter=',')
        end = time.time()
        print('Computing matmul %d Done' % s)
        ttime = (end-start) * 1000.0
        # benchmarks.append(ttime)
        print('time %.2f' % ttime)
   
    # plt.show()
arr=[1024]

plot_matmul_performance( [4] )
#plot_matmul_performance( [1024] )

# p.start()

# NUM_WORKERS = 1
 
# start_time = time.time()
 
# with mp.Pool(processes=NUM_WORKERS) as pool:
#     pool.apply(plot_matmul_performance, args=(arr,"helo"))
#    # results.wait()
 
# end_time = time.time()   

# print("Time for MultiProcessingSquirrel: %.2fsecs" % (end_time - start_time))