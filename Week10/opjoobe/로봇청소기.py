# 각각의 칸은 벽이거나 빈칸이다..
# 청소기는 바라보는 방향이 있음. (동,서,남,북)
# (r,c) => 지도 북쪽에서부터 r번째, 서쪽에서부터 c번째

import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
r,c,d = map(int, input().strip().split()) # (r,c)는 칸의 좌표, d는 방향

Arr = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

direction_D = dict()
direction_D[0] = [(0,-1), (1,0), (0,1), (-1,0)] # 북쪽
direction_D[1] = [(-1,0), (0,-1), (1,0), (0,1)] # 동쪽
direction_D[2] = [(0,1), (-1,0), (0,-1), (1,0)] # 남쪽
direction_D[3] = [(1,0), (0,1), (-1,0), (0,-1)] # 서쪽

visited[r][c] = True
cnt = 1

while True:
    # 단계 2. 현재 위치에서 다음을 반복하며, 인접한 칸을 탐색한다.
    if d < 0:
        d += 4
    now_rotate_D = direction_D[d]
    for dr, dc in now_rotate_D:
        d -= 1
        nr, nc = r+dr, c+dc
        if 0<=nr<N and 0<=nc<M and not Arr[nr][nc] and not visited[nr][nc]:
            r,c = nr,nc
            cnt += 1
            visited[nr][nc] = True # 단계 1. 현재 위치를 청소한다
            break
    else:
        d += 4 # 다시 원래 d로 돌려줌
        dr, dc = now_rotate_D[1]
        nr, nc = r+dr, c+dc
        r, c = nr, nc
        # 뒷칸이 벽이라면 청소기 작동이 종료됨.
        if Arr[nr][nc]:
            break
        if not visited[nr][nc]:
            visited[nr][nc] = True # 단계 1. 현재 위치를 청소한다
            cnt += 1
print(cnt)