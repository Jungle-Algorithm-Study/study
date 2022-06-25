from collections import defaultdict
from heapq import heapify, heappop

genres = ["classic", "pop", "classic", "classic", "pop"]	
plays = [500, 600, 150, 800, 2500]	
# genres = ["classic", "pop", "classic", "classic", "classic"]
# plays = [500, 1000, 400, 300, 200]


def solution(genres, plays):
    play_list = defaultdict(list)
    # 장르별로 음악 분류하기
    for idx, box in enumerate(zip(plays, genres)):
        play, genre = box
        play_list[genre].append((-play, idx, genre)) # 재생시간, 고유번호, 장르를 저장, 재생시간은 heap 사용을 위해 음수 취함

    rank = defaultdict(list)
    answer = []
    # 장르 합산 순위 결정
    for genre, lst in play_list.items():
        cal_sum = sum([-i[0] for i in lst])
        rank[cal_sum] = lst[-1][-1]   
    # 장르 합산 점수가 높은 장르부터 2개씩 뽑음
    for ranking in sorted(rank.keys(), reverse=True):
        genre = rank[ranking]
        heapify(play_list[genre])
        if len(play_list[genre]) < 2: # 음악이 1개뿐인 경우
            answer.append(heappop(play_list[genre])[1])
        else:
            for i in range(2): # 그 이상은 2개씩 뽑음
                answer.append(heappop(play_list[genre])[1])
    return answer
    
print(solution(genres, plays))
