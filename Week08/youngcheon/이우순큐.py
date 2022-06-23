from heapq import heappush, heappop, heapify
def solution(operations):
    max_heap = []; min_heap = []
    for i in operations:
        command, number = i.split()
        if command == 'I':
            heappush(max_heap, -int(number))
            heappush(min_heap, int(number))
        else:
            if int(number) > 0:
                try:min_heap.remove(-heappop(max_heap))
                except:continue
            else:
                try:max_heap.remove(heappop(min_heap))
                except:continue
            heapify(min_heap)
            heapify(max_heap)
    try: 
        return [-heappop(max_heap),heappop(min_heap)]
    except:
        return [0,0]