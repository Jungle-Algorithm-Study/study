def solution(brown, yellow):
    answer = []
    cnt = brown + yellow
    
    for i in range(3, 100000) :
        if cnt % i != 0 :
            continue
        else :
            for j in range(3, 100000) :
                if i * j == cnt :
                    if (i-2) * (j-2) == yellow :
                        answer.append(j)
                        answer.append(i)
                        return answer
