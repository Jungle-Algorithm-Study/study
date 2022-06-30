# 프로그래머스 # 예상대진표 # 10min sol

def solution(n,a,b):
    a -= 1
    b -= 1
    cnt = 0
    while True:
        cnt += 1 # ROUND {cnt} start
        next_a = a // 2
        next_b = b // 2
        if next_a == next_b:
            # a xor b can go to next round
            break
        a = next_a
        b = next_b
    return cnt