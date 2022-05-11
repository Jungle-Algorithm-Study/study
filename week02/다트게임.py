def solution(dartResult):
    answer = 0
    before = []
    bonus = {'S':1,'D':2,'T':3}
    tmp = 0
    for i in dartResult :
        if i.isdigit():
            if i == '0' :
                if tmp != 1 :
                    answer += tmp
                    before.append(tmp)
                    tmp = 0
                else :     
                    tmp = 10
            else : 
                answer += tmp
                before.append(tmp)
                tmp = 0
                tmp += int(i)
        elif i in ['S','D','T']:
            tmp = tmp ** bonus[i]
        elif i == '*' :
            answer = before[-1] + answer
            tmp = tmp *2
        elif i == '#' :
            tmp = tmp*(-1)
    answer += tmp
            
    return answer
