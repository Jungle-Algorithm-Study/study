from collections import defaultdict
from math import ceil
def solution(fees, records):
    dic = defaultdict(int)
    for i in records:
        time, car, status = i.split()
        time = int(time[:2])*60+int(time[-2:])
        if status == 'IN':
            dic[car] -= time
        else:
            dic[car] += time
            
    for k,v in dic.items():
        fee = v+(23*60+59) if v<=0 else v
        total = fees[1] + ceil((fee-fees[0])/fees[2]) * fees[3]
        dic[k] = fees[1] if total < fees[1] else total
        
    return [v for k,v in sorted(dic.items())]