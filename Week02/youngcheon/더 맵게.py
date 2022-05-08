# 더 맵게
from heapq import heappop, heappush, heapify
def solution(scov, K):
    heapify(scov) #우선순위 큐로 만들기
    count = 0 # 카운트
    while scov: # 스코빌 리스트가 빌때까지 반복
        a = heappop(scov) # 가장 적은 값을 뽑아냄
        if a >= K: # 가장 작은값이 K 이상이라면
            return count # count 반환하고 종료
        if scov: # 가장 작은값을 뽑은 후에도 값이 남아있다면
            b = heappop(scov) # 그다음 작은 값을 뽑아냄
            heappush(scov, a+(b*2)) #계산한 값을 다시 넣음
            count += 1 # 카운트 +1
    return -1 # a값이 k값을 못넘고 끝나게 되면 -1 반환