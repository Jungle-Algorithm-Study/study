# # 야근 피로도 : 야근을 시작한 시점에서, 남은 일의 작업량을 제곱하여 더한 값. 
# # N시간 동안 야근 피로도를 최소화하도록 일하기
# # 1시간동안 작업량 1만큼을 처리할 수 있다.

from heapq import heapify, heappush, heappop
def solution(n, works):
    if sum(works) <= n:
        return 0
    if len(works) == 1:
        return (works[0]-n) ** 2
    works = [-x for x in works]
    heapify(works)
    while n:
        heappush(works, heappop(works)+1)
        n -=1 
                
    works = [x**2 for x in works]
    return sum(works)

# from heapq import heapify, heappush, heappop
# def solution(n, works):
#     if sum(works) <= n:
#         return 0
#     if len(works) == 1:
#         return (works[0]-n) ** 2
#     works = [-x for x in works]
#     heapify(works)
#     while n:
#         n1 = heappop(works)
#         n2 = heappop(works)
#         if n1 != n2:
#             gap = n2-n1
#             if gap >= n:
#                 heappush(works, n1+n)
#                 n -= n
#             else:
#                 heappush(works, n2)
#                 n -= gap
#             heappush(works, n2)
#         else:
#             heappush(works, n1+1)
#             heappush(works, n2)
#             n -= 1 
                
#     works = [x**2 for x in works]
#     return sum(works)
        
            
        
        
        