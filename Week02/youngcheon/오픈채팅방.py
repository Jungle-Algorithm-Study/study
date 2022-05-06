# 오픈채팅방 
def solution(record):
    user = {}; message = []
    for i in record:
        status, *id_ = i.split()
        if not status == 'Change':
            message.append((id_[0], {'Leave':'나갔습니다.','Enter':'들어왔습니다.'}[status]))
        if not status == 'Leave':
            user[id_[0]]=id_[1]
    return [f"{user[m[0]]}님이 {m[1]}" for m in message]