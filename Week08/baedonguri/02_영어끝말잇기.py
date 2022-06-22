def solution(n, words):
    check_lst = [words[0]]
    answer = [0,0]
    num = 0
    for i in range(len(words)-1):
        num += 1
        if words[i+1] not in check_lst and words[i][-1] ==  words[i+1][0] and len(words[i+1]) > 1:
            check_lst.append(words[i+1])
        else:
            tmp = (num%n)+1
            answer[0] = tmp
            answer[1] = num // n+1
            break
    return answer
        
   
n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(n, words))
