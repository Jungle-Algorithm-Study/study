# 체육복 # 풀이날짜 5월4일 # sol 21 min 
# 중간에 한번 꼬여서 지체됨. 너무 한번에 완벽하게 풀려는 욕심을 버려야 할듯.

def solution(n, lost, reserve):
    answer = 0
    new_lost = list(set(lost)-set(reserve))
    new_reserve = list(set(reserve)-set(lost))
    save = 0
    for i in new_lost:
        case1 = i-1
        case2 = i+1
        if case1 in new_reserve:
            new_reserve.remove(case1)
            save +=1
        elif case2 in new_reserve:
            new_reserve.remove(case2)
            save += 1
    answer = n-len(new_lost)+save
    return answer

n = 5
lost = [2,4]
reserve = [1,3,5]


print(solution(n,lost,reserve))
