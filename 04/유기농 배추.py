from collections import deque


search = [(-1,0),(0,1),(1,0),(0,-1)]

T = int(input())
for _ in range(T):
    M, N, k = map(int, input().split())
    # 배추밭을 만듭니다
    farm = [[0] * M for _ in range(N)]
    for __ in range(k):
        # 배추를 심습니다
        x, y = map(int, input().split())
        farm[y][x] = 1
        
    # 0마리로 시작
    baechooWorm = 0
    # 밭을 돌아봅니다
    for i in range(N):
        for j in range(M):
            # 배추가 있는 자리 발견하면 0으로 방문처리 하고 큐에 넣음
            if farm[i][j] == 1:
                q = deque([(i,j)])
                farm[i][j] = 0
                # 주변을 탐색함
                while q:
                    x ,y = q.popleft()
                    for sx, sy in search:
                        nx, ny = x + sx, y + sy
                        if 0 <= nx < N and 0 <= ny < M and farm[nx][ny] == 1:
                            # 발견하면 방문처리
                            farm[nx][ny] = 0
                            q.append((nx,ny))
                # 벌레 + 1        
                baechooWorm += 1
                            
                            
    print(baechooWorm)
