from collections import defaultdict
from heapq import heappush, heappop
from math import inf
def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    for a,b,c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))
    distance = [inf] * (N+1)
    q = []
    heappush(q, (0, 1))
    distance[1] = 0
    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))
    return len(list(filter(lambda x: x<=K, distance)))