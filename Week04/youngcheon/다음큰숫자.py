def solution(n):
    original = bin(n).count('1')
    while 1:
        if bin(n+1).count('1') == original:
            return n+1
        n+=1