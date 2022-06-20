import heapq

def dijsktra(start,n):
    min_fare = [int(1e9)] * (n+1)
    min_fare[0] = 0
    heap = [(0,start)]
    
    while heap :
        each_cost, now = heapq.heappop(heap)
        
        if each_cost > min_fare[now] :
            continue
        
        for i in road[now] :
            cost = i[1] + each_cost 
            if cost < min_fare[i[0]] :
                min_fare[i[0]] = cost
                heapq.heappush(heap,(cost,i[0]))
    return min_fare

def solution(n, s, a, b, fares):
    global road 
    road = [[] for i in range(n+1)] 
    
    for node1, node2, fare in fares :
        road[node1].append((node2, fare))
        road[node2].append((node1, fare))
    min_fare = dijsktra(s,n)
    cost = min_fare[a] + min_fare[b]
    for i in range(1,n+1) :
        if s != i :
            min_fare = dijsktra(i,n)
            cost = min(cost, min_fare[s] + min_fare[a] + min_fare[b])
    
    return cost
