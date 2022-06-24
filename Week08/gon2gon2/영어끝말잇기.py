def solution(n, words):
    prev = words[0][0]
    이미말한단어 = dict()
    
    for i in range(len(words)):
        now_word = words[i]
        turn, num = divmod(i, n)
        
        if prev[-1] != now_word[0] or now_word in 이미말한단어:
            return [num + 1, turn + 1]
        
        prev = now_word
        이미말한단어[now_word] = 1
        
    return [0, 0]
