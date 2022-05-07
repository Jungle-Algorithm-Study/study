def solution(new_id):
    answer = ''
    #1번
    new_id = new_id.lower()
    #2번
    for i in new_id :
        if i.isalpha() or i.isdigit() or i in ['-','_','.']:
            answer += i
    #3번
    while '..' in answer:
        answer = answer.replace('..','.')
    #4번
    if answer[0] == '.' :
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.' :
        answer = answer[:-1]
    #5번
    if answer == '' :
        answer = 'a'
    #6번
    if len(answer) >= 16 :
        answer = answer[:15]
        if answer[-1] == '.' :
            answer = answer[:-1]
    #7번
    while len(answer) < 3 :
        answer += answer[-1]
    print(answer)
    return answer