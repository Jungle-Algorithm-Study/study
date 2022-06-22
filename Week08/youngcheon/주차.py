from collections import defaultdict
from math import ceil
def solution(fees, records):
    dic = defaultdict(int)
    for i in records:
        time, car, status = i.split()
        temp = list(map(int,time.split(':')))
        time = temp[0]*60+temp[1]
        if status == 'IN':
            dic[car] += time
        else:
            dic[car] -= time
    answer = []
    for k,v in dic.items():
        fee = v-(23*60+59) if v>=0 else v
        total = fees[1] + ceil((abs(fee)-fees[0])/fees[2]) * fees[3]
        answer.append([fees[1] if total < fees[1] else total , k])
    answer.sort(key= lambda x: x[1])
    return list(map(lambda x: x[0], answer))