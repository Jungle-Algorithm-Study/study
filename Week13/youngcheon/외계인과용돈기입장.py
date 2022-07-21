input = __import__('sys').stdin.readline
n,m = map(int, input().split())
money = list(map(int,input().split()))
dp = [0]*(len(money)+1)
dp[1] = money[0]
for i in range(2,len(dp)):
	dp[i] = dp[i-1]+money[i-1]
for _ in range(m):
	a, b = map(int, input().split())
	answer = dp[b]-dp[a-1]
	print('+'+str(answer) if answer > 0 else answer)