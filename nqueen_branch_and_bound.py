from mpi4py import MPI


def printSolution(board):
    s = ''
    for i in range(N):
        for j in range(N):
            s += (' Q ' if board[i][j] else ' . ')
        s += ('\n')
    return s


def isSafe(row, col, slashCode, backslashCode,
           rowLookup, slashCodeLookup, backslashCodeLookup):
    if (slashCodeLookup[slashCode[row][col]] or
            backslashCodeLookup[backslashCode[row][col]] or
            rowLookup[row]):
        return False
    return True


def solveNQueensUtil(board, col, slashCode, backslashCode,
                     rowLookup, slashCodeLookup,
                     backslashCodeLookup):
    if(col >= N):
        return True
    for i in range(N):
        if(isSafe(i, col, slashCode, backslashCode,
                  rowLookup, slashCodeLookup,
                  backslashCodeLookup)):
            board[i][col] = 1
            rowLookup[i] = True
            slashCodeLookup[slashCode[i][col]] = True
            backslashCodeLookup[backslashCode[i][col]] = True

            if(solveNQueensUtil(board, col + 1, slashCode, backslashCode,
                                rowLookup, slashCodeLookup,
                                backslashCodeLookup)):
                return True
            board[i][col] = 0
            rowLookup[i] = False
            slashCodeLookup[slashCode[i][col]] = False
            backslashCodeLookup[backslashCode[i][col]] = False
    return False


def solveNQueens(board = None):
    if not board:
        board = [[0 for i in range(N)]
                for j in range(N)]
    board[0][0] = 1
    slashCode = [[0 for i in range(N)]
                 for j in range(N)]
    backslashCode = [[0 for i in range(N)]
                     for j in range(N)]
    rowLookup = [False] * N
    x = 2 * N - 1
    slashCodeLookup = [False] * x
    backslashCodeLookup = [False] * x
    for rr in range(N):
        for cc in range(N):
            slashCode[rr][cc] = rr + cc
            backslashCode[rr][cc] = rr - cc + N-1
    if(solveNQueensUtil(board, 0, slashCode, backslashCode,
                        rowLookup, slashCodeLookup,
                        backslashCodeLookup) == False):
        print("Solution does not exist")
        comm.send(board, False)
        return False
    print(printSolution(board))
    comm.send(board, True)
    return True


N = 5
# Driver Cde
solveNQueens()
# import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


# print("Process ", rank, " before n = ", n[0])
# comm.Bcast(n, root=0)
# print("Process ", rank, " after n = ", n[0])

# gl_result = np.full(size,0)
# self_result = np.full(size,0)

# for i in range(size):
#     if rank == i:
#         self_result[i]=i

if rank == 0:
    board = [[0]*N]*N
    comm.bcast(board, root=0)
else:
    board = comm.recv(source = 0)
    solveNQueens(board)

# print("Process ", rank)
comm.Reduce(board, MPI.BOR, 0)
