def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    for city in cities:
        city = city.lower()
        
        for i, v in enumerate(cache):
            if v == city:
                cache.pop(i)
                cache.append(city)
                answer += 1
                break
                
        else:
            if cache and len(cache) == cacheSize:
                cache.pop(0)
                
            if cacheSize: # cacheSize가 0인 경우에는 append 못하게
                cache.append(city)
                
            answer += 5
                
    return answer
