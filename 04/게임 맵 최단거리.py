import collections

def bfs(start , target , maps):
    # 시계방향으로
    search = {(-1,0),(0,1),(1,0),(0,-1)}
    # x , y , 칸수
    q = collections.deque([(start[0], start[1], 1)])
    # 방문 체크를 위해서 만듭니다
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    # 현재 위치는 방문처리
    visited[start[0]][start[1]] = True
    
    while q:
        x , y , num = q.popleft()
        # 바로 찿으면
        if (x,y) == target:
            return num
        # 상하좌우 탐색 하면서 방문처리 하고 시간 + 1
        for sx , sy in search:
            nx = sx + x
            ny = sy + y
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and not visited[nx][ny] and maps[nx][ny] != 0:
                visited[nx][ny] = True
                q.append((nx,ny,num+1))
    # 찿을수 없으면 ..
    return -1

def solution(maps):
    # 시작위치와 적의 위치가 정해져있음
    start = (0,0)
    enemy = (len(maps)-1,len(maps[0])-1)
                
    # 탐색
    enemySearch = bfs(start,enemy,maps)
    # -1 있으면 못찿은거므로..
    if enemySearch == -1:
        return -1
    # 더해줍니다
    return enemySearch
