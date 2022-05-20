import re
import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    command = input().rstrip()
    
    if len(command) != 7:
        print(0)

    elif len(set(command)) != 2:
        print(0)

    else:
        p = r'^([A-Z])\1([A-Z])\2\1\2\2'
        matched = re.match(p, command)
        print(1 if matched else 0)
