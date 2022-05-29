from heapq import heappop, heapify
def solution(routes):
    heapify(routes)
    _, last = heappop(routes)
    answer = 1
    while routes:
        start, end = heappop(routes)
        if start <= last: #겹치는 경우
            # 겹치는데 진출지점이 last보다 작으면 갱신해줘야함
            last = min(last, end)
        else: # 겹치지 않으면
            #카메라 설치
            answer += 1
            # 갱신
            last = end
    return answer