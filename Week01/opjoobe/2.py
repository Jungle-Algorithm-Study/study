# 크레인 인형뽑기 게임 # 풀이날짜 5월1일 # sol 11 min

def solution(board, moves):
    answer = 0
    stack = []
    n = len(board)
    for move in moves:
        col = move-1
        target = 0
        for row in range(n):
            if board[row][col]:
                target = board[row][col]
                board[row][col] = 0
                break
        if target:
            if stack and stack[-1] == target:
                answer += 2
                stack.pop()
            else:
                stack.append(target)
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]

moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))

