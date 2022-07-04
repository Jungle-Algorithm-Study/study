from collections import defaultdict, deque
def solution(n, edge):
    graph = defaultdict(list)
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    visited = [0]*(n+1)
    visited[1] = 1
    q = deque([1])
    
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = visited[now] + 1
                q.append(i)

    return visited.count(max(visited))