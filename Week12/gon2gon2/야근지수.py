import heapq
def solution(n, works):
    works = [*map(lambda x: -x, works)]
    heapq.heapify(works)
    
    while n and works[0] != 0:
        now = heapq.heappop(works)
        heapq.heappush(works, now + 1)
        n -= 1
    
    return sum(map(lambda x: x ** 2, works))