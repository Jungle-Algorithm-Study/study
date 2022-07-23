# 프로그래머스 # 배달 # 20min sol

from collections import defaultdict, deque
from math import inf
def solution(N, road, K):
    graph = defaultdict(list)
    for u,v,d in road:
        graph[u].append([v,d])
        graph[v].append([u,d])
    distance = [inf]*(N+1)
    distance[1] = 0
    q = deque([1])
    while q:
        now_city = q.popleft()
        for next_city, dist in graph[now_city]:
            if distance[next_city] > distance[now_city] + dist:
                distance[next_city] = distance[now_city] + dist
                q.append(next_city)
                
    return len([x for x in distance[1:] if x <= K])