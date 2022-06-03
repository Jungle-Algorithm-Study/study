import re

def recur(s,d,c):
    if s == '1': 
        return [c,d]
    temp = s.count('0')
    s = bin(len(re.sub('[0]','',s)))[2:]
    return recur(s,d+temp,c+1)

def solution(s):
    return recur(s,0,0)