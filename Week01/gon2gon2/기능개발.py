# 시작: 23:52
# 종료: 00:09
def solution(progresses, speeds):
    '''
    진도가 100이 되면 서비스 반영 가능
    progresses  : 최초 작업 진도가 적힌 배열(순서대로 배포되어야 함)
    speeds      : 작업별 하루 개발 속도
    
    return: 한번에 몇개의 기능이 배포되는지
    
    progresses에 id도 같이 기록해두고, while q and q[0] > 100을 이용해
    맨 앞부터 작업완료되는 대로 popleft한 다음 temp에 append
    
    '''
    
    answer = []
    
    # id를 같이 넣어주는 이유: progresses에서 원소를 popleft하더라도 id를 이용해서 속도를 참조할 수 있게
    from queue import deque
    progresses = [[i, v] for i, v in enumerate(progresses)]
    progresses = deque(progresses)

    # 남은 작업이 있는 동안
    while progresses:
        temp = 0 # 배포되는 작업의 수
        
        # 맨 앞부터 배포할 수 있는 작업들을 하나씩 빼고 temp에 저장
        while progresses and progresses[0][1] >= 100:
            progresses.popleft()
            temp += 1
            
        # 만약 배포할 작업이 있으면 answer에 그 개수를 append
        if temp:
            answer.append(temp)
    
        # 남은 작업들의 진도를 올려줌
        for i in range(len(progresses)):
            p_id = progresses[i][0]
            progresses[i][1] += speeds[p_id]
    
    return answer
