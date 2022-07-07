def solution(n, s):
    if s // n == 0 :
        return [-1]
    
    num, left = divmod(s, n)
    rst = [num] * n
    
    if left :
        for i in range(len(rst)) :
            rst[i] += 1
            left -= 1
            if not left :
                break

    return sorted(rst)
