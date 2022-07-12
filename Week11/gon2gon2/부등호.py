k = int(input())
sign = input()

check = lambda x, y, sign: eval(f"{x} {sign} {y}")

def solution(k, sign):
    answer = []
    MIN = int((k+1)*'9')
    MAX = 0
    sign = sign.split()

    # 현재 인덱스, 지금까지의 숫자 배열, 
    stack = [[0, [i]] for i in range(10)]


    while stack:
        now_idx, now_arr = stack.pop()

        if len(now_arr) == k+1:
            now_arr = [*map(str, now_arr)]
            MIN = min(MIN, int("".join(now_arr)))
            MAX = max(MAX, int("".join(now_arr)))
            continue


        # arr[-1]보다 작아져야 함
        if sign[now_idx] == ">":
            for i in range(now_arr[-1], -1, -1):
                if i not in now_arr and check(now_arr[-1],i,sign[now_idx]):
                    stack.append([now_idx+1, now_arr+[i]])
        else:
            for i in range(0, 10, 1):
                if i not in now_arr and check(now_arr[-1],i,sign[now_idx]):
                    stack.append([now_idx+1, now_arr+[i]])
            
        
    answer = list(map(lambda x: str(x).zfill(k+1),[MIN, MAX]))

    print(max(answer))
    print(min(answer))
    
    
solution(k, sign)