# 프로그래머스 # 괄호변환 #220605 #2시30분시작 #3시1분끝 # 31min

def solution(w):
    answer = ''
    ''' 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환 '''
    if not w:
        return answer
    ''' 2. 문자열 w 를 u,v로 분리 '''
    u = ''
    balance = 0
    for i in range(len(w)):
        now = w[i]
        if now == '(':
            balance += 1
            u += now
        else:
            balance -= 1
            u += now
        if balance == 0:
            v = w[i+1:]
            break
    # print(f"u:{u},v:{v}")
    ''' *** u가 올바른 괄호 문자열인지 검증 *** '''
    stack = []
    j=0
    while j < len(u):
        pt = u[j]
        if pt == '(':
            stack.append(pt)
        else:
            if not stack:
                break
            stack.pop()
        j+=1

    ''' 3. u가 올바른 괄호 문자열이라면'''
    if j == len(u) and not stack:
        return u + solution(v) # 3-1

    ''' 4. u가 올바른 괄호 문자열이 아니라면'''
    answer += '(' # 4-1
    answer += solution(v) # 4-2
    answer += ')' # 4-3
    u = u[1:-1] # 4-4 
    for pt in u: # 4-4 replace 세번 쓰면 될거같긴한데 귀찮..
        if pt == '(':
            answer += ')'
        else:
            answer += '('

    return answer # 4-5


p1 = '(()())()'
p2 = ')('
p3 = '()))((()'

print("답:",solution(p1))
print("답:",solution(p2))
print("답:",solution(p3))