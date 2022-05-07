# 폰켓몬

def solution(nums):
    limit = len(nums) // 2
    nums = set(nums)
    answer = len(nums)
    
    if answer > limit :
      return limit
    else :  
      return answer 

nums = [3,3,3,2,2,4]
print(solution(nums))
