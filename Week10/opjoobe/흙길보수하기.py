# 백준 # 흙길보수하기 # 5시 13분 시작 # 5시 33분 끝 # 20min sol
import sys
input = sys.stdin.readline

N, L = map(int, input().strip().split())

pools = [list(map(int, input().strip().split())) for _ in range(N)]
pools.sort(key = lambda x: (x[0], x[1])) # 정렬 후에, start가 더 작아지면 안될듯

def sol(pools, N, L):
    now = 0
    cnt = 0
    for start, end in pools:
        if start > now:
            now = start
        if end <= now:
            continue
        need, rest = divmod(end - now, L)
        if rest:
            need += 1
            end += L-rest
        cnt += need
        now = end
    return cnt

print(sol(pools, N, L))