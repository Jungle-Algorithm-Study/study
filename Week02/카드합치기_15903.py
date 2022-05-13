import sys
import heapq
input = sys.stdin.readline
a, b = map(int,input().split())
card = list(map(int, input().split()))
heapq.heapify(card)
card.sort()

for i in range(b):
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    sum = a+b
    heapq.heappush(card, sum)
    heapq.heappush(card, sum)
sum = 0
for i in card :
    sum += i

print(sum)
