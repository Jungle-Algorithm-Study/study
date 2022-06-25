def solution(info, edges):
    visited = [0]*len(info)
    visited2 = [0]*len(edges)
    visited[0] = 1
    answer = []
    def dfs(sheep,wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return
        for i in range(len(edges)):
            parent = edges[i][0]
            child = edges[i][1]
            isWolf = info[child]
            if visited[parent] and not visited2[i]:
                visited[child] = 1
                visited2[i] = 1
                dfs(sheep+(isWolf==0), wolf+(isWolf==1))
                visited[child] = 0
                visited2[i] = 0
    dfs(1, 0)
    return max(answer)