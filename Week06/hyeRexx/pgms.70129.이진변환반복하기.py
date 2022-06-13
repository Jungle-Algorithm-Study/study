# https://programmers.co.kr/learn/courses/30/lessons/70129
# 10분컷 힐링문제

import re 

def solution(s):
    answer = [1, 0]
    
    while True :
        answer[1] += s.count('0')
        s = re.sub('0', '', s)
        s = str(bin(len(s)))[2:]
        
        if s == '1' :
            return answer
        
        answer[0] += 1
        
    return answer
