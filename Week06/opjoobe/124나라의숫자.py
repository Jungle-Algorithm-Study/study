#프로그래머스 # 124 나라의 숫자 # 7시18분 시작 # 7시 48분 끝 # 30mins

def solution(n):
    answer = ''
    while n:
        n, b = divmod(n,3)
        if not b:
            b = 3
            n -= 1
        answer += str(b)
    answer = answer[::-1].replace('3','4')
    return answer

n = 12
print(solution(n))