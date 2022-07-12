k = int(input())
giho = list(input().split())
answer = []
visited = [0] * 10
def dfs(result, index):
    if index == k+1:
        answer.append(result)
        return 
    for i in range(10):
        if not visited[i]:
            if index == 0 or eval(result[-1]+giho[index-1]+str(i)):
                visited[i] = 1
                dfs(result+str(i), index+1)
                visited[i] = 0
dfs("",0)

# for문 때문에 마지막에 나온게 max고 처음이 가장 작음
print(answer[-1])
print(answer[0])