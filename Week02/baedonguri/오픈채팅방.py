def solution(records):
    answer = []
    members = {}
    # Enter와 Change를 우선적으로 처리
    for record in records:
        status, id_, *nickname = record.split()
        if status == 'Enter' or status == 'Change':
            members[id_] = nickname
            
    # Enter와 Leave를 처리 후 리스트에 저장
    for record in records:
        status, id_, *nickname = record.split()

        member = members[id_][0]
        if status == 'Enter':
            answer.append(f'{member}님이 들어왔습니다.')
        elif status == 'Leave':
            answer.append(f'{member}님이 나갔습니다.')

    return answer
