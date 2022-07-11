cacheSize = 3
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]	
cities = ["A","B","A"]
def solution(cacheSize, cities):
    cache = []
    excute_time = 0

    for city in cities:
        city = city.lower()
        if cacheSize:
            if city in cache:
                excute_time += 1
                idx = cache.index(city)
                cache.append(cache.pop(idx))
                continue
            if len(cache) == cacheSize:
                cache.pop(0)
            cache.append(city)
            excute_time += 5
        else:
            return len(cities) * 5

    return excute_time



print(solution(cacheSize, cities))