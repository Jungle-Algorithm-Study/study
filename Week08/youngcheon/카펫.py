def solution(brown, yellow):
    brown -= 4
    brown //= 2
    
    for i in range(brown):
        x, y = i, brown-i
        if x*y == yellow:
            return sorted([x+2,y+2],reverse=True)