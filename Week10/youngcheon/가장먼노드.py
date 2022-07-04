from collections import defaultdict, deque
def solution(n, edge):
    graph = defaultdict(list)
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [0]*(n+1)
    
    # 1부터 출발
    visited[1] = 1
    q = deque([1])
    
    # BFS
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = visited[now] + 1
                q.append(i)
    # 처음에는 각 번호로 가는 경로를 일일히 다 추적하려고 해서
    # 시간초과가 발생했는데, 
    # 메모이제이션으로 (사실 당연한거긴함..... .그냥 개미친놈)
    # 시간초과 해결함. 하
    return visited.count(max(visited))