# 다트게임 # sol 20min # 첫번째 풀이 변경 # 정규표현식 공부해야 할듯.
def solution(dartResult):
    ans = [] 
    now = [] #defaultdict 쓰면 ans로 다 할수는 있을듯
    idx = -1
    for i in dartResult:
        print(i, ans)
        if i.isdigit():
            now.append(i)
        else:
            if now: # len(now) > 0
                ans.append(int(''.join(now)))
                idx += 1 
                now.clear() # now = []
            if i in ['S','D','T']:
                if i == 'D':
                    ans[idx] = ans[idx] ** 2
                elif i == 'T':
                    ans[idx] = ans[idx] ** 3
            else:
                if i == "*":
                    ans[idx] *= 2
                    if idx > 0:
                        ans[idx-1] *= 2
                else:
                    ans[idx] *= -1
    answer = sum(ans)
    return answer

dartResult = "1S*2T*3S"
print(solution(dartResult))