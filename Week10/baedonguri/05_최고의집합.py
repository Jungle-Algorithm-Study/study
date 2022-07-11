# from itertools import combinations_with_replacement as H

# def solution(n,s):
#     answer = []
#     for i in H(range(s),n):
#         if sum(i) == s:
#             answer.append(list(i))

#     if not answer:
#         return [-1]
#     tmp = [i[0]*i[1]for i in answer]

#     idx = tmp.index(max(tmp))

#     return answer[idx]


def solution(n,s):
    answer = []
    x,y = divmod(s,n)
    if x < 1:
        return [-1]

    for i in range(n):
        answer.append(x)
    
    idx = len(answer)-1

    for i in range(y):
        answer[idx-i] = answer[idx-i] + 1

    return answer
        

print(solution(2,8))