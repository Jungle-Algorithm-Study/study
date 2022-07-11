def solution(n,a,b):
    answer = 0
    
    while a != b:
        a = sum(divmod(a,2))
        b = sum(divmod(b,2))
        answer += 1
        
    return answer