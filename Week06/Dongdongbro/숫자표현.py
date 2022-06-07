def solution(n):
    start, count = 1, 1
    
    while start != n :
        total = 0
        for i in range(start ,n+1) :
            total += i
            
            if total == n :
                count += 1
                break
                
            elif total > n : break
        
        start += 1
        
    return count
