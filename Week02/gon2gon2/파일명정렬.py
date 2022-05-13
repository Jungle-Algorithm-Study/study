def find_head(name):
    idx = 0
    while idx<len(name) and not name[idx].isdigit():
        idx += 1
    return idx

def find_number(name):
    idx = 0
    while idx<len(name) and name[idx].isnumeric():
        idx += 1
    return idx

def solution(files):
    answer = []
    for i,f in enumerate(files):
        
        # f = '-----1' <- 런타임에러 잡는 데에 도움됨
        
        # head 찾기
        head_idx = find_head(f)
        head = f[:head_idx]
        rest = f[head_idx:]
        
        # number, tail 찾기
        number_idx = find_number(rest)
        number = rest[:number_idx]
        tail = rest[number_idx:]
        
        answer.append([head.lower(), int(number), tail, i])
        
    answer.sort(key=lambda x:(x[0], x[1], x[3], x[2]))
    answer = [files[i] for h,n,t,i in answer]
    return answer
