input = __import__('sys').stdin.readline
import sys
sys.setrecursionlimit(10**5)
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
visited = [[0]*n for _ in range(n)]
dx, dy = [1,-1,0,0], [0,0,-1,1]
answer = 0
def dfs(x, y):
    if not visited[x][y]:
        visited[x][y] = 1
        for i in range(4):
            nx, ny = dx[i]+x, dy[i]+y
            if 0<=nx<n and 0<=ny<n:
                if graph[x][y] > graph[nx][ny]:
                    dp[x][y] = max(dp[x][y], dfs(nx,ny))
    return dp[x][y] + 1
for i in range(len(graph)):
    for j in range(len(graph[0])):
        answer = max(answer, dfs(i,j))
print(answer)