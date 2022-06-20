# 나의 이상한 풀이...
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

# 수정한 풀이
def solution(brown, yellow):
    cnt = brown + yellow
    
    for i in range(3, 100000) :
        if cnt % i != 0 :
            continue
        else :
            j = cnt // i
            if (i-2) * (j-2) == yellow :
                return [j,i]
