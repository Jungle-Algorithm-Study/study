input = __import__('sys').stdin.readline

cnt, long = map(int, input().split())
puddles = [tuple(map(int, input().split())) for _ in range(cnt)]
rst, curr = 0, 0

for puddle in sorted(puddles) :
    start, end = puddle
    
    if end > curr :
        if start < curr :
            start = curr

        need = (end - start + (long - 1)) // long
        rst += need
        curr = start + (need * long)
    
print(rst)
