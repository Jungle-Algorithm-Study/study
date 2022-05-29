
def get_total_capacity(n, times, mid):
    people = 0
    for t in times:
        people += mid//t
    return people
    

def solution(n, times):
    answer = max(times) * n
    start, end = 0, answer
    
    while start <= end:
        mid = (start + end ) // 2
        
        total_capacity = get_total_capacity(n, times, mid)
        if total_capacity >= n:
            end = mid - 1
            answer = min(mid, answer)
        
        else:
            start = mid + 1
    
    return answer
