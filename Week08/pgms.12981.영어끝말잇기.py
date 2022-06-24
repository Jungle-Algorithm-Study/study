def solution(n, words):
    word = set()

    for i in range(len(words)) :
        word.add(words[i])
        
        # case 1 : 앞 사람의 끝 글자와 다른 글자를 말했을 때
        if i > 0 and words[i][0] != words[i - 1][-1] :
            return [(i % n) + 1,  (i // n) + 1] # turn, game count
    
        # case 2 : 중복된 단어를 말했을 때
        if len(word) != i + 1 :
            return [(i % n) + 1,  (i // n) + 1]
    
    # case 3 : 게임이 중간에 끝나지 않았을 때 
    return [0, 0]
    
