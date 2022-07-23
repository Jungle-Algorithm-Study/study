input = __import__('sys').stdin.readline
n = int(input())
distances = list(map(int, input().split()))
cheaperStation, *stations = map(int, input().split())

totalCost = 0
for Station, Distance in zip(stations, distances):
	totalCost += cheaperStation * Distance
	cheaperStation = min(cheaperStation, Station)
print(totalCost)