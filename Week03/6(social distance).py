# 대기실 5개, 각 대기실은 5x5 형태.
# 거리두기 위해 맨해튼거리 >2 되도록 # 파티션으로 막혀있으면 ok

# 대기실별로 거리두기 준수 여부 확인하기

""" 응시자 P 빈 테이블 O 파티션 X """
# places 의 각 행이 각 대기실
places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

# 첫번째 풀이
import itertools
def solution(places):
    answer = []
    for place in places:
        participants = [[i,j] for i in range(5) for j in range(5) if place[i][j]=='P']
        flag = True
        for c in itertools.combinations(participants,2):
            p1, p2 = c[0],c[1]
            p1_x, p1_y = p1[0], p1[1]
            p2_x, p2_y = p2[0], p2[1]
            # dist > 2
            if abs(p1_x - p2_x) + abs(p1_y - p2_y) > 2:
                continue
            # dist = 1
            if abs(p1_x - p2_x) + abs(p1_y - p2_y) < 2:
                flag = False
                break
            # dist = 2
            if p1_x == p2_x: # case 1 : same column
                if place[p1_x][(p1_y + p2_y)//2] == 'O':
                    flag = False
                    break
            elif p1_y == p2_y: # case 2: same row
                if place[(p1_x + p2_x)//2][p1_y] == 'O':
                    flag = False
                    break
            else: # case 3: diagonal
                if place[p1_x][p2_y] == 'O' or place[p2_x][p1_y] == 'O':
                    flag = False
                    break
        answer.append(1 if flag else 0)
    return answer
print(solution(places))

# 두번째 풀이
# 어떤 점이 있을때, 오른쪽 점 / 아래쪽 점 / 우측아래대각선 점만 확인하면 됨.

def solution(places):
    answer = []
    for place in places:
        participants = [[i,j] for i in range(5) for j in range(5) if place[i][j]=='P']
        flag = True
        for c in itertools.combinations(participants,2):
            p1, p2 = c[0],c[1]
            p1_x, p1_y = p1[0], p1[1]
            p2_x, p2_y = p2[0], p2[1]
            # dist > 2
            if abs(p1_x - p2_x) + abs(p1_y - p2_y) > 2:
                continue
            # dist = 1
            if abs(p1_x - p2_x) + abs(p1_y - p2_y) < 2:
                flag = False
                break
            # dist = 2
            if p1_x == p2_x: # case 1 : same column
                if place[p1_x][(p1_y + p2_y)//2] == 'O':
                    flag = False
                    break
            elif p1_y == p2_y: # case 2: same row
                if place[(p1_x + p2_x)//2][p1_y] == 'O':
                    flag = False
                    break
            else: # case 3: diagonal
                if place[p1_x][p2_y] == 'O' or place[p2_x][p1_y] == 'O':
                    flag = False
                    break
        answer.append(1 if flag else 0)
    return answer
print(solution(places))
