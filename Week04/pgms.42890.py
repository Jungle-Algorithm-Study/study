from itertools import combinations

def solution(relation) :
    row = len(relation) # row cnt
    col = len(relation[0]) # att cnt
    
    # 가능한 모든 조합 만들기 (att)
    combi = []
    for i in range(1, col + 1) :
        combi.extend(combinations(range(col), i))
        
        
    unq = []
    for i in combi :
        # combi att no로 새로운 키 제작
        tmp = [tuple([item[key] for key in i]) for item in relation]
        
        if len(set(tmp)) == row : 
            flag = True
            
            for x in unq :
                if set(x).issubset(set(i)) : # 부분 집합 확인
                    flag = False
                    break
            
            if flag : # 부분 집합 통과한 경우만 append
                unq.append(i)
    
    return len(unq)

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],
            ["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation)) # 2
