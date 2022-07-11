# max time : 88ms
def solution(s):
    stack = []
    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    return (len(stack)<1)+0