answer = []
def check(w1, w2):
    return sum([1 for a,b in zip(w1,w2) if a==b])+1 == len(w1)
    
def dfs(word, array, target, count):
    if word == target:
        return count
    for i in array:
        if check(word, i):
            result = dfs(i,array[:array.index(i)]+array[array.index(i)+1:], target, count+1)
            answer.append(result)
    return 99999

def solution(begin, target, words):
    if target not in words:
        return 0
    dfs(begin, words, target, 0)
    return min(answer)

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))