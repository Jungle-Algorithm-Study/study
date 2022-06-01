# 메뉴 리뉴얼 # 30min sol

from itertools import combinations
def solution(orders, course):
    answer = []
    for c in course:
        most_cnt = 2
        most_L = []
        orders = [x for x in orders if len(x) >= c]
        if len(orders) < 2:
            break
        set_c = sorted((set(''.join(orders))))
        for i in combinations(set_c, c):
            now_cnt = 0
            menu = set(i)
            for case in orders:
                if menu.issubset(set(case)):
                    now_cnt += 1
            if now_cnt < 2:
                continue
            if now_cnt > most_cnt:
                most_L = [''.join(i)]
                most_cnt = now_cnt
            elif now_cnt == most_cnt:
                most_L += [''.join(i)]
        if most_L:
            answer += most_L
        else:
            break
    answer.sort()
    return answer

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]

print(solution(orders, course))

