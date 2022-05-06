from collections import defaultdict
def solution(record):
    user = defaultdict(list)
    message = []
    for i in record:
        if 'Leave' in i:
            status, id_ = i.split()
            message.append((id_, "나갔습니다."))
        else:
            status, id_, nickname = i.split()
            user[id_].append(nickname)
            if status == 'Enter':
                message.append((id_,"들어왔습니다."))
    return [f"{user[m[0]][-1]}님이 {m[1]}" for m in message]
