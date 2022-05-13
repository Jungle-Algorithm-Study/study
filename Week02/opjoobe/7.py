# 다트게임 # sol 20min # 첫번째 풀이 # TC당 0.02~0.03 ms 
def solution(dartResult):
    ans = []
    now = []
    case = -1
    for i in dartResult:
        if i.isdigit():
            now.append(i)
        else:
            if len(now) > 0:
                ans.append(int(''.join(now)))
                case += 1
                now.clear() # now = []
            if i in ['S','D','T']:
                if i == 'D':
                    ans[case] = ans[case] ** 2
                elif i == 'T':
                    ans[case] = ans[case] ** 3
            else:
                if i == "*":
                    ans[case] *= 2
                    if case > 0:
                        ans[case-1] *= 2
                else:
                    ans[case] *= -1

    print(ans)
    answer = sum(ans)
    return answer

dartResult = "1S*2T*3S"
print(solution(dartResult))

hexint = '8'
newhexint = int(hexint, 16)
print(newhexint)