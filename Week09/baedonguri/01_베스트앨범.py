from collections import defaultdict
from heapq import heapify, heappop

genres = ["classic", "pop", "classic", "classic", "pop"]	
plays = [500, 600, 150, 800, 2500]	
# genres = ["classic", "pop", "classic", "classic", "classic"]
# plays = [500, 1000, 400, 300, 200]


def solution(genres, plays):
    play_list = defaultdict(list)
    for idx, box in enumerate(zip(plays, genres)):
        play, genre = box
        play_list[genre].append((-play, idx, genre))

    rank = defaultdict(list)
    answer = []
    for genre, lst in play_list.items():
        cal_sum = sum([-i[0] for i in lst])
        rank[cal_sum] = lst[-1][-1]   

    for ranking in sorted(rank.keys(), reverse=True):
        genre = rank[ranking]
        heapify(play_list[genre])
        if len(play_list[genre]) < 2:
            answer.append(heappop(play_list[genre])[1])
        else:
            for i in range(2):
                answer.append(heappop(play_list[genre])[1])
    return answer
    
print(solution(genres, plays))
