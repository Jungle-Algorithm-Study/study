# 행렬테두리회전하기 # 28min sol

# 첫번째 풀이 
# 직사각형 범위를 선택 => "테두리" 부분 숫자들을 시계방향으로 회전한다.
# 각 회전은 (x1, y1, x2, y2)인 정수 4개로 표현함.
def solution(rows, columns, queries):
    answer = []
    total = rows * columns
    Arr = [x for x in range(1,total+1)]
    # column 가로 4 , row 세로 6 => divmod(idx, 4==column) => 몫: row, 나머지: col 
    # 역추출 : idx = row * columns + col
    
    for query in queries:
        x1, y1, x2, y2 = map(lambda x: x-1, query)
        before = total + 1
        all_L = []
        # 2행(x1) 2열(y1) ~ 2행(x1) 4열(y2) # x1 고정
        for col in range(y1,y2+1):
            now_idx = columns * x1 + col
            Arr[now_idx], before = before, Arr[now_idx]
            all_L.append(before)
        # 3행(x1+1) 4열(y2) ~ 5행(x2) 4열(y2) # y2 고정
        for row in range(x1+1,x2+1):
            now_idx = columns * row + y2
            Arr[now_idx], before = before, Arr[now_idx]
            all_L.append(before)
        # 5행(x2) 3열(y2-1) ~ 5행(x2) 2열(y1) # x2 고정
        for col in range(y2-1,y1-1,-1):
            now_idx = columns * x2 + col
            Arr[now_idx], before = before, Arr[now_idx]
            all_L.append(before)
        # 4행(x2-1) 2열(y1) ~ 2행(x1) 2열(y1) # y1 고정
        for row in range(x2-1,x1-1,-1):
            now_idx = columns * row + y1
            Arr[now_idx], before = before, Arr[now_idx]
            all_L.append(before)
        answer.append(min(all_L))
        
    return answer