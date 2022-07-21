# 가로 2 세로 1
def solution(n):
    DP = [0]*(n+1)
    DP[1] = 1
    DP[2] = 2
    # DP[2] = DP[1] (-1에서는 세로로 하나 세우기라 그대로) + DP[0] (-2에서는 옆으로 두개 눕히기라 그대로)
    for i in range(3,n+1):
        DP[i] = (DP[i-1] + DP[i-2]) % 1000000007
    return DP[n] 
    