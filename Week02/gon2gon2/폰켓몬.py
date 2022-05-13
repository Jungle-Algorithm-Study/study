# 시작: 16:22
# 종료: 16:26

def solution(nums):
    '''
    N마리 중 N/2마리
    폰켓몬 번호 == id
    '''
    
    # 풀이 1
    # n//2와 고유한 숫자의 갯수를 비교해 더 적은 거로 반환 
    # 만약 고유한 포켓몬의 개수가 적으면 중복제거된 모든 포켓몬 id가 고유한 아이디가 충분히 많다면 n//2가 반환
    return min(len(set(nums)), len(nums)//2)


    # 풀이 2
    # 구구절절 combination -> 시간 초과
    
#     from itertools import combinations
    
#     n = len(nums)
#     answer = 0
#     for comb in combinations(nums, n//2):
        
#         answer = max(answer, len(set(comb)))
        
#     return answer

