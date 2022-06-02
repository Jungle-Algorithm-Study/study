def solution(n, times):
    start, end = 0, max(times)*n
    while start <= end:
        mid = (start+end)//2
        s = sum([mid//i for i in times])
        if s < n:
            start = mid+1
        else:
            end = mid-1
    return start