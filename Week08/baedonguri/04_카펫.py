def solution(brown, yellow):
    total = brown+yellow    
    for row in range(1, total+1):
        for col in range(row,0,-1):
            if (row-2)*(col-2) == yellow and row*col == total:
                return [row, col]