N, M = map(int, input().split())
log = [*map(int, input().split())]
DP = [0] * (N+1)

for i in range(1, N+1):
    DP[i] = DP[i-1] + log[i-1]

for _ in range(M):
    s,e = map(int, input().split())
    ans = DP[e]-DP[s-1]

    if ans > 0: print('+',end='')

    print(ans)
