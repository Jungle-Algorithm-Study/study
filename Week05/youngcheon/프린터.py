from collections import deque
def solution(pri, location):
    answer = []
    q = deque([(i,e) for i,e in enumerate(pri)])
    while q:
        max_ = max(q, key=lambda x: x[1])[1]
        l, p = q.popleft()
        if p == max_:
            answer.append(l)
        else:
            q.append((l, p))
    return answer.index(location)+1


print(solution([2, 1, 3, 2],2))