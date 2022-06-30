#프로그래머스 #베스트앨범 #17min sol #폰코딩
from collections import Counter, defaultdict
def solution(genres, plays):
    answer = []
    plays_by_genre = []
    
    N = len(plays)
    songs_by_genre = defaultdict(list)
    
    for id in range(N):
        genre, play = genres[id], plays[id]
        songs_by_genre[genre].append([play, id])
        
    for genre in songs_by_genre.keys():
        
        songs_by_genre[genre].sort(key = lambda x: (-x[0], x[1]))
        
        plays_by_genre.append([genre,sum([x[0] for x in songs_by_genre[genre]])])
    
    plays_by_genre.sort(key = lambda x: -x[1])
    
    for genre, cnt in plays_by_genre:
        now_songs = songs_by_genre[genre]
        
        answer.append(now_songs.pop(0)[1])
        if not now_songs:
            continue
        answer.append(now_songs.pop(0)[1])
    return answer