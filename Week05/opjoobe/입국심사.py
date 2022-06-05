def solution(n, times):
    high = times[0]*n
    low = 1
    print(f"low = {low}, high = {high}")
    while low <= high:
        cnt = 0
        mid = (low+high)//2
        for t in times:
            cnt += (mid//t)
        if cnt < n: # LowerBound 를 찾는 문제이기에, 조건에 부합하는, 즉 cnt == n인 경우 high-1을 통해 더 lower한게 있는지 찾아줌
            low = mid + 1
            print(f"mid: {mid} || low -> {low}, high = {high}") # 만약 28이 조건에 부합 안했으면 low+1 = 29가 되어서 정답 알맞게 내줌
        else:
            high = mid - 1
            print(f"mid: {mid} || low = {low}, high -> {high}")
    return low # high가 아니라 low를 리턴하게 해야함. 위와 일맥상통하게, LowerBound를 찾는 문제이기 때문에.
            
n = 6
times = [7,10]

print(solution(n,times))



