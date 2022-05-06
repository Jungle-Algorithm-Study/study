# 시작: 14:02
# 종료: 14:20
def solution(record):
    '''
    1. 가장 마지막에 갱신된 정보만 필요하므로, answer에는 user_id와 user_name만 저장해둔다.
    2. 
    '''
    answer = []
    
    # 가장 최신의 닉네임을 저장해둘 딕셔너리
    id_to_name = dict()
    
    for r in record:
        user_action, *user_id_name = r.split()
        
        user_id = user_id_name[0]
        
        
        # 닉네임 갱신
        if user_action in ("Enter", "Change"):
            user_name = user_id_name[-1]
        	id_to_name[user_id] = user_name
            
            
            
        ## 채팅방에 기록이 남는 액션만 모음
        # action 0 == Enter
        if user_action == 'Enter':
            user_log.append((0,user_id))
            
        # action 1 == Leave
        elif user_action == 'Leave':
            user_log.append((1,user_id))
            
            
    # action별 메시지        
    message = ["님이 들어왔습니다.", "님이 나갔습니다."]
    
    # user_action과 user_id를 넣으면 출력 형식에 맞게 바꿔줌
    decode = lambda user_action, user_id : f"{id_to_name[user_id] + message[user_action]}"
    
    answer = [decode(a, i) for a,i in user_log]
    
    return answer
