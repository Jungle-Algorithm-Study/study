def solution(n):
    ans = 0
    
    while True:
        n,y = divmod(n,2)
        if y != 0:
            ans += 1  
        if n <= 0:
            return ans
