from heapq import heapify, heappop, heappush
def solution(scoville, K):
    heapify(scoville)
    answer = 0
    while True:
        try:
            first = heappop(scoville)
            if first >= K: 
                return answer
            mix = first + (heappop(scoville)*2)
            heappush(scoville,mix)
            answer += 1
        except:
            return -1


print(solution([1, 2, 3, 9, 10, 12],7))
