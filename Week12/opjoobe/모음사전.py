# 프로그래머스 # 모음사전 
# 첫번째 풀이 # itertools.product( , repeat = ) 랑 L.index()가 생각이 안나서 걍 직접 다 만듬
def solution(word):
    answer = 0
    L = []
    def make(n,now):
        L.append(now)
        if n == 5:
            return
        for c in 'AEIOU':
            make(n+1, now+c)    
    for c in 'AEIOU':
        make(1,c)
        
    i = 1
    while True:
        if word == L[i-1]:
            return i
        i += 1

# 두번째 풀이 # itertools.product랑 index 사용 # 약간 더 빠름
from itertools import product
def solution(word):
    L = []
    for i in range(1,6):
        L.extend(list(product('AEIOU', repeat=i)))
    return sorted((map(lambda x: ''.join(x), L))).index(word)+1
    # 이걸 한줄로 줄이면, sorted(["".join(c) for i in range(1,6) for c in product("AEIOU", repeat=i)]).index(word) + 1
    return {''.join(k):v for v,k in enumerate(L,1)}[word] # 이렇게 하면 느림


