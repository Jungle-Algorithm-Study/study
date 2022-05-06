#체육복~
def solution(n, lost, reserve):
    rst = 0
    lost.sort()
    reserve.sort()
    temp = lost.copy()
    
    for value in temp :
        if reserve.count(value):
            lost.remove(value)
            reserve.remove(value)

    for l in lost :
        if reserve.count(l - 1) :
            rst += 1
            reserve[reserve.index(l - 1)] = 0
        elif reserve.count(l + 1) :
            rst += 1
            reserve[reserve.index(l + 1)] = 0
        else :
            continue
            
    return (n - len(lost)) + rst

#testCase
n = 8
lost = [1, 2, 3, 4]
reserve = [1, 2, 3, 4]

print(solution(n, lost, reserve))
