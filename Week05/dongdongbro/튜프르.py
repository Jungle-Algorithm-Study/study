def solution(s):
    answer = []
    a = s.split('},{')
    b = list(map(lambda x : x.replace('{','').replace('}','').split(','),a))
    b.sort(key = lambda x: len(x))
    for i in b :
        for j in i :
            if int(j) not in answer:
                answer.append(int(j))
        
    return answer

# def solution(s):

#     s = Counter(re.findall('\d+', s))
#     return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

# import re
# from collections import Counter
