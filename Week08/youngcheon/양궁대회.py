# start 7:10 
# end 8:30
def solution(n, info):
    answer = []
    
    # 10,9...1,0 score
    score = list(range(10,-1,-1))
    
    # (8, 18 test case) reversed score list for priority
    reverse_score = score[::-1]
    
    # dfs함수
    def dfs(n, result, total, index, apeach,priority):
        if index==10:
            answer.append([total-apeach,result+[n],priority])
            return
        elif n <= 0: # 화살이 없을때 (리스트 뒤에 0 채워주기 위함)
            if info[index]: # 어피치 점수 있을때
                dfs(n, result+[0], total, index+1, apeach+score[index],priority)
            else: # 어피치 0점
                dfs(n, result+[0], total, index+1, apeach,priority)
        else:
            for i in range(2):
                if i == 0: # 두가지 경우의 수 : 쏘지 않고 넘길때,  쏠때
                    if info[index]: # 나는 쏘지 않는데 어피치는 쐈을때
                        dfs(n, result+[0], total, index+1, apeach+score[index], priority)
                    else: # 나도 쏘지 않고 어피치도 쏘지 않을때
                        dfs(n, result+[0], total, index+1, apeach,priority)
                else: # 어피치보다 1발 더쏘기
                    ryan = info[index]+1
                    if n-ryan<0: # 1발 더쏘려고하는데 화살이 부족할때
                        if info[index]:
                            dfs(n, result+[0], total, index+1, apeach+score[index], priority)
                        else:
                            dfs(n, result+[0], total, index+1, apeach, priority)
                        return
                    else:
                        # 어피치보다 한발 더 쏘는경우
                        # result list에 ryan변수만큼 추가, 점수추가, 우선순위점수 추가
                        dfs(n-ryan,result+[ryan],total+score[index],index+1,apeach, priority+reverse_score[index])
    
    # dfs 실행
    dfs(n, [], 0, 0, 0, 0)
    
    # 점수차이와 우선순위 기준으로 sort, 점수차이와 우선순위는 클 수록 좋으므로 뒤집어줌
    answer.sort(key=lambda x: [x[0],x[2]], reverse = True)
    
    # 점수차가 나지않는경우(이길수 없는경우) -1 리턴
    if answer[0][0] <= 0:
        return [-1]
    else:
        # result list 리턴
        return answer[0][1]