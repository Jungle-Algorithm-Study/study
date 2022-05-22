'''
begin에서 target으로 바꾸는 가장 짧은 변환과정
한 단어만 다른 애로 바꾸고 내가 없는 리스트를 한번 더 탐색
'''
def change_possible(foo, bar):
    ''''''
    n = len(foo)
    cnt = 0
    for i in range(n):
        if foo[i] == bar[i]:
            cnt += 1
    return n-1 == cnt


def dfs(now, candidate, count, target):
    
    if now == target:
        return count
    
    ans = 999999
    for i in range(len(candidate)):
        # 다른 갯수 비교
        if change_possible(now, candidate[i]):
            result = dfs(candidate[i], candidate[:i]+candidate[i+1:], count+1, target)
            ans = min(ans, result)
    
    return ans
    


def solution(begin, target, words):
    if target not in words:
        return 0
    answer = 99999
    answer = min(answer, dfs(begin, words, 0, target))
    
    return answer
