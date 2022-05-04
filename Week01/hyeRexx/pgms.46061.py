def solution(board, moves):
    answer = 0
    box = []
    
    for col in moves :
        for row in range(len(board)) :
            if board[row][col - 1] :
                box.append(board[row][col - 1])
                board[row][col - 1] = 0
    
                case = 1
                while case == 1 and len(box) > 1 :
                    if box[-1] == box[-2] :
                        box.pop()
                        box.pop()
                        answer += 2
                        break
                    else :
                        case = 0
                
                break
    
    return answer


# Test case : 4
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))
