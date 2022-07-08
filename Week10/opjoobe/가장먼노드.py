# 가장먼노드 # 16min sol # 첨에 머리가 도저히 안돌아서, BFS 혹은 DFS라는 단서 참고함. # 다음엔 그래프 보면 BFS DFS...
from collections import deque, defaultdict
def solution(n, edge):
    answer = 0
    # 그래프를 파악하기 (connection)
    connection = defaultdict(list)
    for u, v in edge:
        connection[u].append(v)
        connection[v].append(u)
    # queue를 돌려서 BFS 해주기 위한 초기설정    
    q = deque([1])
    visited = [True] * 2 + [False]*(n-1)
    dist = 0
    # 거리(dist)별로 순차적으로 탐색할 수 있도록, BFS 구성 
    while True:
        next_q = deque()
        for now in q:
            for candidate in connection[now]:
                if visited[candidate]: continue
                next_q.append(candidate)
                visited[candidate] = True
        if not next_q:
            # next_q로 탐색할 다음 후보지가 없다?
            # 현재 dist에서 q에 들어있던 것들이, 가장 멀리 떨어진 노드임. 그 갯수를 세자
            answer = len(q)
            break
        q = next_q
        dist += 1
    return answer