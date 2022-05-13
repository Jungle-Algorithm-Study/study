def solution(participant, completion):
    from collections import defaultdict
    answer = []
    part = defaultdict(int)
    
    for p in participant:
        part[p] += 1
    
    for c in completion:
        part[c] -= 1
    
    
    # 그냥 다 돌고 return
    # 25, 39, 47, 53, 57
    # 28. 43. 47. 62. 51
    answer = [k for k,v in part.items() if v > 0]
    return answer[0]
    
    
    # 나오면 바로 return
    # 25, 47, 41, 54, 55
    # 24, 39, 40, 55, 58
    # for k, v in part.items():
    #     if v > 0:
    #         return k
    
