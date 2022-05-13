def solution(progresses, speeds) :
    answer = []
    cnt = 0
    day = 0
    
    while progresses:
        if (progresses[0] + day * speeds[0]) >= 100:
            cnt += 1
            progresses.pop(0)
            speeds.pop(0)
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            day += 1
                
    answer.append(cnt)
    
    return answer

# Test case : [2, 1]
progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))
