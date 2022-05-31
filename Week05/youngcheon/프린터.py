from collections import deque
def solution(pri, location):
    answer = []
    q = deque()
    for i,e in enumerate(pri):
        q.append((i, e))
    while q:
        temp = list(map(lambda x: x[1], q))
        l, p = q.popleft()
        if p == max(temp):
            answer.append(l)
        else:
            q.append((l, p))
    return answer.index(location)+1