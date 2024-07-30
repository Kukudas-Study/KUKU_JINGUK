n,m = map(int,input().split())
numbers = sorted(list(map(int, input().split())))
visited = [False] * n

nlist = []

def dfs():
    if len(nlist)==m:
        print(' '.join(map(str,nlist)))
        return
    x = 0
    for i in range(n):
        if not visited[i] and x != numbers[i]:
            visited[i] = True
            nlist.append(numbers[i])
            x = numbers[i]
            dfs()
            visited[i] = False
            nlist.pop()
            
dfs()
