# 오픈채팅방 
def solution(record):
    user = {}; message = []
    for status, *id_ in map(lambda x: list(x.split()), record):
        if status != 'Change':
            message.append((id_[0], {'Leave':'나갔','Enter':'들어왔'}[status]))
        if status != 'Leave':
            user[id_[0]] = id_[1]
    return [f"{user[m[0]]}님이 {m[1]}습니다." for m in message] 