def solution(record):
    answer = []
    dic = {}
    
    for info in record :
        each_info = info.split()
        if len(each_info) == 3:
            dic[each_info[1]] = each_info[2]
    
    for info in record :
        each_info = info.split()
        if each_info[0] == "Enter" :
            answer.append(f"{dic[each_info[1]]}님이 들어왔습니다.")
        elif each_info[0] == "Leave" :
            answer.append(f"{dic[each_info[1]]}님이 나갔습니다.")
    

    return answer
