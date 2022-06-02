import re
def solution(s):
    answer= []
    s = list(filter(lambda x: x not in ['',','], re.split('[{}]',s)))
    s.sort(key=lambda x: len(x))
    for i in s:
        if len(i) == 1:
            answer.append(i)
        else:
            temp = list(i.split(','))
            for j in answer:
                temp.remove(j)
            answer.extend(temp)
    return list(map(int, answer))

# COUNTER
import re
from collections import Counter
def solution(s):
    return [int(k) for k,v in sorted(Counter(re.findall('\d+',s)).items(),key=lambda x:x[1],reverse = True)]