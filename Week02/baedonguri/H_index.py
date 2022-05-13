def solution(citations):
    answer = 0
    c_len = len(citations)
    citations.sort()
    for i in range(c_len):
        if citations[i] >= c_len-i:
            return c_len-i
    return 0

print(solution([3, 0, 6, 1, 5]))