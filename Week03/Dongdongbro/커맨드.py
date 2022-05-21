import re

T = int(input())
for _ in range(T) :
    a = input()

    if re.fullmatch('([A-Z])\\1([A-Z])\\2\\1\\2\\2', a) and a[0] != a[2] :
        print(1)
        continue
