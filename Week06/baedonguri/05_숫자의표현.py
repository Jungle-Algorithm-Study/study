# [프로그래머스] 숫자의 표현 python
# https://programmers.co.kr/learn/courses/30/lessons/12924
n = 15
def solution(n):
    cnt = 0
    for i in range(1,n+1):
        tmp = 0
        for j in range(i, n+1):
            tmp += j
            if tmp == n:
                cnt += 1
                break
            elif tmp > n:
                break
    return cnt

print(solution(n))