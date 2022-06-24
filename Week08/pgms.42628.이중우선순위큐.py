from heapq import heappop, heappush, heapify

def solution(operations):
    heap = []
    
    for cmd in operations :
        operator, value = cmd.split()
        value = int(value)
        
        if operator == 'I' :
            heappush(heap, value)
            
        elif heap and operator == 'D' :
            if value == -1 :
                heappop(heap)
            else :
                heap.remove(max(heap))
        
        heapify(heap)

    return [max(heap), heap[0]] if heap else [0, 0]
