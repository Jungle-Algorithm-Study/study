# 주식 가격
# 고니고니 코드 이해하고 넘어감

def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for i in range(len(prices)) :
        while stack and prices[stack[-1]] > prices[i] :
            crtIdx = stack.pop()
            answer[crtIdx] = i - crtIdx
        stack.append(i)
        
    while stack :
        crtIdx = stack.pop()
        answer[crtIdx] = i - crtIdx

    return answer
