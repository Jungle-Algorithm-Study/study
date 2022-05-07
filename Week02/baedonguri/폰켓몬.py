def solution(nums):
    n = len(nums)//2
    k = len(set(nums))
    if n <= k: return n
    return k