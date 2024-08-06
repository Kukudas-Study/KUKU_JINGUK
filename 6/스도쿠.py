import sys

board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
zero = []

for y in range(9):
    for x in range(9):
        if not board[y][x]:
            zero.append((y, x))

def is_sudoku(ty, tx, n):
    y = (ty // 3) * 3
    x = (tx // 3) * 3
    for i in range(9):
        # 가로줄 확인
        if board[ty][i] == n:
            return False
        # 세로줄 확인
        if board[i][tx] == n:
            return False
        # 3 * 3 확인
        if board[y + i // 3][x + i % 3] == n:
            return False
    return True

def dfs(idx):
    if idx == len(zero):
        for y in range(9):
            print(*board[y])
        exit(0)

    y, x = zero[idx]
    for i in range(1, 10):
        if is_sudoku(y, x, i):
            board[y][x] = i
            dfs(idx + 1)
            board[y][x] = 0

dfs(0)
