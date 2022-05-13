# 첫번째 풀이
# import re
# def solution(dartResult):
    
#     times = {
#         "S" : 1,
#         "D" : 2,
#         "T" : 3,
#     }
    
#     bonus = re.split(r'\d', dartResult)[1:]
#     bonus = [b for b in bonus if b]
#     point = [*map(int, re.findall(r'[\d]+',dartResult))]
    
#     stack = []
#     for p, b in zip(point, bonus):
#         now = p ** times[b[0]]
        
#         # 스타상
#         if b[-1] == "*":
#             if stack:
#                 stack[-1] = stack[-1] * 2
#             stack.append(now * 2)
            
#         # 아차상
#         elif b[-1] == "#":
#             stack.append(now * -1)
            
#         else:
#             stack.append(now)
    
#     answer = sum(stack)
    
#     return answer




# 2번째 풀이
import re
def solution(dartResult):
    
    times = {
        "S" : 1,
        "D" : 2,
        "T" : 3,
    }
    
    
    p = r'(\d+)([SDT])([*#])?'
    p = re.compile(p)
    dart = p.findall(dartResult)
    
    stack = []
    
    for n,b,o in dart:
        now = int(n) ** times[b]
        
        if o == '*':
            if stack:
                stack[-1] *= 2
            stack.append(now*2)
            
        elif o == '#':
            stack.append(now*-1)
        
        else:
            stack.append(now)
        
    answer = sum(stack)
    
    return answer