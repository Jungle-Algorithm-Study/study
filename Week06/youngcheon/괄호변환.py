# 균형있는 문자열인지 확인
def check(w):
    if not w: return False
    while True:
        c = len(w)
        w = w.replace('()','')
        if c == len(w):
            break
    return True if w=="" else False  

# 괄호 뒤집기
def reverse(u):
    temp = ""
    for c in u:
        temp += ')' if c == '(' else '('
    return temp

# 재귀 함수
def recur(w):
    u, v= '',''
    if w == '':
        return w
    left, right = 0, 0
    for i in range(len(w)):
        if w[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            u = w[:i+1]
            v = w[i+1:]
            break
    # u가 균형있는 문자열이면
    if check(u):
        return u+recur(v)
    else:
        return "("+recur(v)+")"+reverse(u[1:-1])

def solution(p):
    return recur(p)