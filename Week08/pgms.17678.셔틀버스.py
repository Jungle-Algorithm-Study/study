def solution(busCnt, itv, sheet, waitline):
    answer = ''
    line = []
    bus = []
    
    for w in waitline :
        h, m = map(int, w.split(":"))
        line.append(h * 60 + m)
        
    line.sort()
    
    for n in range(busCnt) :
        bus.append([540 + (itv * n), []])
    
    for b in bus :
        limit = sheet
        while line :
            if line[0] > b[0] or not limit :
                break
            if line[0] <= b[0] and limit :
                b[1].append(line.pop(0))
                limit -= 1
    
    if len(bus[-1][1]) < sheet :
        a, b = map(str, divmod(bus[-1][0], 60))
    elif len(bus[-1][1] ) == sheet:
        a, b = map(str, divmod(bus[-1][1].pop() - 1, 60))
    
    return a.zfill(2) + ":" + b.zfill(2)
