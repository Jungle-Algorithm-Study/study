def solution(board, moves):
    answer = 0
    doll = []
    for i in moves :
        for j in range(len(board)):
            if board[j][i-1] != 0 :
                doll.append(board[j][i-1])
                board[j][i-1] = 0
                if len(doll) > 1 :
                    a = doll.pop()
                    b = doll.pop()
                    if a != b:
                        doll.append(b)
                        doll.append(a)
                    else :
                        answer += 2

                break


    return answer