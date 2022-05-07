# 더 맵게

from heapq import heapify, heappop, heappush

def solution(scoville, K):
    heapify(scoville)
    answer = 0

    while True :
        if scoville[0] >= K :
            return answer
        else :
            first = heappop(scoville)
            second = heappop(scoville)
            
            new = first + (second * 2)
            answer += 1
            
            heappush(scoville, new)
    
    return answer


scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))

#heapq를 사용, [0]과 [1]을 팝
#팝한 0과 1을 섞기 ([0] + [1]*2) > cnt ++
#섞은 값을 다시 heappush
#heapq[0]이 k이상이 될 때까지의 섞은 횟수 cnt 리턴
