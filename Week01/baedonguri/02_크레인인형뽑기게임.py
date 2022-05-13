def solution(board, moves):
    n = len(board)
    stack = []
    answer = 0
    # 뽑을 순서
    for i in moves:
        for j in range(n):
            if board[j][i-1] != 0:
                push_item = board[j][i-1] # 아이템을 뽑고
                board[j][i-1] = 0 # 뽑은 위치를 0으로 초기화
                
                # 스택에 아이템이 쌓여 있을 경우
                if len(stack) > 0:
                    if stack[-1] == push_item: # 스택의 마지막 아이템이 새로 들어올 아이템과 같다면
                        stack.pop() # 스택에서 마지막 아이템을 제거해주고
                        answer += 2 # answer에 2를 추가
                        break
                # 일치하지 않을 경우 스택에 아이템을 넣어줌
                stack.append(push_item)
                break
    return answer