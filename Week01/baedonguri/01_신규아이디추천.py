import sys
input = sys.stdin.readline


def solution(new_id):
    #1 모두 소문자로 변경
    new_id = new_id.lower()

    #2 알파벳 혹은 숫자이거나 허용한 특수문자일 경우 answer 문자열에 추가
    answer = ''
    for s in new_id:
        if s.isalnum() or s in ['-','_','.']:
            answer += s
    #3 ".."가 있다면 '.'으로 치환
    while '..' in answer:
        answer = answer.replace('..', '.')
    #4 시작 혹은 마지막 지점에 '.'가 있다면 시작지점 이후의 문자열만 저장 ㄷ
    if answer[0] == '.': 
        if len(answer) >= 2:
            answer = answer[1:]

    if answer[-1] == '.': answer = answer[:-1]

    #5 만약 위의 단계를 거치고 나서 빈 문자열이 되었을 경우 'a'를 넣어줌
    if answer == '': answer = 'a'

    #6 만약 아이디의 길이가 16이상이면 문자열을 잘라줌
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.': # 문자열을 잘랐을 때 마지막이 .이라면 끝을 제외한 나머지를 저장
            answer = answer[:-1]
    #7 만약 최종 아이디의 길이가 3 미만이라면 길이가 3이 될때까지 아이디의 마지막 문자를 추가
    while len(answer) < 3:
        answer += answer[-1]

    return answer


ans = "=.="
print(solution(ans))
