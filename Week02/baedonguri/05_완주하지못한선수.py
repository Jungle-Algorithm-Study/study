def solution(participant,completion):
    hashSum = 0
    hashDic = {}
    
    for p in participant:
        hashDic[hash(p)] = p
        hashSum += hash(p)

    for c in completion:
        hashSum -= hash(c)

    return hashDic[hashSum]

print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))