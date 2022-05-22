begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

def check_word(word1, word2):
    check_num = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            check_num += 1
    
    return 1 if check_num == 1 else 0

def dfs(now, target ,words, cnt):
    if now == target:
        return cnt 

    ans = 99999
    for i in range(len(words)):
        if check_word(now, words[i]):
            result = dfs(words[i], target ,words[:i]+words[i+1:], cnt+1)
            ans = min(ans, result)
            
    return ans


def solution(begin, target, words):    
    if target not in words:
        return 0
     
    ans  = dfs(begin, target, words, 0)
    return ans
    
print(solution(begin, target, words))

        









