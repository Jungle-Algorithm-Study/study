def solution(begin, target, words):
    answer = []
    visited = [0 for _ in range(len(words))]
    # 두 단어가 한자리만 다른지 체크하는 함수
    check = lambda w1,w2 : sum([1 for a,b in zip(w1,w2) if a==b])+1 == len(w1)
    
    # dfs함수
    def dfs(word, array, target, count):
        if word == target: #dfs끝까지 도달하면 answer에 append
            answer.append(count)
        for i in range(len(visited)):
        	# 조건을만족하고 visited하지 않은 단어면
            if check(word, words[i]) and not visited[i]:
                visited[i] = 1
                dfs(words[i],words,target,count+1)
                # dfs문이 끝났다는 것은 target에 도달했다는 뜻. 
                # visited를 다시 미방문 처리(백트래킹)하여 다른 경우의 수 탐색
                visited[i] = 0 
    # words에 target이 없다면 0을 반환 (dfs 수행x)
    if target not in words:
        return 0
    # dfs 수행
    dfs(begin, words, target, 0)
    # 최소값 반환
    return min(answer)
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))