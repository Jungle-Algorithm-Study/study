
# operations = ["I 16","D 1"]
operations = ["I 7","I 5","I -5","D -1"]	
from heapq import heapify, heappush, heappop

def solution(operations):
    min_heap = []
    max_heap = []
    answer = [0,0]
    for oper in operations:
        command,num = oper.split(' ')
        if command == 'I':
            heappush(min_heap, int(num))
            heappush(max_heap, -int(num))
        elif command =='D' and num == '1':
            if not max_heap: continue
            max_ = heappop(max_heap)
            min_idx = min_heap.index(-max_)
            del min_heap[min_idx]
        else:
            if not min_heap: continue
            min_ = heappop(min_heap)
            max_idx = max_heap.index(-min_)
            del max_heap[max_idx]
    
    if max_heap and min_heap:
        answer[0] = -max_heap[0]
        answer[1] = min_heap[0]
    return answer

print(solution(operations))