def solution(n):
    original = bin(n).count('1')
    while 1:
        if bin(n+1).count('1') == original:
            return n+1
        n+=1
# bit 연산
def solution(n):
    postPattern = n & -n
    smallPattern = ((n ^ (n + postPattern)) // postPattern) >> 2
    return n+postPattern | smallPattern