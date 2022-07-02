from collections import deque
def solution(cacheSize, cities):
    # 소문자로 통일
    cities = list(map(lambda x: x.lower(), cities))
    
    # 캐시사이즈가 0이라면 5곱하고 리턴
    if not cacheSize:
        return 5*len(cities)
    
    # 캐시 deque 생성
    cache = deque([0]*cacheSize)
    
    answer = 0
    for city in cities:
        if city in cache: # 캐시히트
            answer += 1
            cache.remove(city) #삭제하고
            cache.append(city) #마지막에 추가
        else: # 캐시미스
            answer += 5
            cache.rotate(-1) # 왼쪽방향으로 회전
            cache[-1] = city # 회전할경우 -1번째가 가장 먼저들어온 친구임
    return answer