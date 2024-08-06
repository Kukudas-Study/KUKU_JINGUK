def dfs(board, row, n):
    num = 0
    if n == row:
        return 1
        
    for col in range(n):
        board[row] = col
        for i in range(row):
            if board[i] == board[row] or abs(board[i]-board[row]) == row - i:
                break
        else:
            num += dfs(board,row+1,n)
            
    return num



def solution(n):
    answer = dfs([0]*n,0,n)
    return answer
