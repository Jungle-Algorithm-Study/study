# 다음 큰 숫자

def solution(n):
    cnt = bin(n).count('1')
    num = n + 1
        
    while bin(num).count('1') != cnt :
        num += 1
    
    return num
