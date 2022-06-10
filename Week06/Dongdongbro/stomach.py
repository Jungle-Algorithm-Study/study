def solution(clothes):
    answer = {}
    for i in clothes :
        if i[1] in answer : answer[i[1]] += 1
        else : answer[i[1]] = 1
    count = 1
    for val in answer.values() :
        count *= (val+1)
    
    return count -1
  
'''
def solution(clothes):
  from collections import Counter
  from functools import reduce
  cnt = Counter([kind for name, kind in clothes])
  answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
  return answer
'''
