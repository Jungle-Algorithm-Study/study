def solve(number):
    if number % 2 == 0:
        return number//2
    else:
        return (number+1)//2

def solution(n,a,b):
    count = 0
    while a!=b:
        a = solve(a)
        b = solve(b)
        count+=1
    return count
# 생각해보니까 +1하든 안하든 //2 하면 걍 //2임 ㄹㅇ;