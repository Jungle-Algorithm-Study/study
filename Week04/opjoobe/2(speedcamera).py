# 5월 21일 오후 7시 # sol 10 min

def solution(routes):
    answer = 0
    routes_n = len(routes)
    if routes_n == 1:
        return 1
    routes.sort(key=lambda x: (x[1],x[0]))
    before = routes[0][1]
    answer += 1
    for i in range(1, routes_n):
        if before < routes[i][0]:
            answer += 1
            before = routes[i][1]
    return answer

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes))