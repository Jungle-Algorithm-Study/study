from collections import deque

def turnLeft(d):
    return {0:3, 1:0, 2:1, 3:2}[d]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
cleaned = [[0]*m for _ in range(n)]
cleaned[r][c] = 1

# 바라보는 위치 기준 왼쪽 좌표
goLeft = {0: [0,-1], 1: [-1,0], 2:[0,1], 3:[1,0]}
# 바라보는 위치 기준 뒷쪽 좌표
goBack = {0: [1,0], 1: [0,-1], 2:[-1,0], 3:[0,1]}

q= deque()
q.append([r,c])
count = 0
ans = 1
while q:
    x, y = q.popleft()
    # 4번 연속 회전이라면 
    if count >= 4:
        #nx, ny = 뒷쪽 좌표
       nx, ny = goBack[d][0]+x, goBack[d][1]+y
       # 빠꾸할때는 청소여부 상관없음
       if 0<= nx < n and 0<=ny<m and not graph[nx][ny]:
           q.append([nx,ny])
           count = 0
           continue
       else:
           break 
    # nx, ny = 내 왼쪽 좌표
    nx, ny = goLeft[d][0]+x, goLeft[d][1]+y
    # 바라보는 위치 업데이트
    d = turnLeft(d)
    # 범위내에 있고 nx ny가 빈칸이면서 청소하지 않았다면
    if 0<= nx < n and 0<=ny<m and not graph[nx][ny] and not cleaned[nx][ny]:
        q.append([nx,ny])
        cleaned[nx][ny] = 1
        ans += 1
        count = 0
    else:
        # 돌기만하므로 제자리, 회전 카운트 + 1
        q.append([x,y])
        count += 1

print(ans)