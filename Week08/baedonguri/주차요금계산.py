from collections import defaultdict
import math
# fees = [180, 5000, 10, 600]
# records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

fees = [120, 0, 60, 591]
records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]	

def calc_time(in_time, out_time):
    in_h, in_m = in_time.split(':')
    out_h, out_m = out_time.split(':')
    return int(int(out_h)-int(in_h))*60 + (int(out_m) - int(in_m))

def solution(fees, records):
    db = defaultdict(list)
    db_time = defaultdict(list)
    db_fee = defaultdict(list)

    for record in records:
        time, car_num, command = record.split()
        if command == 'IN':
            db[car_num].append(time)
        elif command == 'OUT':
            in_time = db.pop(car_num)[0]
            total_time = calc_time(in_time, time)
            db_time[car_num].append(total_time)

    if db:
        for key, value in db.items():
            total_time = calc_time(value[0], '23:59')
            db_time[key].append(total_time)
    
    for car_num, times in db_time.items():
        total_time = sum(times)
        if total_time < fees[0]:
            db_fee[car_num] = fees[1]
        else:
            fee = fees[1] + math.ceil((total_time-fees[0])/fees[2]) * fees[3]
            db_fee[car_num] = fee            

    answer = []
    for key, val in db_fee.items():
        answer.append([int(key),val])
    answer.sort(key=lambda x:x[0])
    
    return [i[1] for i in answer]
    


print(solution(fees, records))




