import collections

# bfs로 레버까지의 최단시간을 찿고 출구까지의 최단시간을 찿아서 더해줌 bfs 2번
def bfs(start , target , maps):
    
    # 시계방향으로
    search = {(-1,0),(0,1),(1,0),(0,-1)}
    # x , y , 걸린시간 
    q = collections.deque([(start[0], start[1], 0)])
    # 방문 체크를 위해서 만듭니다
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    # 현재 위치는 방문처리
    visited[start[0]][start[1]] = True
    
    while q:
        #현재 위치정보와 시간 꺼내기
        x , y , time = q.popleft()
        # 바로 찿으면
        if (x,y) == target:
            return time
        # 상하좌우 탐색 하면서 방문처리 하고 시간 + 1
        for sx , sy in search:
            nx = sx + x
            ny = sy + y
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and not visited[nx][ny] and maps[nx][ny] != 'X':
                visited[nx][ny] = True
                q.append((nx,ny,time+1))
    # 찿을수 없으면 ..
    return -1

def solution(maps):
    # 문자열을 탐색해서 시작위치와 레버위치 출구위치를 찿습니다
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                start = (i,j)
            if maps[i][j] == 'L':
                lever = (i,j)
            if maps[i][j] == 'E':
                eexxiitt = (i,j)
                
    # 탐색합니다
    leverSearch = bfs(start,lever,maps)
    # 2번째는 시작위치가 레버위치
    exitSearch = bfs(lever,eexxiitt,maps)
    # -1 있으면 못찿은거므로..
    if leverSearch == -1 or exitSearch == -1:
        return -1
    # 더해줍니다
    return leverSearch+exitSearch
