def solution(n):
    answer = 0
    
    for s in range(1, n+1):
        for e in range(s, n+1):
            
            subset_sum = sum(range(s,e+1))
            
            if subset_sum < n: # 주형이형 말 듣고 올림 zz
                continue
            
            elif subset_sum == n:
                answer += 1
                break    
                
            elif subset_sum > n:
                break
            
    return answer
