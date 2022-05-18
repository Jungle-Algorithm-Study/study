'''
P = 사람
O = 빈 테이블
X = 파티션
'''
def check(graph):
    dx, dy = [1,0],[0,1] #1칸이동
    ddx, ddy = [1,1],[1,-1] #대각선이동
    for i in range(5):
        for j in range(5):
            # P인 경우만 검사함
            if graph[i][j] != 'P':
                continue
            # 한칸 옆에 다른사람이 앉았을 경우
            for k in range(2):
                nx, ny = i+dx[k],j+dy[k]
                if 0<=nx<5 and 0<=ny<5 and graph[nx][ny]=='P':
                    return 0
            # 두칸 떨어져 있는데 가운데에 빈테이블이 있는경우
            for k in range(2):
                nx, ny = i+dx[k]*2, j+dy[k]*2
                if 0<=nx<5 and 0<=ny<5 and graph[nx][ny]=='P':
                    if graph[i+dx[k]][j+dy[k]] == 'O':
                        return 0
            # 대각선 자리 사이에 빈테이블이 있는경우
            for k in range(2):
                nx, ny = i+ddx[k], j+ddy[k]
                if 0<=nx<5 and 0<=ny<5 and graph[nx][ny]=='P':
                    if graph[nx][j]=='O' or graph[i][ny]=='O':
                        return 0
    return 1
                
            
def solution(places):
    answer = [check(i) for i in places] 
    return answer