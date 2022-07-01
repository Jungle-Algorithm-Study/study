from collections import defaultdict
def solution(genres, plays):
    answer = []

    play_of_genres = defaultdict(set)
    counts_of = defaultdict(int)

    for i, (g, p) in enumerate(zip(genres, plays)):
        play_of_genres[g].add((p, i))
        counts_of[g] += p


    for k, v in sorted(counts_of.items(), key = lambda x: x[1], reverse = True):  # 정렬 1
        songs = sorted(play_of_genres[k], key = lambda x: (-x[0], x[1]))          # 정렬 2, 3

        for i in range(min(2, len(songs))): # 최대 두 곡만 저장하도록
            answer.append(songs[i][1])

    return answer
