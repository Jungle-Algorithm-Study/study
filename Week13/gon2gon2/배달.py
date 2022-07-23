from collections import defaultdict
def solution(N, road, K):
    graph = defaultdict(list)
    dist = [500001] * (N + 1)
    dist[1] = 0
    will_be_visited = list(range(1,N+1))
    
    for (s, e, c) in road:
        graph[s].append([e, c])
        graph[e].append([s, c])
        
        if s == 1:
            dist[e] = c
    
    while will_be_visited:
        will_be_visited = sorted(will_be_visited, key = lambda x: dist[x], reverse=True)
        now_city = will_be_visited.pop()
        
        for next_city, next_dist in graph[now_city]:
            dist[next_city] = min(dist[now_city]+next_dist, dist[next_city])


    return len([d for d in dist[1:] if d <= K])
