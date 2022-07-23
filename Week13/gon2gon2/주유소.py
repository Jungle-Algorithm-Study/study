N = int(input())
COST = [*map(int, input().split()[:-1])]
DIST = [*map(int, input().split())]
answer = 0
minimum = COST[0]

for c,d in zip(COST, DIST):
	
    if c < minimum:
        minimum = c

    answer += minimum*d

print(answer)
