# 프로그래머스 # 줄서는방법 # 25min sol

""" 첫번째 풀이(5min): 시간초과 """
def solution2(n, k):
    from itertools import permutations
    L = list(range(1,n+1))
    answer = []
    a = n
    return list(permutations(L,n))[k-1]

""" 두번째 풀이(20min): (n-1)!로 k를 나누면, 첫번째 숫자를 찾을 수 있을 것 같다는 아이디어로 시작 """
def factorial(n):
    if n <= 1: return 1
    return factorial(n-1)*n

def solution(n, k):
    from itertools import permutations
    L = list(range(1,n+1))
    answer = []
    a = n
    k -= 1 # 이거 조정하는 부분에서 오래걸림. (k를 맨 처음에만 -1 해주면 되는데, while문에서 매번 -1 해줘야한다고 생각했음)
    while L :
        idx, k = divmod(k, factorial(a-1))
        target = L[idx]
        answer.append(target)
        L.remove(target)
        a-=1
    return answer

n = 3
k = 5

print(solution(n,k))
print(solution2(n,k))

# print(divmod(0,1))
# print(divmod(-1,1))
