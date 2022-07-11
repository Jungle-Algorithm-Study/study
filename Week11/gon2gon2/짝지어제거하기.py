def solution(s):
    stack = []
    
    for c in s:
        while len(stack) >= 2 and stack[-2] == stack[-1]:
            stack.pop()
            stack.pop()
        stack.append(c)
    
    while len(stack) >= 2 and stack[-2] == stack[-1]:
        stack.pop()
        stack.pop()
    
    return 1 if not stack else 0
