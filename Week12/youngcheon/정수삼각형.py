def solution(triangle):
    # 맨윗줄은 연산할 필요 없으니 두번째 줄부터 연산함
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            # 그 줄의 첫번째 요소라면 그냥 위에있는거 더함
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            # 그 줄의 마지막 요소라면 그냥 위에있는거 더함
            elif j == len(triangle[i])-1:
                triangle[i][j] += triangle[i-1][-1]
            # 중간에 있는 요소라면 그 위에있는 두 수중에 큰값을 골라 더함
            else:
                triangle[i][j] += max(triangle[i-1][j-1:j+1])
    # 이렇게 for문으로 더해 내려가다보면 마지막 줄의 max값이 정답임
    return max(triangle[-1])