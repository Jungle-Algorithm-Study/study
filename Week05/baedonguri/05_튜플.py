def solution(string):
    s = string.split('},{')
    s = [i.replace('{','').replace('}','').split(',') for i in s]
    s.sort(key=lambda x:len(x))
    answer = []
    for i in s:
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
    return answer

# 0531 재도전
from collections import Counter
def solution(string):
    
    count = []
    for s in string.split(','):
        num = ''
        for t in s:
            if t.isdigit():
                num += t
        count.append(int(num))

    cnt_list = Counter(count).most_common(len(count))
    answer = [i[0] for i in cnt_list]
        
    return answer


s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
print(solution(s))
