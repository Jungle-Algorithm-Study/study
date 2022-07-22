# 구름 # 주유소 # 15min sol

N = int(input())
dist = list(map(int, input().strip().split()))
cost = list(map(int, input().strip().split()))

# [현재까지의 최소비용, 현재까지의 누적비용]

DP = [cost[0], 0]
for i in range(1,N):
	DP[1] = dist[i-1] * DP[0] + DP[1]
	DP[0] = min(cost[i], DP[0])
	
print(DP[1])