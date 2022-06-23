from math import ceil

def calc(fees, time) :
    dtime, dfee, stime, sfee = map(int, fees)

    if time <= dtime :
        return dfee
    return dfee + ceil(((time - dtime) / stime)) * sfee
    
    
def solution(fees, records):
    lots = {}
    total = {}
    rst = []
    
    for record in records :
        time, vnum, inout = record.split()
        h, m = map(int, time.split(":"))
        time = h * 60 + m
        
        if not vnum in total :
            total[vnum] = 0 #총시간
        
        if inout == "IN" :
            lots[vnum] = [vnum, 1, time] #입차 : [1] : flag
            
        elif inout == "OUT" :
            lots[vnum][1] = 0 #출차 : [1] : flag
            total[vnum] += time - lots[vnum][2] #total 반영
    
    for l in lots.values() : #출차하지 않은 차 체크
        if l[1] == 1 :
            total[l[0]] += 1439 - l[2]
    
    for t in sorted(list(total.items())) : #값 계산
        rst.append(calc(fees, t[1]))

    return 
