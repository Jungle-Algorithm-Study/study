s = 'baabaa'
# s = 'cdcd'

def check(s):
    stack = []
    stack.append(s[0])
    for i in s[1:]:
        if stack and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    return (0 if stack else 1)

def solution(s):
    answer = check(s)
    return answer

print(solution(s))
