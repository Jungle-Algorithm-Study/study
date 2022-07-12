# 프로그래머스 # 짝지어제거하기 # 4min
def solution(s):
    stack = []
    for i in s:
        stack.append(i)
        while len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
            else:
                break
    return 1 if not stack else 0