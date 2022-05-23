# 프로그래머스 # 주식가격 # 25min sol # 백준 탑 문제랑 사실상 똑같은데 풀이법이 기억이 안나서 오래걸림..
def solution(prices):
    n = len(prices)
    answer = list(range(n))[::-1]
    stack = [[0, prices[0]]]
    for now in range(1, n):
        while stack and stack[-1][-1] > prices[now]:
            before = stack.pop()[0]
            answer[before] = now-before
        stack.append([now, prices[now]])
    return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices))