input = __import__('sys').stdin.readline

a, b = map(int,input().split())
water = [list(map(int, input().split())) for i in range(a)]
water.sort()

present = 0
cnt = 0
diff = 0

for start, end in water :
    if present > start :
        start = present

    diff = end - start

    if diff%b == 0 :
        cnt += diff//b
        present = start + diff
    else :
        hep = diff//b + 1
        cnt += hep
        present = start + hep*b

print(cnt)
