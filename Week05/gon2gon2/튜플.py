def solution(s):
    
    tuples = [*map(lambda x: x.replace("{",'').replace("}","").split(","), s.split("},"))]
    tuples.sort(key=lambda x:len(x))

    # 원소 갯수대로 정렬하고 새로 생긴 원소만 answer에 append
    answer = [int(tuples[0][0])]
    for i in range(1, len(tuples)):
        prev, now = tuples[i-1], tuples[i]
        answer.append(int((set(now) - set(prev)).pop()))
        
    return answer
