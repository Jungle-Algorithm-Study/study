from math import ceil

convert = lambda x: int(x.split(":")[0]) * 60 + int(x.split(":")[1])
MAX_TIME = convert("23:59")

def solution(fees, records):
    answer = []
    
    # 각각 출차관리와 총 
    enter_time_of = dict()
    stay_time_of = dict()
    
    # 기본 시간, 기본 요금, 단위 시간, 단위 요금
    base_time, base_fee, unit_time, unit_fee = fees
    
    for r in records:
        time, number, status = r.split()
        time = convert(time)
        
        
        if status == "IN": # 입차인 경우
            enter_time_of[number] = time
            if number not in stay_time_of:
                stay_time_of[number] = 0
                
        else:
            stay_time = time - enter_time_of[number]
            stay_time_of[number] += stay_time
            enter_time_of[number] = -1 # 입차만 하고 안 나간 경우를 위해 출차한 경우 마킹
            
    numbers = sorted(stay_time_of.keys())
    
    for number in numbers:
        parking_fee = base_fee
        
        # 안 나간 차량 출차처리
        if enter_time_of[number] != -1:
            stay_time_of[number] += MAX_TIME - enter_time_of[number]
            enter_time_of[number] = -1
            
        # 부등호 주의
        if stay_time_of[number] > base_time:
            parking_fee += ceil((stay_time_of[number] - base_time)/unit_time) * unit_fee
            
        answer.append(parking_fee)
        
    return answer
