def get_dist(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])


def solution(numbers, hand):
    '''
    continue 사용 이유?
    continue를 쓰지 않으면 2,5,8,0의 케이스를 else문 안에 넣어야 하는데 depth가 너무 깊어지면 보기 불편해서
    '''
    
    
    
    answer = ''
    
    # keyboard 초기화
    idx = 0
    keyboard = dict()
    keys = "123456789*0#"
    for i in range(4):
        for j in range(3):
            keyboard[keys[idx]] = (i, j)
            idx += 1
    
    # 왼손 오른손 위치 세팅
    left = keyboard['*']
    right = keyboard['#']
    
    # 아래에서 "n in" 연산을 빠르게 처리하기 위해 세트로 변환
    left_numbers = set("147")
    right_numbers = set("369")
    
    
    numbers = [*map(str, numbers)]
    for n in numbers:

        # 바로 처리 가능한 경우
        if n in left_numbers: 
            # 왼손으로만 누르는 번호
            answer += "L"
            left = keyboard[n]
            continue
            
        elif n in right_numbers:
            # 오른손으로만 누르는 번호
            answer += "R"
            right = keyboard[n]
            continue
            
            
            
        # 위치를 계산해야 하는 경우
        target_position = keyboard[n]
        left_dist = get_dist(target_position, left)
        right_dist = get_dist(target_position, right)
            
        if left_dist < right_dist: 
            answer += "L"
            left = target_position
        elif left_dist > right_dist:
            answer += "R"
            right = target_position
        else:
            if hand == "left":
                answer += "L"
                left = target_position
            else:
                answer += "R"
                right = target_position
                
    return answer
