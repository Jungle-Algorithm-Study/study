def solution(routes):
    answer = 1
    routes = sorted(routes, key = lambda x : (x[1], x[0])) # 출구, 입구 순으로 sort
    last = routes[0][1] # 초기값, 가장 빠른 출구

    for route in routes :
        if route[0] <= last : # last보다 입구가 이르게 있는 경우 pass
            continue
        else : # last 이후에 입구가 있는 경우 answer++, last 갱신
            answer += 1 
            last = route[1]
    
    return answer
