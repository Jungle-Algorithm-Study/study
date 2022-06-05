# 프린터 # 7시 7분 시작 # 7시 18분 끝
from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque()
    for idx,priority in enumerate(priorities):
        queue.append([idx, priority])
    # print(queue)
    while queue:
        case_i,case_p = queue.popleft()
        # print(case_i,case_p)
        for i,p in queue:
            if case_p < p:
                queue.append([case_i,case_p])
                break
        else:
            answer += 1
            if case_i == location:
                return answer

priorities = [1, 1, 9, 1, 1, 1]
location = 0

print(solution(priorities, location))