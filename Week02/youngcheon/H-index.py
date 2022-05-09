# H-index
def solution(citations):
    answer = 0
    for i in range(max(citations)):
        if i <= len(list(filter(lambda x: x>=i, citations))):
            answer = i
    return answer

# 한줄 풀이
solution = lambda x : max(map(min, enumerate(sorted(x)[::-1], 1)))