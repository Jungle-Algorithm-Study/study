# 오픈채팅방 
def solution(record):
    user = {}; message = []
    for s, *id_ in map(lambda x: list(x.split()), record):
        if s != 'Change':
            message.append((id_[0], {'L':'나갔','E':'들어왔'}[s[0]]))
        if s != 'Leave':
            user[id_[0]] = id_[1]
    return [f"{user[i]}님이 {m}습니다." for i, m in message]