def solution(genres, plays):
    answer = []
    allgen = {}
    gen = []
    
    for i in range(len(genres)) :
        if not genres[i] in allgen :
            allgen[genres[i]] = [0, genres[i]]
            
        allgen[genres[i]][0] += plays[i]
        allgen[genres[i]].append((plays[i], i))
    
    parsed = list(allgen.values())
    
    for p in parsed :
        gen.append(p[:2])
        allgen[p[1]] = p[2:]
        
    gen = sorted(gen, reverse = True)
        
    for i in range(len(gen)) :
        songs = sorted(allgen[gen[i][1]], key = lambda x : (-x[0], x[1]))
        
        if len(songs) < 2 :
            answer.append(songs[0][1])
            continue
            
        answer.append(songs[0][1])
        answer.append(songs[1][1])

    return answer
