from itertools import combinations
def solution(relation):
    answer = []
    row = len(relation) #6
    col = len(relation[0]) #4
    c = []
    for i in range(1, col+1):
        c.extend(combinations(range(col), i))
    for i in c:
        tmp = [tuple([item[key] for key in i]) for item in relation]
        if len(set(tmp))==row:
            flag = True
            for j in answer:
                if set(j).issubset(set(i)):
                    flag = False
                    break
            if flag:
                answer.append(i)
    return len(answer)
#참고해서 풀었음
