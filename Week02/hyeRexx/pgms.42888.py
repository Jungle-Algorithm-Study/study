# 채팅방

def solution(records):
    answer = []
    sol = []
    userInfo = {}

    for singleRecord in records :
        record = singleRecord.split(' ')
        
        if record[0] == "Change" : # 변경하면 딕셔너리 갱신하고, 레코드도 갱신함
            userInfo[record[1]] = record[2]
                
        elif record[0] == "Enter" : # 들어오면 레코드에 추가하고 딕셔너리 등록함
            answer.append((record[0], record[1]))
            userInfo[record[1]] = record[2]
            
        elif record[0] == "Leave" : # 나가면 레코드에 추가함
            answer.append((record[0], record[1]))
    
    for ans in answer :
        if ans[0] == "Enter" : # ~님이 들어왔습니다.
            sol.append(f"{userInfo[ans[1]]}님이 들어왔습니다.")
        elif ans[0] == "Leave":
            sol.append(f"{userInfo[ans[1]]}님이 나갔습니다.")    
    
    return sol

  
# Test Case
records = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(records))
