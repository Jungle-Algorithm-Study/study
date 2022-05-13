from sys import stdin
from heapq import heapify, heappop, heappush
input = stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
heapify(arr)
for i in range(m):
    hap = heappop(arr) + heappop(arr)
    for j in range(2): heappush(arr, hap)
print(sum(arr))