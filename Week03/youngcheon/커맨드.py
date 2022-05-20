import re
for _ in range(int(input())):
    s = input()
    answer=re.fullmatch('([A-Z])\\1([A-Z])\\2\\1\\2\\2',s) 
    print(1 if answer and s[0]!=s[2] else 0)
