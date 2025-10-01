# 8-Queens Problem (Single Solution)

N = 8

def print_solution(board):
    for row in board:
        print(" ".join("Q" if col else "_" for col in row))
    print()

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False
    
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens(board, row=0):
    if row >= N:
        print_solution(board)
        return True  # ✅ stop after first solution
    
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve_nqueens(board, row + 1):  # return immediately if solved
                return True
            board[row][col] = 0
    return False

# Driver
board = [[0]*N for _ in range(N)]
if not solve_nqueens(board):
    print("No solution exists")
