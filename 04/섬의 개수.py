from collections import deque
# 대각선 까지 확인
search = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def bfs(x,y):
    # 방문하면 0 으로 방문처리
    q = deque([(x,y)])
    island[x][y] = 0
    # 큐가 비어있을떄 까지
    while q:
        x,y = q.popleft()
        for sx , sy in search:
            nx , ny = x + sx , y + sy
            if 0 <= nx < h and 0 <= ny < w:
                # 땅이 있으면 0 으로 방문처리 하고 큐에 추가
                if island[nx][ny] == 1:
                    island[nx][ny] = 0
                    q.append((nx,ny))
while True:
    w, h = map(int, input().split())
    # 입력값의 마지막이 00
    if w== 0 and h == 0:
        break
    count = 0
    island = []

    for _ in range(h):
        island.append(list(map(int,input().split())))
    
    for x in range(h):
        for y in range(w):
            # 땅이 있으면 bfs하고 섬 +1
            if island[x][y] ==1:
                bfs(x,y)
                count += 1

    print(count)
