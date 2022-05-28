'''
가격이 떨어지지 않은 기간
top이 나보다 낮아지기 전까지 push
나보다 낮아지면 pop! and index의 차를 answer에 저장
'''

def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []
    
    # 맨 앞부터 top과 비교하며 나보다 큰 애가 나올 때까지 pop한다.
    for i in range(n):
        while stack and prices[stack[-1]] > prices[i]:
            popped = stack.pop()
            answer[popped] = i-popped        
        stack.append(i)
    
    # 나보다 작은 애가 나온적이 없으면 stack에 처리되지 않은 값들이 남아있다.
    while stack:
        popped = stack.pop()
        answer[popped] = i-popped # 또는 n-popped-1
    
    return answer
