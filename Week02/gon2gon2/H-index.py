def solution(citations):    
    answer = 0
    
    # len(citations)-1일때는 [5,5,5,5,5]케이스에서 안 됐음
    # start가 계속 올라오면서 end와 일치하는 순간이 답이 되는데, -1을 하면 4에서 교차되면서 오답
    start, end = 0, len(citations)
    citations.sort()
    
    while start <= end:
        h = (start+end)//2
        
        if citations[-h] >= h:
            answer = max(answer, h)
            start = h + 1
        
        else:
            end = h -1
    
    return answer
