# 프로그래머스 # 주차요금계산 # 25min sol

# 입차/출차 기록 -> records (시각 / 차량번호 / 입출차)
# 주차요금 -> fees (기본시간/기본요금/단위시간/단위요금)
# 입차 후에 출차된 내역이 없다면, 23:59에 출차한 것으로 간주
# 00시00분 ~ 23시59분 누적주차시간 <= 기본시간 : 기본요금 청구
# 기본시간 초과분 -> 나누어떨어지지 않으면, 단위시간으로 올림
# 차량번호 작은 자동차부터, 청구할 주차 요금

# 두번째 풀이 # 첫번째 풀이에서 함수를 분리해 더 간단하게 만듬
from collections import defaultdict
def time_to_min(t):
    return int(t[:2])*60 + int(t[-2:])
def solution(fees, records):
    base_time, base_fee, unit_time, unit_fee = fees
    def fee(total_time):
        if total_time <= base_time:
            return base_fee
        else:
            unit_cnt, unit_extra = divmod(total_time - base_time, unit_time)
            if unit_extra:
                unit_cnt += 1
            return base_fee + unit_fee * unit_cnt
    parking_log = defaultdict(int)
    accumulated_time = defaultdict(int)
    for record in records:
        time, car, inout = record.split()
        if inout == 'IN':
            parking_log[car] = time_to_min(time)
        else: # 'OUT'
            accumulated_time[car] += time_to_min(time) - parking_log[car]
            del(parking_log[car])
    closing_time = time_to_min("23:59")
    for car, in_time in parking_log.items():
        accumulated_time[car] += closing_time - in_time
    return [fee(accumulated_time[car]) for car in sorted(accumulated_time.keys())]


# 첫번째 풀이 
from collections import defaultdict
def time_to_min(t):
    return int(t[:2])*60 + int(t[-2:])
def solution(fees, records):
    answer = []
    base_time, base_fee, unit_time, unit_fee = fees
    parking_log = defaultdict(int)
    accumulated_time = defaultdict(int)
    for record in records:
        time, car, inout = record.split()
        if inout == 'IN':
            parking_log[car] = time_to_min(time)
        else: # 'OUT'
            parking_time = time_to_min(time) - parking_log[car]
            accumulated_time[car] += parking_time
            parking_log[car] = -1
    
    for car, in_time in parking_log.items():
        end = time_to_min("23:59")
        if in_time >= 0:
            parking_time = end - in_time
            accumulated_time[car] += parking_time
    
    for car in sorted(accumulated_time.keys()):
        total_time = accumulated_time[car]
        if total_time <= base_time:
            answer.append(base_fee)
        else:
            unit_cnt , extra = divmod(total_time - base_time, unit_time)
            if extra:
                unit_cnt += 1
            answer.append(base_fee + unit_fee * unit_cnt)
                
    return answer