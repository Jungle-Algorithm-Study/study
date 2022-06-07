# 프로그래머스 #숫자의 표현 # 5min sol

def solution(n):
    answer = 0
    for i in range(1,n+1):
        i_tot = 0
        for j in range(i, n+1):
            i_tot += j
            if i_tot < n :
                continue
            if i_tot > n :
                break
            if i_tot == n:
                answer += 1     

    return answer