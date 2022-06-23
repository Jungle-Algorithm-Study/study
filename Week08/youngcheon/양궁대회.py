# start 7:10 
# end 8:30
def solution(n, info):
    answer = []
    score = list(range(10,-1,-1))
    
    # dfs함수 정의
    def dfs(n, result, total, index, apeach,priority):
    # n = 화살갯수 / result = 출력리스트/ total = 내 점수
    # index = 인덱스,종료조건 / apeach = 어피치 점수 / priority = 우선순위(낮은 점수일 수록 높음)
        apeach_score = score[index] if info[index] else 0
        if index==10: # 종료조건
        	# answer 리스트에 저장 ( +[n] 은 남은 화살 다쏘기)
            answer.append([total-apeach,result+[n],priority])
            return
        elif n == 0: # 화살이 없을때 (리스트 뒤에 0 채워주기 위함)
            dfs(n, result+[0], total, index+1, apeach+apeach_score,priority)
        else:
            for i in range(2): # 두가지 경우의 수 : 쏘지 않고 넘길때, 쏠 때
                if i == 0: # 쏘지 않고 넘길때
                    dfs(n, result+[0], total, index+1, apeach+apeach_score, priority)
                else: # 어피치보다 1발 더쏘기
                    ryan = info[index]+1
                    if n-ryan<0: # 1발 더쏘려고하는데 화살이 부족할때
                        dfs(n, result+[0],total,index+1,apeach+apeach_score, priority)
                    else:
                        # 어피치보다 한발 더 쏘는경우
                        # result list에 ryan변수만큼 추가, 점수추가, 우선순위점수 추가
                        # 화살 갯수 감소 ( n - ryan )
                        dfs(n-ryan,result+[ryan],total+score[index],index+1,
                            apeach, priority+score[10-index])
    
    # dfs 실행
    dfs(n, [], 0, 0, 0, 0)
    
    # 점수차이와 우선순위 기준으로 sort, 점수차이와 우선순위는 클 수록 좋으므로 뒤집어줌
    answer.sort(key=lambda x: [x[0],x[2]], reverse = True)
    
    # 점수차가 나지않는경우(이길수 없는경우) -1 리턴
    if answer[0][0] <= 0:
        return [-1]
    else:
    	# 내가 이긴 경우
        # result list 리턴
        return answer[0][1]