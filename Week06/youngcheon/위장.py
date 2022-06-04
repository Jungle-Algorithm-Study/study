from collections import defaultdict
def solution(clothes):
    d = defaultdict(int)
    for a,b in clothes:
        d[b] += 1
    temp = [v for k,v in d.items()]
    result = 1
    for i in temp:
        result *= i+1
    return result-1