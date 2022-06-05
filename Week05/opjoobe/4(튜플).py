# 7시 6분 시작 # 19min sol
# 첫번째풀이 #비효율의끝
def solution(s):
    tot_L = []
    now_str = ''
    for case in s[1:-1]:
        if case == '{':
            continue
        if case == '}':
            if now_str[0] == ',':
                now_str = now_str[1:]
            now_L = now_str.split(',')
            tot_L.append(now_L)
            now_str = ''
            continue
        now_str += case  
    tot_L.sort(key=lambda x: len(x))
    answer = []
    for now in tot_L:
        for n in now:
            if n not in answer:
                answer.append(n)
    answer = list(map(int, answer))
    return answer

#두번째풀이 #질문하기 슬쩍보고 아이디어 착안해 작성
def solution(s):
    tuple_L = s[2:-2].split('},{')
    tuple_L.sort(key=lambda x: len(x))
    before_s = set()
    answer = []
    for now_l in tuple_L:
        now_s = set(now_l.split(','))
        answer.append(int(now_s.difference(before_s).pop()))
        before_s = now_s
    return answer

s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(s))