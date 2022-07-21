from sys import stdin
from collections import deque
input = stdin.readline
t = int(input().rstrip())

def bfs():
    que = deque([departure])
    check = [False]*n
    while que:
        x,y = que.popleft()
        if abs(x-dest_x)+abs(y-dest_y) <= 1000:
            return True
        for i in range(n):
            if not check[i]:
                nx, ny = store[i]
                if abs(x-nx)+abs(y-ny) <= 1000:
                    check[i] = True
                    que.append([nx,ny])
    return False 


for _ in range(t):
    n = int(input().rstrip())
    departure = list(map(int,input().split()))
    store = [list(map(int,input().split())) for _ in range(n)]
    dest_x, dest_y = map(int, input().rstrip().split())
    
    result = bfs()    
    print('happy 'if result else 'sad')
    
        
    