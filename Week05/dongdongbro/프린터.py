from collections import deque

def solution(priorities, location):
    que = deque()
    que2 = deque()
    j = 0
    for i in priorities :
        que.append((j,i))
        j += 1
    while len(que) :
        flag = 0
        a = que.popleft()
        for j in range(len(que)) :
            if a[1] < que[j][1] :
                flag = 1
        if flag :
            que.append(a)
        if not flag :
            que2.append(a)
            if a[0] == location :
                break
    return len(que2)
    
