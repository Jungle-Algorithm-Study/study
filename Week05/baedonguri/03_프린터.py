# [프로그래머스] 프린터
# https://programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque

# 첫번째 풀이
# def solution(priorities, location):
#     que = deque([(idx, val) for idx, val in enumerate(priorities)])
#     answer = 0

#     while que:
#         flag = True
#         q = que.popleft()
#         for i in que:
#             if i[1] > q[1]:
#                 flag = False
#         if flag:
#             answer += 1
#             if q[0] == location:
#                 break
#         else:
#             que.append(q)

#     return answer

def solution(priorities, location):
    que = deque([(val, idx) for idx, val in enumerate(priorities)])
    answer = 0

    while que:
        q = que.popleft()
        if que and max(que)[0] > q[0]:
            que.append(q)
        else:
            answer += 1
            if q[1] == location:
                break
    
    
    return answer
priorities = [2, 1, 3, 2]
location = 2
print(solution(priorities, location))
