##########################첫번째 풀이 ##########################
### 60점 밖에 안 나옴
# 연산자는 고유한 우선순위를 가짐
# for 연산자 우선순위[:-1]
#     1. 연산자들의 우선순위를 정한다
#     2. 정규표현식으로 ~숫자기호숫자~ 뽑아내서 계산 결과로 replace한다.
#     3. 마지막-1 연산자까지 1,2를 반복
#     4. 마지막 연산자는 그냥 eval로 퉁친다
#     5. max로 비교하며 갱신

import re
from itertools import permutations

def add_escape(string):
    idx = 1
    while string[idx].isdigit():
        idx += 1
    if string[idx] == '-':
        return string
    return  f"{string[:idx]}\\{string[idx]}{string[idx+1:]}"


def solution(expression):
    answer = 0
    
    priorities = permutations(["+", "-", "*"])

    for prior_oper in priorities:
        temp_expression = expression
        # print("우선순위:", prior_oper)
        for o in prior_oper[:-1]:
            # -는 수량 연산자가 아니라 \가 필요 없다
            # p = f'\\d+\\{o}\\d+' if o != '-' else f'\\d+{o}\\d+'
            
            # 근데 그냥 []안에 쓰면 되겠다
            p = f'\\d+[{o}]\\d+'
            detected = re.search(p, temp_expression)
    
            while detected:
                detected = detected.group() # 숫자연산자숫자 의 형태가 감지되면 ma
                if temp_expression[:1+len(detected)] == f"-{detected}":
                    # 맨앞이 -인데 -가 안 들어가는 것 방지
                    detected = add_escape(f"-{detected}")
                else:
                    detected = add_escape(detected)
                result = eval(detected.replace('\\',''))
                temp_expression = re.sub(detected, str(result), temp_expression, 1)
                detected = re.search(p, temp_expression)
        print(abs(eval(temp_expression)))
        answer = max(answer, abs(eval(temp_expression)))
    
    return answer

##########################두번째 풀이 ##########################
## baedonguri님의 풀이를 참고해서 풀어보았습니다
from itertools import permutations
from collections import deque
import re
def solution(expression):
    answer = 0
    
    numbers = re.findall("\d+", expression)
    opers = re.findall('\D', expression)
    
    # 숫자와 연산자들을 하나의 배열로(arr) 만든다
    arr = deque([numbers[0]])
    for n, o in zip(numbers[1:], opers):
        arr.append(o)
        arr.append(n)
        
    for p in permutations(["+", "-", "*"]):
        answer = max(answer, operate_arr(arr.copy(), p))
        
    return answer

def operate_arr(arr, priority):
    for o in priority:
        stack = []
        
        # 배열을 순회하면서 연산자가 나오면 stack의 top과 arr의 popleft를 연산하고 stack에 push
        while arr:
            now = arr.popleft()
            
            if now == o:
                v = str(eval(stack.pop() + o + arr.popleft()))
                stack.append(v)
            else:
                stack.append(now)
        arr = deque(stack)
    
    return abs(int(arr[0]))
