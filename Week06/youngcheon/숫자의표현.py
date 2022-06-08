def solution(n):
    answer = 0
    target = 1
    start, end = 0, 1
    while end <= n:
        if target < n:
            end += 1
            target += end
        elif target == n:
            answer += 1
            end += 1
            target += end
        else:
            start += 1
            target -= start
    return answer

print(solution(15))