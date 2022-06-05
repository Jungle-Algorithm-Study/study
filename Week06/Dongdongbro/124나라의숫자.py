answer = ''

def solution(n):
    global answer
    if n%3 == 0 : answer += '4'
    elif n%3 == 1 : answer += '1'
    else : answer += '2'
    a = (n-1)//3
    if a > 0 :
        solution(a)
    return answer[::-1]
