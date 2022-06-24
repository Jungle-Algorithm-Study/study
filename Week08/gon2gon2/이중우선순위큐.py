import heapq
def solution(operations):
    answer = []

    min_heap, max_heap = [], []
    elem_num = 0

    for oper in operations:
        o, n = oper.split()
        n = int(n)

        if o == "I":
            elem_num += 1
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -n)

        elif o == "D":
            elem_num = max(0, elem_num - 1)

            if max_heap and n == 1:
                x = heapq.heappop(max_heap)
                min_heap.remove(-x)
                heapq.heapify(min_heap)

            elif min_heap and n == -1:
                x = heapq.heappop(min_heap)
                max_heap.remove(-x)
                heapq.heapify(max_heap)

    return [-max_heap[0], min_heap[0]] if elem_num > 0 else [0, 0]
