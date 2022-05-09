from collections import Counter
def solution(p, c):
    answer = Counter(p)-Counter(c)
    return list(answer.keys())[0]