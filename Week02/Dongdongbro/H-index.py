def solution(citations):
    citations.sort(reverse = True)
    for i in range(0, len(citations)):
        if i >= citations[i] :
            return i
    return len(citations)
  
 '''
 enumerate함수를 사용한다면?
 def solution(citations):
    citations.sort(reverse = True)
    # for i in range(0, len(citations)):
    #     if i >= citations[i] :
    #         return i
    # return len(citations)
    for idx, value in enumerate(citations) :
        if idx >= value :
            return idx
    return len(citations)
'''
