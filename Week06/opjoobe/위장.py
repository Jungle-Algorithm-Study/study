# 프로그래머스 # 위장 #폰코딩;; #30min
from itertools import combinations
def solution(clothes):
    def comb(n,k):
        if k==0 or k==n:
            return 1
        
        a = 1
        b = 1
        for i in range(k):
            a*=(n-i)
            b*=(i+1)
        return a//b
            
    answer = 0
    cd = dict()
    for c in clothes:
        cloth, type = c[0],c[1]
        if type in cd.keys():
            cd[type].append(cloth)
        else:
            cd[type]=[cloth]
    
    flag = True
    for type in cd.keys():
        type_cnt = len(cd[type])
        answer += type_cnt
        if type_cnt > 1:
            flag = False
    if len(cd.keys())==1:
        return answer
    if flag:
        N = len(cd.keys())
        answer = 0
        for K in range(N):
            answer += comb(N,K)
            
        
        return answer
    
    keyl = len(cd.keys())
    for l in range(2,keyl+1):
        for cb in combinations(cd.keys(), l):
            now_comb = 1
            for j in range(l):
                now_comb *= len(cd[cb[j]])
            answer += now_comb
                   
    return answer