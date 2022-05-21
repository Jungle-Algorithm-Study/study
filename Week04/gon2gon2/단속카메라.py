from collections import deque
def solution(routes):
    
    # 처음에 기준을 진입, 이탈 순으로 했는데 반대로 했더니 맞았다.
    routes.sort(key=lambda x: (x[1], [0]))
    routes = deque(routes)
    last = routes.popleft()[1]
    answer = 1

    while routes:
        now = routes.popleft()
        if last < now[0]:
            last = now[1]
            answer += 1
    
    return answer
