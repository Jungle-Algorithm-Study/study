def solution(n, lost, reserve):
    '''
    여벌이 있어도 도난당했으면 빌려줄 수 없음
    최대한 빌려주고 끝까지 못빌린 학생 수
    앞에서부터 pop을 해야 됨
    '''
    answer = n
    
    lost, reserve = set(lost), set(reserve)
    lost_and_reserve = lost & reserve
    
    lost = list(lost - lost_and_reserve)
    reserve = list(reserve - lost_and_reserve)
    
    while reserve:
        r = reserve.pop(0)
        
        if r-1 in lost:
            lost.remove(r-1)
        elif r+1 in lost:
            lost.remove(r+1)
    
    return answer - len(lost)
