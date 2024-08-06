import sys

input = sys.stdin.readline


def dfs(player, score):
    global answer
    if player == 11:
        answer = max(answer, score)
        return
    for i in range(11):
        if visited[i] or not ability[player][i]:
            continue
        visited[i] = True
        order[player] = i
        dfs(player + 1, score + ability[player][i])
        visited[i] = False
        order[player] = 0


c = int(input())
for _ in range(c):
    ability = [list(map(int, input().split())) for _ in range(11)]
    answer = 0
    order = [0] * 11
    visited = [False] * 11
    dfs(0, 0)
    print(answer)
