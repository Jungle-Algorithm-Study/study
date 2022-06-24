from collections import defaultdict
def solution(genres, plays):
    answer = []
    playlist = defaultdict(int)
    idxlist = defaultdict(list)
    for i in range(len(genres)) :
        playlist[genres[i]] += int(plays[i])
        idxlist[genres[i]].append((plays[i],i))
        
    playlist = sorted(playlist.items(), key = lambda item: item[1], reverse = True)
    for i in idxlist.keys() :
        idxlist[i].sort(key = lambda x: x[1])
        idxlist[i].sort(key = lambda x: x[0], reverse = True)
        ''' 위의 두 정렬을 한번에 할 수 있는 획기적인 방법! -x[0]을 기준으로 정렬하면 플레이곡수는 내림차순으로 정렬할 수 있음(고니고니 선수입장)'''
        # idxlist[i].sort(key = lambda x: (-x[0], x[1]))
        
    for i in range(len(playlist)) :
        for j in range(min(2, len(idxlist[playlist[i][0]]))):
            result = idxlist[playlist[i][0]][j][1]
            answer.append(result)
    return answer
