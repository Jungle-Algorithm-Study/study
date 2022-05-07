from heapq import heappop, heappush, heapify
def solution(scov, K):
    heapify(scov)
    count = 0
    while scov:
        a = heappop(scov)
        if a >= K:
            return count
        if scov:
            b = heappop(scov)
            heappush(scov, a+(b*2))
            count += 1
    return -1