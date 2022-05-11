def solution(files):
    answer = []
    head = ''
    num = ''
    tail = ''
    
    for file in files :
        for i in range(len(file)) :
            if file[i].isdigit() :
                head = file[:i]
                num = file[i:]
                for j in range(len(num)) :
                    if not num[j].isdigit() :
                        tail = num[j:]
                        num = num[:j]
                        break
                answer.append([head, num, tail])
                head, num, tail = '','',''
                break
    answer = sorted(answer, key= lambda x:(x[0].lower(), int(x[1])))
    answer = ["".join(i) for i in answer]
    return answer
