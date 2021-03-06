'''remove로 하면 heap 성질이 깨진다는 주형님의 정보로 다시 수정하여 올립니다~~-> heapify추가''' 
#큐가 비어있으면 [0.0] 비어있지 않으면 최댓값, 최솟값을 return
import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    
    for instruction in operations :
        inst, num = instruction.split(" ")
        
        int_num = int(num)
        if inst == 'I' :
            heapq.heappush(min_heap, int_num)
            heapq.heappush(max_heap, (-int_num, int_num))
        
        if inst == 'D' :
            if len(min_heap) == 0 :
                continue
            if int_num == 1 :
                max_val = heapq.heappop(max_heap)
                min_heap.remove(max_val[1])
                heapq.heapify(min_heap)
            else :
                min_val = heapq.heappop(min_heap)
                max_heap.remove((-min_val,min_val))
                heapq.heapify(max_heap)
    if not min_heap :
        return [0,0]
                
    return [heapq.heappop(max_heap)[1], heapq.heappop(min_heap)]



''' 첫번째 풀이 '''
#큐가 비어있으면 [0.0] 비어있지 않으면 최댓값, 최솟값을 return
import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    
    for instruction in operations :
        inst, num = instruction.split(" ")
        
        int_num = int(num)
        if inst == 'I' :
            heapq.heappush(min_heap, int_num)
            heapq.heappush(max_heap, (-int_num, int_num))
        
        if inst == 'D' :
            if len(min_heap) ==0 :
                continue
            if int_num == 1 :
                max_val = heapq.heappop(max_heap)
                min_heap.remove(max_val[1])
            else :
                min_val = heapq.heappop(min_heap)
                max_heap.remove((-min_val,min_val))
                
    if not min_heap :
        return [0,0]
                
    return [heapq.heappop(max_heap)[1], heapq.heappop(min_heap)]
