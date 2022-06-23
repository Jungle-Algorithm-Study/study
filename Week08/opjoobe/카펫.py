# 프로그래머스 # 카펫
# 7시 3분 시작 # 7시 14분 끝

# 두번째 풀이 (첫번째 풀이의 개선)
import math
def solution(brown, yellow):
    total = brown + yellow
    jump = 2 if total % 2 else 1
    for sero in range(3, int(math.sqrt(total))+1, jump):
        if total % sero == 0:
            garo = total // sero
            if yellow == (garo-2)*(sero-2):
                return [garo,sero]

# 첫번째 풀이
import math
def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for sero in range(3, int(math.sqrt(total))+1):
        if total % sero == 0:
            garo = total // sero
            if yellow == (garo-2)*(sero-2):
                break
    return [garo,sero]