# 영천이꺼 참고해서 풀었음
import re
from sys import stdin
input = stdin.readline

def solution(commend):
    if len(commend) != 7:
        return 0
    m = re.match('([A-Z])\\1([A-Z])\\2\\1\\2\\2',commend)
    
    if m is not None and commend[0] != commend[2]:
        return 1

for i in range(int(input())):
    cmd = input().rstrip()

    answer = solution(cmd)

    print(1 if answer else 0)