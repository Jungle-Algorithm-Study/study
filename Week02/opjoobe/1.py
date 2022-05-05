def solution(nums):
    return len(set(nums)) if len(set(nums)) < len(nums)//2 else len(nums)//2
    
# def solution(nums):
#     answer = 0
#     total_cnt = len(nums)
#     unique_cnt = len(set(nums))
#     half_cnt = total_cnt//2
#     answer = unique_cnt if unique_cnt < half_cnt else half_cnt
    
#     return answer

nums = [3,1,2,3]

print(solution(nums))