def solution(tickets):
    from collections import defaultdict, deque
    
    # 1. 그래프 생성
    routes = defaultdict(list)
    for start, end in tickets:
        routes[start].append(end)
    
    # 2. 각 출발 공항의 도착지 리스트를 역순으로 정렬
    for key in routes:
        routes[key].sort(reverse=True)
    
    # 3. DFS 알고리즘으로 경로를 생성
    stack = ["ICN"]
    path = []
    
    while stack:
        airport = stack[-1]
        
        if airport not in routes or not routes[airport]:
            path.append(stack.pop())
        else:
            stack.append(routes[airport].pop())
    
    return path[::-1]
