# 오픈채팅방
def solution(record):
    answer = []
    user = {}
    for r in record:
        order, *rest = r.split()
        if order == 'Enter':
            user[rest[0]] = rest[1]
            answer.append([rest[0], '님이 들어왔습니다.'])
        elif order == 'Leave':
            answer.append([rest[0], '님이 나갔습니다.'])
        else: # 'Change'
            user[rest[0]] = rest[1]
    return [user[line[0]]+line[1] for line in answer]

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))