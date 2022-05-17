from itertools import permutations
import re

expression ="100-200*300-500+20"


def func(expression, op):
    arr = []
    ops = [e for e in expression if not e.isdigit()]
    nums = [e for e in re.split('[^0-9]',expression)]
    for x,y in zip(nums,ops):
        arr.append(x); arr.append(y)
    arr.append(nums[-1]) # ['100', '-', '200', '*', '300', '-', '500', '+', '20']과 같은 형태로 만들어줌

    for o in op: 
        stack = []
        while len(arr) != 0:
            tmp = arr.pop(0)
            if tmp == o:
                stack.append(calc(stack.pop(), arr.pop(0), o))
            else:
                stack.append(tmp)
        arr = stack

    return abs(int(arr[0]))
    
    
def calc(num1, num2, op):
    if op == '+':
        return str(int(num1) + int(num2))
    if op == '-':
        return str(int(num1) - int(num2))
    if op == '*':
        return str(int(num1) * int(num2))


def solution(expression):
    op = ['+', '-', '*']
    result = []
    for p in permutations(op, 3):
        result.append(func(expression, p))
    return max(result)


print(solution(expression))
