# 프로그래머스 # 정수삼각형 # 28min sol
def solution(triangle):
    n = len(triangle)
    DP = [[0]*i for i in range(1,n+1)]
    DP[0][0] = triangle[0][0]
    for i in range(1,n):
        DP[i][0] = DP[i-1][0] + triangle[i][0]
        DP[i][i] = DP[i-1][i-1] + triangle[i][i]
        for j in range(1,i):
            DP[i][j] = max(DP[i-1][j-1], DP[i-1][j]) + triangle[i][j]
    return max(DP[-1])

#     DP[1][0] = DP[0][0] + triangle[1][0]
#     DP[1][1] = DP[0][0] + triangle[1][1]
    
#     DP[2][0] = DP[1][0] + triangle[2][0]
#     DP[2][2] = DP[1][1] + tirangle[2][2]
    
#     DP[3][0] = DP[2][0] + triangle[3][0]
    
#     DP[3][1] = DP[2][0] 
#     DP[3][1] = DP[2][1]
    
#     DP[3][3] = DP[2][2] + triangle[3][3]
