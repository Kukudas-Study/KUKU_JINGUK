from collections import deque
# DFS(깊이우선탐색)  BFS(너비우선탐색)
N, M, V = map(int, input().split())
# 정점 잇기 위해서 리스트 만듬
list = [[] for _ in range(N + 1)]
# 방문여부 체크위해 처음에 False로 채운 배열
visit = [False] * (N + 1)
# 간선 정보 입력
for _ in range(M):
    a, b = map(int, input().split())
    # 양방향 간선
    list[a].append(b)
    list[b].append(a)

# 각 인접 리스트를 오름차순 정렬 
for i in range(1, N + 1):
    list[i].sort()
# 방문했으면 True
def dfs(v):
    visit[v] = True
    print(v, end=' ')
    for i in list[v]:
        # 방문 안했으면 방문
        if not visit[i]:
            dfs(i)

def bfs(v):
    # 시작정점을 큐에 추가
    queue = deque([v])
    visit[v] = True
    # 큐에 값이 없을때까지
    while queue:
        # 정점을 꺼내고 출력
        v = queue.popleft()
        print(v, end=' ')
        # 정점 v 와 연결된 정점들 순회
        for i in list[v]:
            # 방문안했다면 큐에 추가하고 방문처리
            if not visit[i]:
                queue.append(i)
                visit[i] = True

# DFS
dfs(V)
print()

# 다시 전부 False 방문안함으로 변경
visit = [False] * (N + 1)

# BFS
bfs(V)
