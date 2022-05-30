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

s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
print(solution(s))