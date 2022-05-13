## [프로그래머스] 파일명 정렬 (python)
## https://programmers.co.kr/learn/courses/30/lessons/17686

def solution(files):
    datas = []
    for f in files:
        head,number,tail = '','',''
        flag = False
    
        for i in range(len(f)):
            if f[i].isdigit(): # number를 우선적으로 취하고, flag를 True로 취함
                number += f[i]
                flag = True
            elif not flag: # f[i]가 숫자가 아니고 flag가 False일 경우 head를 먼저 취하게 됨
                head += f[i]
            else: # number 이후로 오는 문자를 모두 tail에 넣어줌
                tail += f[i:]
                break
        datas.append((head,number,tail))

    tmp = sorted(datas, key=lambda x :(x[0].lower(),int(x[1])))

    return [f"{i[0]}{i[1]}{i[2]}" for i in tmp]



print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))