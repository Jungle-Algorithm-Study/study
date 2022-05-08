def solution(citations):
    answer = 0
    for i in range(max(citations)):
        if i <= len(list(filter(lambda x: x>=i, citations))):
            answer = i
    return answer