def solution(n, words):
    lists = []
    result = []
    for idx, val in enumerate(words) :
        if not lists :
            lists.append(val)
            continue
        
        person = idx%n

        if (val in lists) or (lists[-1][-1] != val[0])  :
            result.append([person+1,idx//n+1])
            return result[-1]
        lists.append(val)
        
    if not result :
        return [0,0]
