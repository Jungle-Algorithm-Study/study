# pgms.64065.튜플

def solution(s):
    answer = []
    
    # 1. },{ 기준으로 split
    s = s.split('},{')
    
    # 2. 남은 {, } 및 ,를 빈칸으로 대체
    s = list(map(lambda x : x.replace('{','').replace('}','').split(','),s))
    
    # 3. casting to int
    s = [[int(x) for x in c] for c in s]
    
    # 4. length로 sort
    s.sort(key = lambda x : len(x))
    
    # 5. 1차원 배열로 merge
    s = [num for array in s for num in array]
    
    # 6.  answer에 append. 이미 들어간 원소의 경우 pass
    for n in s :
        if answer.count(n) :
            continue
        answer.append(n)
    
    return answer
