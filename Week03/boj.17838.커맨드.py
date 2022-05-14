import re

for _ in range(int(input())) : # trycnt
    cmd = input().rstrip()
    if re.fullmatch('([A-Z])\\1([A-Z])\\2\\1\\2\\2', cmd) and cmd[0] != cmd[2]:
        print(1)    
        continue
    print(0)
