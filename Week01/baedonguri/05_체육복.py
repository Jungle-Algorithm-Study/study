from collections import deque

# def solution(n,lost, reserve):
#     answer = n - len(lost)
#     s_reserve = set(reserve)-set(lost)
#     s_lost = set(lost)-set(reserve)
    
#     que = deque(s_lost)
    
#     while que:
#         l_num = que.popleft()
#         for r_num in s_reserve:
#             if l_num+1 == r_num or l_num-1 == r_num:
#                 answer += 1
#                 s_reserve.remove(r_num)
#                 break

#     return answer
def solution(n, lost, reserve):
    # 여벌 체육복을 가져온 학생도 도난 당할 수 있기 때문에
    # set을 통해 유일값으로 만들어줌
    set_reserve = list(set(reserve)-set(lost))
    set_lost = list(set(lost)-set(reserve))
    set_reserve.sort()
    
    for r in set_reserve:
        # 앞 사람의 번호
        f_num = r - 1
        # 뒷사람의 번호
        b_num = r + 1

        # 빌려야하는 사람이 set_lost 배열에 존재하면 remove 해줌
        if f_num in set_lost:
            set_lost.remove(f_num)
        elif b_num in set_lost:
            set_lost.remove(b_num)
    # 최종적으로 (전체인원 - 못빌린인원)을 해주면 수업을 들을 수 있는 인원수가 됨
    return n - len(set_lost)

n = 5
lost = [2,4]
reserve = [1,3,5]

print(solution(n,lost,reserve))