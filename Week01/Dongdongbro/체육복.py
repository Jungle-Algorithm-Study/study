def solution(n, lost, reserve):
    answer = 0
    students = [1] * (n+2)
    for i in lost :
        if i not in reserve :
            students[i] = 0
    for i in reserve :
        if i not in lost :
            students[i] = 2
    print(students)
    for i in range(1,n+1) :
        if students[i] == 0 :
            if students[i-1] == 2 :
                students[i-1] = 1
                students[i] = 1 
                continue
            elif students[i+1] ==2 :
                students[i+1] = 1
                students[i] = 1
                continue
        else :
            continue
    print(students)
    for i in students :
        if i >= 1 :
            answer += 1
    answer -= 2
    print(answer)
    return answer