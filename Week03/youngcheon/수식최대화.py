from itertools import permutations
import re
answer = []

# 계산해서 다시 리스트로 만드는 함수
def fuc(li,i):
    if len(li) == 3:
        return str(abs(eval(''.join(li))))
    idx = li.index(i)
    temp = li[:idx-1]
    temp.append(str(eval(str(li[idx-1])+str(li[idx])+str(li[idx+1]))))
    temp.extend(li[idx+2:])
    return temp

def solution(exp):
    # 연산자 우선순위 경우의수 
    t = list(permutations(['-','+','*']))
    
    # 숫자와 연산자 쪼개서 다시 담기
    nums = re.split('[\-|\*|\+]',exp)
    opers = re.findall('[\-|\*|\+]',exp)
    res = []
    for n,o in zip(nums,opers):
        res.append(n)
        res.append(o)
    res.append(nums[-1])
    #여기까지 수행하면 ['100', '-', '200', '*', '300', '-', '500', '+', '20'] 이런식으로 됨
    
    #우선순위 경우의수 다돌기
    for j in t:
        temp = res[:]
        for i in j:
            # 연산자가 있을때까지 수행
            while i in temp:
                temp = fuc(temp, i)
        # 결과값 담기
        answer.append(int(temp))
    # 최대값 반환
    return max(answer)