def solution(numbers, hand):
    answer = ''
    # 키패드 좌표 
    keypad = {1:(0,0),2:(1,0),3: (2,0),4:(0,1),5:(1,1),6:(2,1),7:(0,2),
             8:(1,2),9:(2,2),'*':(0,3),0:(1,3),'#':(2,3)}
    # 왼손, 오른손 위치 초기화
    lefthand,righthand = keypad['*'], keypad['#']
    for n in numbers:
        # n의 위치
        x, y = keypad[n]
        # n으로부터 왼손과 오른손 거리
        left_distance = abs(x-lefthand[0])+abs(y-lefthand[1])
        right_distance = abs(x-righthand[0])+abs(y-righthand[1])
        # 1,4,7을 누르려고 한다면 왼손으로
        if n in [1,4,7]:
            answer += 'L'
            lefthand = keypad[n]
        # 3,6,9는 오른손으로 누른다
        elif n in [3,6,9]:
            answer += 'R'
            righthand = keypad[n]
        # 2,5,8,0이라면
        else:
            if left_distance > right_distance:
                answer += 'R'
                righthand = keypad[n]
            elif left_distance < right_distance:
                answer += 'L'
                lefthand = keypad[n]
            else:
                if hand == 'right':
                    answer += 'R'
                    righthand = keypad[n]
                else:
                    answer += 'L'
                    lefthand = keypad[n]
    return answer