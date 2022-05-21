# 5월14일 7시15분시작 # 22min sol
# 백준 커맨드 

# 첫번째 풀이 
import sys, re
input = sys.stdin.readline

def solution(command):
    if len(command) != 7:
        return 0
    A = command[0]
    B = command[2]
    p = re.compile(A)
    new_command = p.sub('1',command)
    p = re.compile(B)
    new_command = p.sub('2',new_command)
    return 1 if new_command == '1122122' else 0

# 두번째 풀이
import sys,re
input = sys.stdin.readline

def solution(command):
    # re.fullmatch('([A-Z])\\1([A-Z])\\2\\1\\2\\2',command) 에서 착안해 그룹으로 변경 
    return 1 if re.fullmatch(r'(?P<A>[A-Z])(?P=A)(?P<B>[A-Z])(?P=B)(?P=A)(?P=B)(?P=B)',command) and command[0]!=command[2] else 0
    # 이거 근데 왜 command[0] != command[2] 빼면 안되는거죠?

for _ in range(int(input())):
    print(solution(input().strip()))