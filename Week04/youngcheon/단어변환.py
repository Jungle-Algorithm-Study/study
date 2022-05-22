def solution(begin, target, words):
    answer = []
    visited = [0 for _ in range(len(words))]
    check = lambda w1,w2 : sum([1 for a,b in zip(w1,w2) if a==b])+1 == len(w1)
    def dfs(word, array, target, count):
        if word == target: 
            answer.append(count)
        for i in range(len(visited)):
            if check(word, words[i]) and not visited[i]:
                visited[i] = 1
                dfs(words[i],words,target,count+1)
                visited[i] = 0
    if target not in words:
        return 0
    dfs(begin, words, target, 0)
    return min(answer)

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))