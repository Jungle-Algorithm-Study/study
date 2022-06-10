def solution(enroll, referral, seller, amount):

    parent_of = {e: r for e,r in zip(enroll, referral)}
    stack = [[s, parent_of[s], 100*a] for s,a in zip(seller, amount)]
    result = {e:0 for e in enroll}
    
    # 부모와 내가 준 0.1을 추가
    while stack:
        src, dst, val = stack.pop()      
        go_up = val//10
        
        
        if go_up < 1: # 상납 X
            result[src] += val
            
        else: # 상납 O
            result[src] += val-go_up
            if dst in parent_of:
                stack.append([dst, parent_of[dst], go_up])
            
    
    return [result[k] for k in enroll]


