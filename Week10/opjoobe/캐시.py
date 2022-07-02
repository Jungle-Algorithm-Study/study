# 도시 이름 검색 => 해당 도시 관련 맛집"게시물"을 DB에서 읽어 보여줌.
# 읽어오는 성능 개선을 위해, 캐시 크기를 조정하려고 함.
# 0 <= cacheSize <= 30
# cities : 도시이름(city)이 담긴 리스트. city는 대소문자 구분없이 영문자로만. 길이 1 ~ 20

''' LRU : Least Recently Used '''
''' LFU : Least Frequently Used '''

# 첫번째 풀이
def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    answer = 0 # initial runtime
    cache = []
    for city in cities:
        city = city.lower()
        if city in cache: # HIT
            answer += 1
            cache.remove(city)
            cache.append(city)
        else: # MISS
            answer += 5
            if len(cache) < cacheSize: # CACHE not full
                cache.append(city)
            else: # CACHE full
                cache.pop(0) # Least Recently Used
                cache.append(city)
    return answer # final runtime