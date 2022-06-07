def solution(n):
    answer = 1
    
    for i in range(1, n) :
        temp = 0
        num = i
        
        while 1 :
            temp += num
            num += 1
            if temp == n :
                answer += 1
            elif temp > n :
                break
    
    return answer
