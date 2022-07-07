from collections import deque
def solution(n,a,b):
    answer = 0
    entry = deque(range(1, n+1))
    
    while entry:
        answer += 1
        
        temp = []
        
        for _ in range(len(entry)//2):
            A = entry.popleft()
            B = entry.popleft()
            
            if sorted([A,B]) == sorted([a,b]):
                return answer
            
            if A in (a,b):
                temp.append(A)
            elif B in (a,b):
                temp.append(B)
            else:
                temp.append(A)
                
        entry = deque(temp)

    
    return answer
