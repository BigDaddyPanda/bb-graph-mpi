
from mpi4py import MPI
import numpy as np
comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank
N = size

if rank == 0:
    k = np.full(1, N, dtype=int)  # default value
else:
    k = np.zeros(1, dtype=int)

comm.Bcast(k, root=0)

my_k = np.zeros(1)
all_k = np.zeros(1)



def saveSolution(board):

    global k,my_k
    k = k + 1
    my_k+=1


def isSafe(board, row, col):
    for i in range(col):
        if (board[row][i]):
            return False
    i = row
    j = col
    while i >= 0 and j >= 0:
        if(board[i][j]):
            return False
        i -= 1
        j -= 1
    i = row
    j = col
    while j >= 0 and i < N:
        if(board[i][j]):
            return False
        i = i + 1
        j = j - 1

    return True


def solveNQUtil(board, col):
    global my_k
    if (col == N):
        saveSolution(board)
        my_k[0] += 1
        return True
    res = False
    for i in range(N):
        if i == rank:
            if (isSafe(board, i, col)):
                board[i][col] = 1
                res = solveNQUtil(board, col + 1) or res
                board[i][col] = 0

    return res


def solveNQ():

    board = [[0 for j in range(10)]
             for i in range(10)]

    if (solveNQUtil(board, 0) == False):

        print("Solution does not exist")
        return
    return


# Driver Code
solveNQ()
comm.Reduce(my_k, all_k, MPI.SUM, 0)
if rank == 0:
    print("count of all possibilities for", N, "-Queen Problem is", all_k[0])
# This code is contributed by YatinGupta
