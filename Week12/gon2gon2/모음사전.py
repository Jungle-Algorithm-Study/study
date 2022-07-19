from itertools import combinations
def solution(word):
    answer = 0
    
    chars = ['A', 'E', 'I', 'O', 'U'] * 5
    pool = set()
    for i in range(1,6):
        for p in combinations(chars, i):
            pool.add(''.join(p))
    pool = sorted(pool)
    
    return pool.index(word)+1

# 위는 13~14 아래가 2~3 나오네요
def solution(word):
    chars = "AEIOU"
    stack = ['']
    pool = set()
    
    while stack:
        
        now = stack.pop()
        if len(now) == 5:
            continue
            
        for c in chars:
            new = now + c
            pool.add(new)
            stack.append(new)
    
    return sorted(pool).index(word)+1

