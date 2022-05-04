def solution(info, query):
    answer = [0] * (len(query))
    inform = []
    stand = []
    for i in range(len(info)) :
        inform.append(info[i].split(' '))
    for i in range(len(query)) :
        stand.append(query[i].replace(' and',''))
        stand[i] = stand[i].split(' ')

    #stand 경우를 돌아가면서 검색
    for i in range(len(stand)) :
        #지원자 한명씩 돌아가면서 검색
        for j in range(len(inform)) :
            chk = 0
            # 각 지원자의 항목을 비교하기 위한것
            for k in range(4) :
                if stand[i][k] != inform[j][k] :
                    if stand[i][k] != '-' :
                        chk = 1
                        break
            if chk == 0 :
                if int(stand[i][4]) <= int(inform[j][4]):
                    answer[i] += 1
    return answer