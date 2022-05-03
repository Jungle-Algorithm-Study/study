from itertools import combinations
from bisect import bisect_left
from collections import defaultdict
def solution(info, query):
    info_dict = defaultdict(list)
    answer = []
    for j in info:
        *user, user_score = j.split()
        for i in range(5):
            for c in combinations(user, i):
                temp = ''.join(c)
                info_dict[temp].append(int(user_score))
    for k in info_dict:
        info_dict[k].sort()
    for i in query:
        *search, q_score = i.replace(" and "," ").replace("-","").split()
        key = ''.join(search)
        if key in info_dict:
            score = info_dict[key]
            if score:
                enter = bisect_left(score, int(q_score))
                answer.append(len(score)-enter)
        else:
            answer.append(0)
    return answer

# 너무 어려워서 정답 코드 참고