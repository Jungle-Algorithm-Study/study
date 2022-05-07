# 카드 합체 놀이

from heapq import heapify, heappop, heappush

cardCnt, tryCnt = map(int, input().split())
cards = [int(x) for x in input().split()]

heapify(cards)

for _ in range(tryCnt) :
    a, b = heappop(cards), heappop(cards)
    new = a + b
    heappush(cards, new)
    heappush(cards, new)

print(sum(cards))
