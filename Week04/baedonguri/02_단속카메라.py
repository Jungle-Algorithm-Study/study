# def solution(routes):
#     routes.sort(key=lambda x:x[0])
#     routes.sort(key=lambda x:x[1])    

#     cnt = 1
#     f_out = routes[0][1]
#     flag = True

#     for route in routes[1:]:
#         s_in, s_out = route        
#         if s_out >= f_out >= s_in:
#             flag = False
#         else:
#             flag = True
#             f_out = s_out

#         if flag: cnt += 1
#     return cnt

# 주형이형 피드백 기반으로 수정한 풀이
def solution(routes):
    routes.sort(key=lambda x:x[1])
    cnt = 1
    f_out = routes[0][1]

    for route in routes[1:]:
        s_in, s_out = route        
        if not (s_out >= f_out >= s_in):
            cnt += 1
            f_out = s_out
        
    return cnt

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]

print(solution(routes))
