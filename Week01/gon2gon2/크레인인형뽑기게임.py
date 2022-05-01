def solution(board, moves):
    '''
    시작: 11:09
    종료: 12:30(점심 먹고 옴)
    '''
    answer = 0
    
    # 매 move마다 구해주면 비효율 적이니까 한번만 구한다.
    N = len(board)
    stack = []

    for m in moves:
        # 인형뽑기는 1부터 시작해서 인덱스 맞춰줌
        m -= 1

        for i in range(N):
            if board[i][m]:         # 비어있는 칸이면 0이므로 위에서부터 아래로 내려가며 인형을 찾는다
                popped = board[i][m]# 인형이 있으면 값을 popped에 저장하고
                stack.append(popped)# popped를 스택에 추가한 뒤 0으로 비워준다.
                board[i][m] = 0
                break

        if len(stack) >= 2 and stack[-1] == stack[-2]: # 순서에 유의(2개 이상인지부터 확인해야 함)
            # 슬라이싱으로 해도 되지만 좀 더 직관적으로 작성
            for _ in range(2):
                 stack.pop()
                 answer += 1
    
    return answer
