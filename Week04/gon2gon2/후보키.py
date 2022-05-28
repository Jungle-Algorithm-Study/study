from itertools import combinations
from collections import deque


def solution(relation):
    
    N = len(relation)                   # 학생 수
    max_attr = len(relation[0])
    attr = [i for i in range(max_attr)] # 특성들
    
    answer = 0
    
    make_key = lambda x, key_idx: "".join([x[k] for k in key_idx])
    
    combs = []
    for i in range(1,max_attr+1):
        combs += combinations(attr, i)
        
    # comb_set은 키 조합들을 모아두기 위해
    # comb_que를 또 만든 이유는 최소성을 위해서 정렬이 필요하기 때문
    comb_set = set(combs)
    comb_que = deque(sorted(comb_set, key=lambda x: (len(x), x)))
    print(comb_set)
    
    while comb_que:
        now = comb_que.popleft()
        table = {make_key(r, now) for r in relation}

        if len(table) == N and now in comb_set:
            now = set(now)
            comb_set = {c for c in comb_set if not now.issubset(c)}
            answer += 1

    return answer
