# 키패드 누르기 # sol 40min 

# 첫번째 풀이. 근데 divmod(number, 3) 으로도 가능했을듯 ! --> 하단에 두번째 풀이로 완료
def solution(numbers, hand):
    answer = ''
    xy = [[x,y] for x in range(4) for y in range(3)]
    keypad_D = {k:v for k,v in zip(list(range(1,10)),xy)}
    # 아이디어는 바로 떠올랐는데 여기까지 32분걸림.. 파이썬 추가공부를 합시다..
    keypad_D['A'] = [3,0] # A = *
    keypad_D[0] = [3,1]
    keypad_D['B'] = [3,2] # B = #
    now_left = keypad_D['A']
    now_right = keypad_D['B']
    for now in numbers:
        if now in (1,4,7):
            answer += 'L'
            now_left = keypad_D[now]
        elif now in (3,6,9):
            answer += 'R'
            now_right = keypad_D[now]
        else:
            now_x, now_y = keypad_D[now]
            left_x, left_y = now_left
            right_x, right_y = now_right
            # 맨해튼 거리로 해줘야 하는 이유: 대각선 이동이 되지 않기 때문. 
            # 상하좌우로만 움직일 수 있기에, x축과 y축에 평행하게만 이동할 수 있다.
            left_dist = abs(now_x - left_x) + abs(now_y - left_y)
            right_dist = abs(now_x - right_x) + abs(now_y - right_y)
            if left_dist < right_dist:
                answer += 'L'
                now_left = keypad_D[now]
            elif left_dist > right_dist:
                answer += 'R'
                now_right = keypad_D[now]
            else:
                if hand == 'right':
                    answer += 'R'
                    now_right = keypad_D[now]
                else:
                    answer += 'L'
                    now_left = keypad_D[now]
    print(keypad_D)
    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	
hand = "right"

print(solution(numbers, hand))

### 두번째 풀이 divmod 활용
def solution(numbers, hand):
    answer = ''
    '''
    keypad       divmod
    1  2  3      0 1 2   
    4  5  6      3 4 5
    7  8  9      6 7 8
    10 11 12     9 10 11
    
    keypad *->10 / 0->11 / #->12
    '''
    now_left = divmod(9,3)   # keypad(*)-1 = 10-1 = divmod 9
    now_right = divmod(11,3) # keypad(#)-1 = 12-1 = divmod 11
    for now in numbers:
        # now is keypad(now)
        if not now: # if now is keypad(0)
            now = 11 # keypad(0) = 11
        if now in (1,4,7):
            answer += 'L'
            now_left = divmod(now-1, 3)
        elif now in (3,6,9):
            answer += 'R'
            now_right = divmod(now-1, 3)
        else:
            now_x, now_y = divmod(now-1, 3)
            left_x, left_y = now_left
            right_x, right_y = now_right
            left_dist = abs(now_x - left_x) + abs(now_y - left_y)
            right_dist = abs(now_x - right_x) + abs(now_y - right_y)
            if left_dist < right_dist:
                answer += 'L'
                now_left = now_x, now_y
            elif left_dist > right_dist:
                answer += 'R'
                now_right = now_x, now_y
            else:
                if hand == 'right':
                    answer += 'R'
                    now_right = now_x, now_y
                else:
                    answer += 'L'
                    now_left = now_x, now_y
    return answer