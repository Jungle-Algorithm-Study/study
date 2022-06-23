from collections import defaultdict
from math import ceil

def solution(fees, records):
    answer = []
    stand_time, stand_fare, add_time, add_fare = fees
    sibal = defaultdict(list)
    money = []
    
    def cal_fee(minute) :
        final_fare = 0
        if minute > stand_time :
            final_fare = stand_fare + ceil((minute-stand_time) / add_time) * add_fare
        else :
            final_fare = stand_fare
        return final_fare
    
    for record in records :
        time, car, in_out = record.split(" ")
        time = int(time[:-3])*60 + int(time[3:])
        sibal[car].append((time, in_out))
    print(sibal)
    for key, val in sibal.items() :
        diff_time = 0
        for real_time, status in val :
            if len(val) % 2 == 0 :
                if status == 'IN' :
                    diff_time -= real_time
                else : 
                    diff_time += real_time
            else :
                last = sibal[key].pop()
                diff_time += (23*60 +59) - int(last[0])
                if len(sibal[key]) !=0 :
                    if status == 'IN' :
                        diff_time -= real_time
                    else : 
                        diff_time += real_time
        result_fare = cal_fee(diff_time)
        money.append((key,result_fare))
        money.sort()
    for i in money :
        answer.append(i[1])
                            
    return answer
