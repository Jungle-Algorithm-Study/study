def solution(progresses, speeds):
    answer = []
    sum = [0] *(len(speeds))
    for i in range(len(speeds)) :
        if (100-progresses[i])%speeds[i] == 0:
            sum[i] = (100-progresses[i])//speeds[i]
        else :
            sum[i] = (100-progresses[i])//speeds[i]+1
    count = 1
    start = sum[0]
    for i in range(1, len(sum)) :
        if sum[i] <= start :
            count += 1
        else :
            answer.append(count)
            start = sum[i]
            count = 1
    answer.append(count)

    print(sum)
    print(answer)
    return answer