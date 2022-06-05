def solution(n, times):
    start = 0
    end = max(times) *n
    
    while start < end :
        count = 0
        mid = (start+end)//2
        for i in times :
            a = mid // i
            count += a
        if count < n :
            start = mid +1
        else :
            end = mid
    
    return end
