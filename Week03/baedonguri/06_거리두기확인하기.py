from collections import deque

place = ["POOOP", 
         "OXXOX",
         "OPXPX", 
         "OOXOX", 
         "POXXP"]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def solution(places):
    answer = []
    for place in places:
        loc = person_loc(place)
        result = bfs(loc, place)
        answer.append(result)
    return answer

def person_loc(place):
    persons = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                persons.append((i,j))
    return persons
            
def bfs(persons, room):
    que = deque(persons)
    checked = [[0]*5 for _ in range(5)]
    
    while que:
        v = que.popleft()
        checked[v[0]][v[1]] = 1

        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]

            if checked[nx][ny] == 3:
                continue
            if 0 <= nx < 5 and 0 <= ny < 5 and not checked[nx][ny]:
                if room[nx][ny] != 'X':
                    checked[nx][ny] = checked[v[0]][v[1]] + 1
                    que.append((nx,ny))
                if room[nx][ny] == 'P':
                    return 0
    return 1


print(solution(place))
# manhatten dist : |a1-b1|+|a2-b2|