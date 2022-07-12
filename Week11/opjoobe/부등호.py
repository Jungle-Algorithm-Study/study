# 백준 # 부등호 # 26min sol

from sys import stdin
input = stdin.readline

k = int(input())
L = input().strip().split()

answer = []
now = []
def backtracking(n, now):
    # if not now:
    #     return
    if n == k:
        answer.append(''.join(list(map(str,now))))
        return
    if L[n] == '>':
        for i in range(int(now[-1])):
            if str(i) in now:
                continue
            backtracking(n+1, now + list(str(i)))
    else:
        for i in range(int(now[-1])+1, 10):
            if str(i) in now:
                continue
            backtracking(n+1, now + list(str(i)))

for i in range(10):
    backtracking(0, [str(i)])
print(answer[-1])
print(answer[0])

''' 기존에 생각한 풀이 '''
# 부등호 k개
# 숫자는 0부터 9

# < < < < 
# ㅁ<ㅁ<ㅁ<ㅁ<ㅁ 

# < 개수에 따라서 달라진다. 
# < 가 4개면, 앞에 올수있는 최댓값 = 9-4 = 5
# < 가 1개면, 앞에 올 수 있는 최대값 = 9-1 = 8

# > > > 

# 마지막 숫자 ㅁ 을 기준으로, -1씩 하는게 최댓값.
# 만약 이렇게 했는데 마지막 숫자가 -1 이하다? 그러면 앞에꺼(before)죄다 +?

# < < < < 마지막 숫자 ㅁ 을 기준으로 +1씩 하는게 최소
# 만약 이렇게 했는데 마지막 숫자가 10이상이다? 그럼 앞에꺼(before) 죄다 -?