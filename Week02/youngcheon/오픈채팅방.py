# 오픈채팅방 
def solution(record):
    user = {}; message = []
    type_ = {'Leave':'나갔습니다.','Enter':'들어왔습니다.'}
    for i in record:
        status, *id_ = i.split()
        if not status == 'Change':
            message.append((id_[0], type_[status]))
        if not status == 'Leave':
            user[id_[0]]=id_[1]
    return [f"{user[m[0]]}님이 {m[1]}" for m in message]
print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))