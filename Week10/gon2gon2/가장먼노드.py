from collections import deque
def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    
    for (v1, v2) in edge:
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    queue = deque([[0, 1]])
    
    visited = [0] * (n + 1)
    
    while queue:
        now_length, now_node = queue.popleft()
        for next_node in graph[now_node]:
            if not visited[next_node]:
                visited[next_node] = now_length + 1
                queue.append([now_length + 1, next_node])
        
    visited = visited[2:]
    max_value = max(visited)
    
    return len([v for v in visited if v == max_value])
