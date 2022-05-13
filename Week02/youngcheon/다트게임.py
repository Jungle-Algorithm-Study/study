def solution(dartResult):
    # 10을 A로 바꿔줌
    dart = dartResult.replace('10','A')
    stack = []
    for i in dart:
        if i=='A' or i.isdigit(): # A이거나 10
            stack.append(int(i) if i != 'A' else 10)
        elif i.isalpha(): #S,D,T일 경우
            stack[-1] **= {'S':1,'D':2,'T':3}[i]
        elif i == '#': # '#'일 경우 -1 곱함
            stack[-1] *= -1
        else: # '*' 일 경우 뒤에서부터 두개를 2배해서 다시 넣어줌
            temp = []
            temp.append(stack.pop()*2)
            if stack:
                temp.append(stack.pop()*2)
            stack.extend(temp[::-1])
    return sum(stack) #stack의 합 출력