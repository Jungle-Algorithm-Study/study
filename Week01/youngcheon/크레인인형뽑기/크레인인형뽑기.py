def solution(board, moves):
    baguni = []
    count = 0
    for i in moves:
        for j in range(len(board[0])):
            if board[j][i-1] != 0:
                baguni.append(board[j][i-1])
                board[j][i-1] = 0
                break
        if len(baguni)>1 and baguni[-1]==baguni[-2]:
            baguni = baguni[:-2]
            count += 2
    return count

print(solution([[0,0,0,0,0],
                [0,0,1,0,3],
                [0,2,5,0,1],
                [4,2,4,4,2],
                [3,5,1,3,1]],
                [1,5,3,5,1,2,1,4]))