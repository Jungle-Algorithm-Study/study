import sys
input = sys.stdin.readline

P = "0011011"
T = int(input())

for t in range(T):
    
    command = input().strip()
    set_command = set(command)

    if len(command) != 7:
        print(0)
        continue

    elif len(set_command) != 2:
        print(0)
        continue
    
    idx = 0
    dict_for_pattern = dict()
    for c in command:
        if c not in dict_for_pattern:
            dict_for_pattern[c] = str(idx)
            idx += 1
            
    pattern = ""
    for c in command:
        if not c.isupper():
            break
        pattern += dict_for_pattern[c]

    if pattern != P:
        print(0)
        continue

    print(1)