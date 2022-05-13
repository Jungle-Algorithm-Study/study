# [프로그래머스] 키패드누르기 (python)
# https://programmers.co.kr/learn/courses/30/lessons/67256
from collections import deque

def solution(numbers, hand):
    result = ''
    keypad = {1 : (0,0), 2 : (0,1), 3 : (0,2),
        4 : (1,0), 5 : (1,1), 6 : (1,2),
        7 : (2,0), 8 : (2,1), 9 : (2,2),
        '*': (3,0), 0 : (3,1), '#' : (3,2)}

    cur_l,cur_r = (3,0),(3,2)

    que = deque(numbers)
    while que:
        n = que.popleft()

        if n in (1,4,7):
            result += 'L'
            cur_l = keypad[n]
        elif n in (3,6,9):
            result += 'R'
            cur_r = keypad[n]
        else:
            cur = keypad[n]
            l_dist = abs(cur[0]-cur_l[0]) + abs(cur[1]-cur_l[1])
            r_dist = abs(cur[0]-cur_r[0]) + abs(cur[1]-cur_r[1])

            if l_dist < r_dist:
                result += 'L'
                cur_l = cur
            elif l_dist > r_dist:
                result += 'R'
                cur_r = cur
            else:
                if hand == 'right':
                    result += 'R'
                    cur_r = cur
                else:
                    result += 'L'
                    cur_l = cur             
    return result


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))
