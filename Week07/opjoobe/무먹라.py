# 프로그래머스 #무지의먹방라이브 

# 첫번째 풀이 # 정확성 100 # 효율성 0 # 20min
from collections import deque
def solution(food_times, k):
    answer = 1
    if k > sum(food_times):
        return -1
    # 1. 큐를 이용한 정확성 풀이
    q = deque(list(enumerate(food_times,1)))
    while q and k:
        now_idx, now_cnt = q.popleft()
        now_cnt -= 1
        if now_cnt:
            q.append((now_idx, now_cnt))
        k-=1
    if k > 0:
        return -1
    else:
        return q.popleft()[0] if q else -1
    
# 2. 전체길이를 재서, 전체길이 * 최소횟수가 k보다 작으면 한번에 루프를 돌아버리는 풀이 # 80min...
        
from heapq import heappop, heapify
def solution(food_times, k):
    heap = list(zip(food_times, list(range(1, len(food_times)+1))))
    heapify(heap)
    before = 0
    while heap:
        min_cnt = heap[0][0]
        heap_length = len(heap)
        one_period = (min_cnt-before) * heap_length
        if one_period >= k:
            n1, n2 = divmod(k, heap_length)
            k = n2
            if n1 >= min_cnt - before:
                while heap and heap[0][0] == min_cnt:
                    heappop(heap)
            # j = 0
            # while k >= heap_length:
            #     k -= heap_length
            #     j += 1
            # if j >= min_cnt - before:
            #     while heap and heap[0][0] == min_cnt:
            #         heappop(heap)
            break
        else:
            k -= one_period
            before = min_cnt
            while heap and heap[0][0] == min_cnt:
                heappop(heap)
    
    if not heap:
        return -1
    else:
        heap = list(heap)
        heap.sort(key=lambda x:x[1])
        if k == len(heap):
            return heap[0][1]
        else:
            return heap[k][1]
            
        
    
    
        
    
    