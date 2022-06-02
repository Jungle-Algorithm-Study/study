from collections import deque
def solution(priorities, location):
    n = len(priorities)
    answer = [0] * n
    cnt = 1
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    
    while not answer[location]:
        now = queue.popleft()
        if not queue or now[1] >= max(queue, key=lambda x: x[1])[1]:
            answer[now[0]] = cnt
            cnt += 1
            
        else:
            queue.append(now)
            
    
    return answer[location]
