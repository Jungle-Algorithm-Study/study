def convert(n):
    ret = ''
    while n>0:
        # 3진법
        n, mod = divmod(n, 3)
        # 나머지가 0이면 4로 바꿔줘야함, 
        # 자릿수도 낮아져야 하므로 n-1
        if mod == 0:
            mod = 4
            n -= 1
        ret += str(mod)
    return ret[::-1]

def solution(n):
    return convert(n)