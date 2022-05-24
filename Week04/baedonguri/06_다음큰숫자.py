# [프로그래머스] 다음큰숫자 (python)
# https://programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    MAX_NUM = 1000000
    n_bin = bin(n)[2:]
    one_cnt = n_bin.count('1')

    for i in range(n+1, MAX_NUM):
        target = bin(i)[2:]
        if one_cnt == target.count('1'):
            return i

print(solution(78))