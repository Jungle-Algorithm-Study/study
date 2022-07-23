# 구름 # 외계인과 용돈기입장 # 15min sol
#살아온 날짜, 궁금한 구간 숫자
#그날의 수입 혹은 지출
#3째줄부터 M개의 줄

N, M = map(int, input().split())
DP = [0] * (N+1)

L = input().split()
for i in range(1, N+1):
	DP[i] = int(L[i-1]) + DP[i-1]

for _ in range(M):
	s, e = map(int, input().split())
	result = DP[e] - DP[s-1]
	print('+' + str(result) if result > 0 else result)