from collections import deque
def solution(prices):
    answer = []
    que = deque(prices)
    while len(que) > 0 :
        count =0
        a = que.popleft()
        for i in que :
            if a <= i :
                count += 1
            else : 
                count += 1
                break
        answer.append(count)
            
    return answer
