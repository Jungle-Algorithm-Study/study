'''
고니고니 영어단어장
몫: quotient
나머지: remainder
'''

def solution(n, s):

    if n > s: return [-1]

    quotient, remainder = divmod(s, n)
    
    answer = [quotient] * n
    
    for i in range(remainder):
        answer[-i-1] += 1

    return answer
