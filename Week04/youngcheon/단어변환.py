answer = []

check = lambda w1,w2 : sum([1 for a,b in zip(w1,w2) if a==b])+1 == len(w1)
    
def dfs(word, array, target, count):
    if word == target: 
        return count
    for i in range(len(array)):
        if check(word, array[i]):
            answer.append(dfs(array[i],array[:i]+array[i+1:],target,count+1))
    return 99999

def solution(begin, target, words):
    if target not in words:
        return 0
    dfs(begin, words, target, 0)
    return min(answer)

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))