def solution(brown, yellow):
    n = (brown-4)//2
    for i in range(n):
        x, y = i, n-i
        if x*y == yellow:
            return sorted([x+2,y+2],reverse=True)