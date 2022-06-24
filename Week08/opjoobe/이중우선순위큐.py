# 큐가 비어있으면 [0,0]
# 큐가 비어있지 않으면 [최댓값, 최솟값]
# 1 < = operations  < 1mil

# 최댓값이 둘 이상인 경우, 하나만 삭제
# 최솟값이 둘 이상인 경우, 하나만 삭제
# 빈 큐에 데이터 삭제하라는 연산이 주어지면, 해당 연산은 무시(continue)

''' 연산 '''
# I 숫자: 숫자를 삽입
# D 1 : 최댓값 하나 삭제
# D -1 : 최솟값 하나 삭제
from heapq import heappush, heappop, heapify
def solution(operations):
    answer = []
    min_heap = []
    max_heap = []
    for now_op in operations:
        order, n = now_op.split()
        if order == 'D':
            if not min_heap:
                continue
            if int(n) == 1:
                target = heappop(max_heap)
                min_heap.remove(-target)
            else:
                target = heappop(min_heap)
                max_heap.remove(-target)
        else: # order = 'I'
            heappush(min_heap, int(n))
            heappush(max_heap, -int(n))
            
    ''' 모든 연산이 처리한 후, 답을 return '''
    if not min_heap:
        return [0,0]
    else:
        maxi = -heappop(max_heap)
        mini = heappop(min_heap)
        return [maxi, mini]