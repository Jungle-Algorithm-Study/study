def solution(n):
    temp = [1]
    count = 0
    while temp[-1] <= n:
        if sum(temp) < n:
            temp.append(temp[-1]+1)
        elif sum(temp) > n:
            temp = temp[1:]
        else:
            count += 1
            temp.append(temp[-1]+1)
    return count