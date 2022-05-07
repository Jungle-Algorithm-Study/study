def solution(scoville, K):
    import heapq
    '''
    가장 안 매운 음식 2개를 pop해서 새 음식으로 만든다.
    모든 음식의 맵기가 K가 될 때 까지
    
    우선순위 큐로 가장 작은애부터 뽑는다.
    '''
    answer = 0
    
    
    heapq.heapify(scoville)
    
    
    while len(scoville) >= 2 and scoville[0] < K:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        heapq.heappush(scoville, first+second*2)
        answer += 1
    
    if scoville[0] < K:
        return -1
        
    return answer
