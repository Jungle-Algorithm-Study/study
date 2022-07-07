def solution(n, s):
    if n > s:
        return [-1]
    answer = []
    for i in range(n,0,-1):
        t = s//i
        answer.append(t)
        s -= t
    return answer