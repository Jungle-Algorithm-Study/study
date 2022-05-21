def solution(routes):
    routes.sort()
    routes.sort(key = lambda x: x[1])
    answer = 1
    start = routes[0][1]
    
    for i in range(1, len(routes)):
        if start < routes[i][0]:
            start = routes[i][1]
            answer += 1
                
    return answer
